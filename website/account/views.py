from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.forms import RegistrationForm
from django.contrib.auth.models import User

def AccountRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])
            user.save()
            account = user.get_profile()
            account.name = form.cleaned_data.get('real_name', None)
            account.save()
            return HttpResponseRedirect('/profile/')
        else:
                return render_to_response('register.html', {'form':form}, context_instance = RequestContext(request))
    else:
        ''' pusty formularz '''
        form = RegistrationForm()
        context ={'form': form}
        return render_to_response('register.html', context, context_instance = RequestContext(request))

