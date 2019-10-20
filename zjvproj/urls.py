from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_complete, password_reset_confirm, password_reset_done
from django.urls import include, path
from django.views.generic import TemplateView

from zjvapp import views

urlpatterns = [
    # me
    path('', views.index, name='index'),  # `home` in Osborn 1 4.13
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('thing/<slug>', views.thing_detail, name='thing_detail'),
    path('thing/<slug>/edit/', views.thing_edit, name='thing_edit'),

    # Registration Redux: login, logout, register form, register ack
    path('accounts/', include('registration.backends.simple.urls')),

    # pw reset
    path('accounts/password/reset/', password_reset, {'template_name': 'registration/password_reset_form.html'}, name='password_reset'),  # prompt email to send reset link
    path('accounts/password/done/', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),  # ack link sent
    path('accounts/password/reset/<uidb64>/<token>', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),  # input new pw
    path('accounts/password/complete/', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),  # ack new

    # admin
    path('admin/', admin.site.urls),

]
