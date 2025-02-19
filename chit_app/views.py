from django.shortcuts import render, redirect, get_object_or_404
from .models import ChitRegistration
from .forms import ChitForm
from django.http import HttpResponse


def register_chit(request):
    if request.method == "POST":
        form = ChitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ChitForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def view_chits(request):
    query_type = request.GET.get('chit_Type', '')
    query_number = request.GET.get('chit_Number', '')

    chit = None
    if query_type and query_number:
        try:
            chit = ChitRegistration.objects.get(chit_Type=query_type, chit_Number=query_number)
        except ChitRegistration.DoesNotExist:
            chit = None
            
        return render(request, "view_chits.html", {
        "chit": chit,
        "weeks": range(1, 53)
    })

    return render(request, 'view_chits.html', {'chit': chit})

def edit_chit(request, chit_id):
    chit = get_object_or_404(ChitRegistration, id=chit_id)
    
    if request.method == "POST":
        form = ChitForm(request.POST, instance=chit)
        if form.is_valid():
            form.save()
            return redirect('view_chits')
    else:
        form = ChitForm(instance=chit)

    return render(request, 'edit_chit.html', {'form': form, 'chit': chit})


def handle_week(request, chit_id, week):
    return HttpResponse(f"You clicked Week {week} for Chit ID {chit_id}")

def handle_payment(request, chit_id):
    chit = get_object_or_404(ChitRegistration, id=chit_id)

    if request.method == "POST":
        payment_weeks = int(request.POST.get("payment_weeks", 0))
        amount_per_week = int(request.POST.get("amount_per_week", 0))
        overdue_fees = int(request.POST.get("overdue_fees", 0))
        cash_received = int(request.POST.get("cash_received", 0))
        include_overdue = request.POST.get("include_overdue") == "on"

        total_amount = payment_weeks * amount_per_week
        if include_overdue:
            total_amount += overdue_fees
            
            balance = total_amount - cash_received

        return HttpResponse(f"""
            <h2>Payment Summary</h2>
            <p><strong>Number of Weeks:</strong> {payment_weeks}</p>
            <p><strong>Amount per Week:</strong> {amount_per_week}</p>
            <p><strong>Overdue Fees:</strong> {overdue_fees if include_overdue else 0}</p>
            <p><strong>Total Amount:</strong> {total_amount}</p>
            <p><strong>Cash Received:</strong> {cash_received}</p>
            <p><strong>Balance:</strong> {balance}</p>
            <a href='/view_chits/?chit_Type={chit.chit_Type}&chit_Number={chit.chit_Number}'>
                <button>Back</button>
            </a>
        """)

    return HttpResponse("Invalid Request")

