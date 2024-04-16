from django.test import TestCase, Client
from django.urls import reverse
from .models import Hotel, Service, Feedback

class FeedbackFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.hotel = Hotel.objects.create(name="Test Hotel", address="123 Main St")
        self.service = Service.objects.create(hotel=self.hotel, service_name="Room Service", description="Excellent room service.")

    def test_feedback_form_success(self):
        response = self.client.post(reverse('feedback', args=[self.hotel.id, self.service.id]), data={'rating': 5, 'comment': 'Great service!'})
        self.assertEqual(response.status_code, 302)  # Redirects to hotel detail page
        feedback = Feedback.objects.get(hotel=self.hotel, service=self.service)
        self.assertEqual(feedback.rating, 5)
        self.assertEqual(feedback.comment, 'Great service!')

    def test_feedback_form_invalid(self):
        response = self.client.post(reverse('feedback', args=[self.hotel.id, self.service.id]), data={'rating': '', 'comment': ''})
        self.assertEqual(response.status_code, 200)  # Remains on the same page
        self.assertFormError(response, 'form', 'rating', 'This field is required.')
        self.assertFormError(response, 'form', 'comment', 'This field is required.')