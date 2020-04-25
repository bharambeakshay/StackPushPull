from django.urls import path
from . import views


urlpatterns = [
    path('',views.account_home_view,name="account-home"),
    path('user-profile/',views.user_profile_view,name="user-profile"),

    path('login/',views.login_view,name="login"),
    path('login-check/',views.login_handle,name="login-check"),
    path('signup/',views.signup_view,name="signup"),
    path('logout/',views.logout_view,name="logout"),
]