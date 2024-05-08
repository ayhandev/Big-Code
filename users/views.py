from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ResetPasswordForm, SignUpForm, SignInForm, EditProfileForm, ProfileForm
from django.contrib import messages


def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dom:helo')
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    form = SignInForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dom:helo')
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')


@login_required
def edit_profile(request):
    profile = request.user.profile
    user_form = EditProfileForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, 'Ваш профиль успешно обновлен.')
        return redirect('dom:helo')

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'edit_profile.html', context)


def reset_password(request):
    form = ResetPasswordForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            messages.success(request, 'Пароль успешно изменен.')
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('users:sign_in')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ResetPasswordForm(request.user)
    return render(request, 'reset_password.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import Profile


@login_required
def view_profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None
    context = {'user': user, 'profile': profile}
    return render(request, 'profile.html', context)


@login_required
def view_other_profile(request, user_id):
    other_user_profile = get_object_or_404(Profile, pk=user_id)
    context = {'profile': other_user_profile, 'other_user': other_user_profile.user}
    return render(request, 'other_profile.html', context)
