from django.urls import path

from randoms import views

urlpatterns = [
    path('uuids/', views.RandomView.as_view()),
]