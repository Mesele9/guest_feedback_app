from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit_feedback/<int:hotel_id>/', views.submit_feedback, name='submit_feedback'),
    path('submit_complaint/<int:hotel_id>/', views.submit_complaint, name='submit_complaint'),
    path('submit_maintenance_request/<int:hotel_id>/', views.submit_maintenance_request, name='submit_maintenance_request'),
    path('feedback/<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
    path('complaint/<int:complaint_id>/', views.complaint_detail, name='complaint_detail'),
    path('maintenance_request/<int:maintenance_request_id>/', views.maintenance_request_detail, name='maintenance_request_detail'),
    path('complaint/<int:complaint_id>/update_status/', views.update_complaint_status, name='update_complaint_status'),
    path('maintenance_request/<int:maintenance_request_id>/update_status/', views.update_maintenance_request_status, name='update_maintenance_request_status'),
]
