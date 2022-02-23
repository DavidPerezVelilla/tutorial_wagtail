from django.urls import path
from .import views

urlpatterns = [
    path('detalle/<int:pk>',views.NoticiaDetail.as_view())
]