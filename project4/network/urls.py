
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("asset", views.asset, name="asset"),
    path("transaction", views.transaction, name="transaction"),
    path('accountKey', views.accKey, name="accKey"),
    path("profile", views.profile, name="profile"),

    path("buy", views.buy, name="buy"),
    path("sell", views.sell, name="sell"),
    path('api/buysell', views.api_buysell, name="api_buysell"),
]
