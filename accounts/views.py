# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET
 
def register(request):
    """
    View for registering as a new user
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                        amount=100,
                        currency="eur",
                        description=form.cleaned_data['email'],
                        card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    form.save()
                    user = auth.authenticate(email=request.POST.get('email'),
                                            password=request.POST.get('password1'))
                    if user:
                        auth.login(request, user)
                        messages.success(request, "Thank you for registering. I hope you enjoy using Im.Om as much as I've enjoyed making it. Peace, love and thanks.")
                        return redirect(reverse('mytimer'))
                    else:
                        messages.error(request, "unable to log you in at this time!")
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = UserRegistrationForm()
 
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
 
    return render(request, 'register.html', args)



def login(request):
    """
    The login view
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                        password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have succesfully logged in. Now let's meditate.")
                return redirect(reverse('mytimer'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form' :form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    """
    The logout view
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out. See you soon.')
    return redirect(reverse('index'))