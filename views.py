from django.views.generic.edit import FormView
from django.contrib.auth.models import User

__author__ = 'episage'
from django.views.generic import TemplateView
from forms import SignUpForm
from django.shortcuts import render
from django.http import *


class Homepage(TemplateView):
    template_name = "homepage.html"


class SignUpView(FormView):
    template_name = "sign-up.html"
    form_class = SignUpForm
    success_url = "sign-up-success"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = User.objects.create_user(
            form.cleaned_data['login'],
            form.cleaned_data['email'],
            form.cleaned_data['password'])
        user.save()
        return HttpResponse('success')
        return super(SignUpView, self).form_valid(form)

    def form_invalid(self, form):
        errors = [(k, force_unicode(v[0]) ) for k, v in form.errors.items()]
        return HttpResponse(errors)


def sign_up(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SignUpForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user = User.objects.create_user(
                form.cleaned_data['login'],
                form.cleaned_data['email'],
                form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = SignUpForm() # An unbound form

    return render(request, 'sign-up.html', {
        'form': form,
        })