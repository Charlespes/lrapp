import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from lrapp.account.models import FavPage, FavCategory
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].encode('UTF-8')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            favcategory = FavCategory(user=user, created_on=datetime.datetime.now())
            favcategory.save()
            favpage = FavPage(user=user, created_on=datetime.datetime.now())
            favpage.save()
            return redirect('/')
        else:
            print form.error_messages
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

