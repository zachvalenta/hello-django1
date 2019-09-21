from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from zjvapp import views

urlpatterns = [
    path('', views.index, name='index'),  # `home` in Osborn 1 4.13
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('thing/<slug>', views.thing_detail, name='thing_detail'),
    path('thing/<slug>/edit/', views.thing_edit, name='thing_edit'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
