"""p_gastro URL Configuration
"""
from django.contrib import admin
from django.urls import path
from gastro_app.views import (
    homepage, reservations, contact, user_registration,
    user_login, reservation_list, user_logout,
    update_reservation, delete_reservation
)
from gastro_app import views
from django.contrib.auth.decorators import login_required

"""p_gastro URL configuration"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('reservation_list/', views.reservation_list, name='reservation_list'),
    path('reservation/<int:pk>/update/',
         views.update_reservation,
         name='update_reservation'),
    path('reservation/<int:pk>/delete/',
         views.delete_reservation,
         name='delete_reservation'),
    path('thanksres/', views.thanksres_view, name='thanksres'),
    path('thanks/', views.thanks_view, name='thanks'),
]
