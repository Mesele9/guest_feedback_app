from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Feedback, Complaint, MaintenanceRequest, Hotel
from .forms import FeedbackForm, ComplaintForm, MaintenanceRequestForm

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'home.html', {'hotels': hotels})


def dashboard(request):
    # Count the number of feedbacks, complaints, and maintenance requests
    feedbacks_count = Feedback.objects.count()
    complaints_count = Complaint.objects.count()
    maintenance_requests_count = MaintenanceRequest.objects.count()

    # Retrieve all feedbacks, complaints, and maintenance requests
    feedbacks = Feedback.objects.all()
    complaints = Complaint.objects.all()
    maintenance_requests = MaintenanceRequest.objects.all()

    context = {
        'feedbacks_count': feedbacks_count,
        'complaints_count': complaints_count,
        'maintenance_requests_count': maintenance_requests_count,
        'feedbacks': feedbacks,
        'complaints': complaints,
        'maintenance_requests': maintenance_requests,
    }
    return render(request, 'dashboard.html', context)


def submit_feedback(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.hotel = hotel
            feedback.user = request.user
            feedback.save()
            return redirect('home')
    else:
        form = FeedbackForm()

    return render(request, 'submit_feedback.html', {'form': form, 'hotel': hotel})


def submit_complaint(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.hotel = hotel  # Set the hotel field
            complaint.user = request.user
            complaint.save()
            return redirect('home')
    else:
        form = ComplaintForm()

    return render(request, 'submit_complaint.html', {'form': form, 'hotel': hotel})


def submit_maintenance_request(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save(commit=False)
            maintenance_request.hotel = hotel  # Set the hotel field
            maintenance_request.user = request.user
            maintenance_request.save()
            return redirect('home')
    else:
        form = MaintenanceRequestForm()

    return render(request, 'submit_maintenance_request.html', {'form': form, 'hotel': hotel})


def feedback_detail(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    return render(request, 'feedback_detail.html', {'feedback': feedback})

def complaint_detail(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    return render(request, 'complaint_detail.html', {'complaint': complaint})

def maintenance_request_detail(request, maintenance_request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, id=maintenance_request_id)
    return render(request, 'maintenance_request_detail.html', {'maintenance_request': maintenance_request})

@require_POST
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    new_status = request.POST.get('new_status')
    if new_status in ['fixed', 'done']:
        complaint.status = new_status
        complaint.save()
    return redirect('dashboard')

@require_POST
def update_maintenance_request_status(request, maintenance_request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, id=maintenance_request_id)
    new_status = request.POST.get('new_status')
    if new_status in ['fixed', 'done']:
        maintenance_request.status = new_status
        maintenance_request.save()
    return redirect('dashboard')
