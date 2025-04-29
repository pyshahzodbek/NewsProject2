from  django.urls import  path
from  .views import  user_login,dashboard_views
from django.contrib.auth.views import LogoutView,LoginView,PasswordChangeView,PasswordChangeDoneView,\
    PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns=[
    # path('login/',user_login,name='login'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/',PasswordChangeView.as_view(),name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password-reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password-reset-done',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_conform'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('profile/',dashboard_views,name='user_profile'),
]