from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservations
from .forms import UserRegistrationForm
from django.contrib import messages
from .forms import LoginForm
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def user_registration(request):
    """user registration method to allow users to register"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registration successful! You can now log in.')
            return redirect('user_login')
        else:
            messages.error(
                request,
                'Registration failed. Please check the form errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def homepage(request):
    """Hompage rendering request
    """
    return render(request, "index.html")


def thanks_view(request):
    """Thanks page rendering request"""
    return render(request, 'thanks.html')


def contact(request):
    """Contact page rendering request and method for contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('thanks')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


@login_required
def reservations(request):
    """User reservations method for making a reservation"""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            # Server-side phone number validation
            phone_number = form.cleaned_data['phone']
            if not phone_number.isdigit():
                messages.error(request, 'Enter a valid phone number.')
                return render(request, 'reservations.html', {'form': form})
            reservation.save()
            messages.success(request, 'Reservation created successfully.')
            return redirect('thanksres')
        else:
            messages.error(request, 'Please check the form errors below.')
    else:
        form = ReservationForm()
    return render(request, 'reservations.html', {'form': form})


@login_required
def reservation_list(request):
    """user reservation list method"""
    user_reservations = Reservations.objects.filter(user=request.user)
    if user_reservations:
        return render(
            request, 'reservation_list.html',
            {'reservations': user_reservations})
    else:
        return render(request, 'no_reservations.html')


@login_required
def update_reservation(request, pk):
    """User reservation modification method"""
    reservation = get_object_or_404(Reservations, pk=pk)

    if request.method == 'POST':
        # Check if the requesting user is the same as the user
        # who made the reservation
        if request.user == reservation.user:
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                form.save()
                messages.success(request, 'Reservation updated successfully.')
                return redirect('reservation_list')
            else:
                messages.error(
                    request,
                    'Invalid form data. Please check the form and try again.')
        else:
            messages.error(
                request, 'You are not allowed to update this reservation.')
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'update_reservation.html', {'form': form})


@login_required
def delete_reservation(request, pk):
    """User delete reservation method"""
    reservation = get_object_or_404(Reservations, pk=pk)

    # Check if the requesting user is the same as the user who
    # made the reservation
    if request.user == reservation.user:
        if request.method == 'POST':
            reservation.delete()
            messages.success(request, 'Reservation deleted successfully.')
            return redirect('reservation_list')
        else:
            return render(
                request,
                'delete_reservation.html',
                {'reservation': reservation}
            )
    else:
        messages.error(
            request,
            'You are not allowed to delete this reservation.'
        )
        return redirect('reservation_list')


def user_login(request):
    """User login method"""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('reservations')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    """User logout request"""
    logout(request)
    return redirect('home')


@login_required
def thanksres_view(request):
    return render(request, 'thanksres.html')
