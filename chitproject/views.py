from django.shortcuts import render,redirect
from .forms import ChitForm
from .forms import ChitFund

def register_chit(request):
    if request.method == "POST":
        form = ChitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = ChitForm()
    return render(request, 'register.html', {'form': form})

def view_chits(request):
    chits = ChitFund.objects.all()
    return render(request, 'shop/view.html', {'chits': chits})

def success(request):
    return render(request, 'success.html')
