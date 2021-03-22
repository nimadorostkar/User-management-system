from django.urls import path
from . import views

urlpatterns = [
    path('/<int:User.id>/', views.dashboard, name='dashboard'),
]


#/<int:id>/
