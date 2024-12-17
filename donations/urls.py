from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('donate/', views.Donate.as_view(), name='donate'),
    path('donate/<int:cat_id>/', views.Donate.as_view(), name='donate_with_cat'),
    path('success/<str:donation_number>/', views.successMsg, name="success"),
    path(
        "create_payment_intent/",
        views.create_payment_intent,
        name="create_payment_intent",
    ),
    path('cache_donation_data/', views.cache_donation_data, name='cache_donation_data'),
    path('wh/', webhook, name="webhook")
]