from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import View

from app.models import Experience
from project import settings
from .forms import ContactForm
from .render import html_to_pdf


def profile(request):
    template = loader.get_template("profile.html")
    return HttpResponse(template.render({}, request))


def history(request):
    template = "history.html"
    experiences = Experience.objects.all()
    context = {"experiences": experiences}
    return render(request, template, context)


def generate_pdf(request):
    experiences = Experience.objects.all()
    context = {"experiences": experiences}
    pdf = html_to_pdf("history.html", context)
    return HttpResponse(pdf, content_type="application/pdf")


def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, email, [settings.ADMIN_EMAIL])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact.html", {"form": form})


def success(request):
    return HttpResponse("Thanks for your message!")
