from django.shortcuts import render
from .models import Entry

def index(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', {'entries':entries})

# Create your views here.
def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry':entry})