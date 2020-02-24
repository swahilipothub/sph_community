from django.urls import path
# from .views import SignUpView, LoginView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:pk>/change_password/', views.change_password, name='change_password'),
]


# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login'),
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('profile/', UserProfileView.as_view(), name='profile')
# ]