from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.views.generic import TemplateView
from forms import NewAccountForm
from django.shortcuts import render
from django.http import *
from hero.models import Hero
from django.template import RequestContext

class Homepage(TemplateView):
    template_name = "homepage.html"


class AccountCreate(CreateView):
    model=User
    template_name = "sign-up.html"

    def form_invalid(self, form):
        errors = [(k, force_unicode(v[0]) ) for k, v in form.errors.items()]
        return HttpResponse(errors)

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(AccountCreate, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dic
        initial = initial.copy()
        SignUpFormset = modelformset_factory(User, form=NewAccountForm)
        formset=SignUpFormset()

        initial['formset'] = formset
        # etc...
        return initial

#class SignUpFormView(FormView):
#    template_name = "sign-up.html"
#    form_class = NewAccountForm
#    success_url = "sign-up-success"
#
#
##    SignUpFormset = modelformset_factory(User, form=SignUpForm)
##    formset=SignUpFormset()
##    print formset
##    test_val= ['kasia','asia',4,2,1]
#
#    def form_valid(self, form):
#        # This method is called when valid form data has been POSTed.
#        # It should return an HttpResponse.
#        user = User.objects.create_user(
#            form.cleaned_data['login'],
#            form.cleaned_data['email'],
#            form.cleaned_data['password'])
#        user.save()
##        return HttpResponse('success')
##        return super(SignUpView, self).form_valid(form)
#
#    def form_invalid(self, form):
#        errors = [(k, force_unicode(v[0]) ) for k, v in form.errors.items()]
#        return HttpResponse(errors)