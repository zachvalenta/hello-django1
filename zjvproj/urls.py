from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from zjvapp import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('admin/', admin.site.urls),
]
