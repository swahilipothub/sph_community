from django.urls import path, include

from sms import views

urlpatterns = [
    path('history/', views.sms_list, name='sms_list'),
    path('fetch/', views.sms_fetch, name='sms_fetch'),
    # path('queue/', views.sms_queue, name='sms_queue'),
    path('balance/', views.user_balance, name='user_balance'),
    path('', views.sms_create, name='sms_create'),
]