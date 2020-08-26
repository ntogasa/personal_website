from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    """
    Accepts GET and POST requests and returns the corresponding template. For POST requests,
    contact_view() will check form validity, send an email to the given email address, and
    redirect the user to the 'success' page. In the case of a GET request, contact_view()
    will load a blank form for the user.

    :param request:     A GET or POST request.
    :return:            For GET requests, an empty contact form is loaded. For POST requests, the user
                        is redirected to the 'success' page.
    """
    # If the request is a GET request, then simply load the contact form blank
    if request.method == 'GET':
        form = ContactForm()
    # However if it is not a GET, and instead a POST request, handle the data input in the form
    else:
        form = ContactForm(request.POST)
        # check that all required fields are filled
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            if name:
                subject = f"{name}: {subject}"
            # Attempt to send an email
            try:
                send_mail(subject=subject,
                          message=message,
                          from_email=email,
                          recipient_list=['ntogasa@gmail.com'])
            # Handle any error here, return that Invalid header is found (NEED LANDING PAGE FOR THIS)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    """Accepts a request and returns the rendered 'contact/success.html' template"""
    return render(request, 'contact/success.html')
