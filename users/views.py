from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST': # if the request is a POST request
        form = UserCreationForm(request.POST) # create a form with the POST data
        if form.is_valid():
            username = form.cleaned_data.get('username') # get the username from the form
            messages.success(request, f'Account created for {username}!') # send a success message
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form}) # form value is the form variable defined above