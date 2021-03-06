from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from . import forms

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return render(request, 'accounts/profile.html', {
                        'form': form
                    })
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            # login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('login'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('accounts:sign_in'))


@login_required
def profile(request, pk):
    """Display User Profile"""
    profile = request.user.profile
    profiles = models.Profile.objects.all()
    return render(request, 'accounts/profile.html', {
        'profile': profile, 'profiles': profiles
    })


@login_required
def edit_profile(request, pk):
    user = request.user
    profile = get_object_or_404(models.Profile, user=user)
    form = forms.ProfileForm(instance=profile)

    if request.method == 'POST':
        form = forms.ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Profile Successfully!")
            return render(request, 'accounts/profile.html', {
                'form': form
            })

    return render(request, 'accounts/edit_profile.html', {
        'form': form
    })


@login_required
def change_password(request, pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'accounts/profile.html', {
                'form': form
            })
            
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def company(request, pk):
    """Display User Company"""
    company = request.user.company
    return render(request, 'accounts/company.html', {
        'company': company
    })

@login_required
def edit_company(request, pk):
    user = request.user
    company, _ = models.Company.objects.get_or_create(user=user)
    form = forms.CompanyForm(instance=company)

    if request.method == 'POST':
        form = forms.CompanyForm(instance=company, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Company Successfully!")
            return render(request, 'accounts/profile.html', {
                'form': form
            })

    return render(request, 'accounts/edit_company.html', {
        'form': form
    })