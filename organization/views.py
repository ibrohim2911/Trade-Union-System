from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import organizationRegistrationForm
def register(request):
    if request.method == 'POST':
        form = organizationRegistrationForm(request.POST)
        if form.is_valid():
            organization = form.save()
            login(request, organization)  # Log in the newly registered organization
            return redirect('home')  # Redirect to your desired page after successful registration
    else:
        form = organizationRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_organization(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        organization = authenticate(email=email, password=password)
        if organization is not None:
            if organization.is_active:
                login(request, organization)
                return redirect('home')  # Redirect to your desired page after successful login
            else:
                # Handle inactive organization case (e.g., display an error message)
                pass
        else:
            # Handle invalid login credentials (e.g., display an error message)
            pass
    else:
        form = AuthenticationForm()  # You can use a custom login form if needed

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_organization(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
   
