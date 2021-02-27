from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.

def accueil(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":

        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['doc.m.scialom@gmail.com'],  # to email
        )

        return render(request, 'contact.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message': message
        })

    else:
        return render(request, 'contact.html', {})


def apropos(request):
    return render(request, 'about.html', {})


def rdv(request):
    if request.method == "POST":
        nom = request.POST['nom']
        tel = request.POST['tel']
        email = request.POST['email']
        moment = request.POST['moment']
        day = request.POST['day']
        message = request.POST['message']

        # Build request
        appointment_request = "Je souhaite un rendez-vous de préférence le " + day + " " + moment + "." \
                              + " Mon numéro est: " + tel + "." + message

        # Send an email
        send_mail(
            nom,  # subject
            appointment_request,  # message
            email,  # from email
            ['doc.m.scialom@gmail.com'],  # to email
        )

        return render(request, 'booknow.html', {
            'nom': nom,
            'tel': tel,
            'email': email,
            'moment': moment,
            'day': day,
            'message': message})

    else:
        return render(request, 'booknow.html', {})
