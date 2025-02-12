from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #path("", views.index, name="index"),

    path('CreateUserRegister/', views.CreateUserRegister.as_view()),

    path('LoginUser/', views.AppToken.as_view()),

    path('GetUserProfileDetails/', views.GetUserProfileDetails.as_view()),

    path('GetUserProfileDetails/<pk>', views.GetUserProfileDetails.as_view()),
    
    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="dashboard/password_reset_done.html"),
        name="password_reset_complete"),

    path('Car_Reservation/', views.Car_ReservationView.as_view(), name='Car'),
    path('Car_Reservation/<int:pk>', views.Car_ReservationViewDetail.as_view()),
    path('Send_Your_Message/', views.Send_Your_MessageView.as_view(), name='Send_Message'),
    path('Send_Your_Message/<int:pk>', views.Send_Your_MessageViewDetail.as_view()),
    
]