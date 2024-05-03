from django.shortcuts import render, redirect
from .models import ContactUs
from .forms import ContactForm, MessageForm


def Contact(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, 'contact_us/contact.html', context={'form': form})
