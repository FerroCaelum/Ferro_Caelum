from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from forms import SignUpForm
from django.shortcuts import render
from django.http import *
from hero.models import *

class Homepage(TemplateView):
    template_name = "homepage.html"


class SignUpView(CreateView):
    template_name = "sign-up.html"
    form_class = SignUpForm
    success_url = "sign-up-success"

    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'])
        user.save()
        return HttpResponse('success')

    #        return super(SignUpView, self).form_valid(form)

    def form_invalid(self, form):
        errors = [(k, force_unicode(v[0]) ) for k, v in form.errors.items()]
        return HttpResponse(errors)

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)

        SignUpFormSet = modelformset_factory(User, form=SignUpForm)
        formset = SignUpFormSet(queryset=User.objects.none())
        context['formset'] = formset.as_p()
        return context