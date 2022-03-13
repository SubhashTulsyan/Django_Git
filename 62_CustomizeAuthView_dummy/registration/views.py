from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
class MyLoginView(LoginView):
    template_name = "registration/login.html"  # we have to define

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["next"] = "/login/"
        print("context login: ", context)
        # form, view, next, site, site_name
        return context


class MyLogoutView(LogoutView):
    template_name = "registration/logged_out.html"  # Default template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['next'] = '/login/'
        print("context logout: ", context)
        # form, view, next, site, site_name
        return context


class MyPasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change_form.html"  # Default template
    # success_url = '/password_change_done/' #def value
    form_class = PasswordChangeForm
    # extra_context = {}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("context PasswordChangeView: ", context)
        return context


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"  # Default template
    # extra_context = {}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("context PasswordChangeView: ", context)
        return context


class MyPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset_form.html"  # Default template
    form_class = PasswordResetForm
    email_template_name = "registration/password_reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"
    token_generator = default_token_generator
    from_email = None
    html_email_template_name = None
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # form
        print("context PasswordChangeView: ", context)
        return context


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_form.html"  # Default template
    form_class = PasswordResetForm
    email_template_name = "registration/password_reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"
    token_generator = default_token_generator
    from_email = None
    html_email_template_name = None
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # form
        print("context PasswordChangeView: ", context)
        return context
