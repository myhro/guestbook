import socket
from django.shortcuts import redirect, render
from .forms import PersonForm
from .models import Person

def home(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    people = Person.objects.all()
    return render(request, 'home.html', locals())
