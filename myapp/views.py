from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', {'entries':entries})

# Create your views here.
def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry':entry})

def add(request):
    
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            ###
            name        = form.cleaned_data['name']
            date        = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name    = name,
                date    = date,
                description = description,
            ).save()

            return HttpResponseRedirect('/')
            
    else:
        form = EntryForm()

    return render(request, 'myapp/form.html', {'form': form})