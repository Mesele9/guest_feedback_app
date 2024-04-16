from django import forms
from .models import Feedback, Complaint, MaintenanceRequest

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['hotel', 'feedback_text', 'rating']
        widgets = {
            'hotel': forms.HiddenInput(),
            'feedback_text': forms.Textarea(attrs={'rows': 3}),
            'rating': forms.Select(choices=[(i, f'{i} stars') for i in range(1, 6)]),
        }

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['hotel', 'subject', 'description']
        widgets = {
            'hotel': forms.HiddenInput(),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter subject'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['hotel', 'description']
        widgets = {
            'hotel': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
