from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm # import the form we created in forms.py

def register(request):
    if request.method == 'POST': # if the request is a POST request
        form = UserRegisterForm(request.POST) # create a form with the POST data
        if form.is_valid():
            form.save() # save the form
            username = form.cleaned_data.get('username') # get the username from the form
            messages.success(request, f'Account created for {username}!') # send a success message
            return redirect('blog-home') # redirect to the home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) # form value is the form variable defined above