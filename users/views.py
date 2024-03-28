from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # import the form we created in forms.py
from django.contrib.auth.decorators import login_required # import the login required decorator
from django.contrib.auth import logout
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST': # if the request is a POST request
        form = UserRegisterForm(request.POST) # create a form with the POST data
        if form.is_valid():
            form.save() # save the form
            username = form.cleaned_data.get('username') # get the username from the form
            messages.success(request, f'Your Account has been created! You are now able to login') # send a success message
            return redirect('login') # redirect to the home page
    else:
        form = UserRegisterForm()
    return render(request=request, template_name='users/register.html', context={'register_form': form}) # form value is the form variable defined above

@login_required # this decorator will redirect to the login page if the user is not logged in
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated') # send a success message
            return redirect('profile') # redirect to the home page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context=context) # render the profile page

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html') # render the profile page

