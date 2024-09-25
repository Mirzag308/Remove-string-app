from django.urls import path
from . import views  # Correct import from the current module

urlpatterns = [
    path('', views.remove_vowels, name='remove_vowels'),
]

# remove_vowels_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.remove_vowels, name='remove_vowels'),
    # path('test/', views.test_view, name='test_view'),
]
