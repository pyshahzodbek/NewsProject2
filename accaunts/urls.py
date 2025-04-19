from  django.urls import  path
from  .views import  user_login,dashboard_views
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns=[
    # path('login/',user_login,name='login'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out'), name='logout'),
    path('profile/',dashboard_views,name='user_profile'),
]