from django.urls import path

from .views import contact_email

urlpatterns = [
    path('', contact_email, name='contact' ),
]