
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
<<<<<<< HEAD
    path("register", views.register, name="register"),
    path("asset", views.asset, name="asset"),
    path("transaction", views.transaction, name="transaction"),
    path('accountKey', views.accKey, name="accKey"),
=======
    path("profile/<str:username>", views.profile, name="profile"),
>>>>>>> main
]
