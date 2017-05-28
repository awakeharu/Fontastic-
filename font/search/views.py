from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.forms import ValidationError
from signup.forms import MyLoginForm , MyRegForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

def homepage(request):

    # form = ServiceForm()
    return render(request, 'homepage.html',{'MyLoginForm' :MyLoginForm, 'MyRegForm': MyRegForm ,})