from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm # import the form we created in forms.py
from django.contrib.auth.decorators import login_required # import the login required decorator

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
    return render(request=request, template_name='users/profile.html') # render the profile page