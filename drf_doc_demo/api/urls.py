from api.views import AlphabetView, ConverterView
from django.urls import path

urlpatterns = [
    path("converter/", ConverterView.as_view(), name="converter"),
    path("alphabet/", AlphabetView.as_view(), name="alphabet"),
]
