from django.urls import path
from core.views import views

app_name = "core"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    
    path("register", views.register_request, name="register")
]
