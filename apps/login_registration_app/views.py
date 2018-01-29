from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)

def current_user(request):
    return User.objects.get(id = request.session['user_id'])

def index(request):

    return render(request, 'login_registration_app/index.html')


def register(request):
    if request.method == "POST":
        # Validate form data
        errors = User.objects.validate_registration(request.POST)

        # Check if errors don't exist
        if not errors:
            # create user
            user = User.objects.create_user(request.POST)

            # log in the user
            request.session['user_id'] = user.id

            # redirect to success page
            return redirect(reverse('dashboard'))

        # flash errors
        flash_errors(errors, request)

    #redirect landing
    return redirect(reverse('landing'))

def login(request):
    if request.method == "POST":
        # Validate my login data
        check = User.objects.validate_login(request.POST)

        # Check if retrieved a valid user
        if check['user']:
            # log in user
            request.session['user_id'] = check['user'].id

            # redirect to success page
            return redirect(reverse('dashboard'))

        # Flash error messages
        flash_errors(check['errors'], request)

    return redirect(reverse('landing'))

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect(reverse('landing'))
