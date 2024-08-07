from django.urls import path,include
from .views import*

urlpatterns=[
    path('login/',userLogin,name="login"),
    path('register/',register,name="register"),
    path('logout/',userLogout,name="logout"),
    path('iletisim/',iletisim,name="iletisim"),
    path('basvur/',basvur,name="basvur"),
]