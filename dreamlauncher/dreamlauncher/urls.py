from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import core.views as cv 
urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", cv.homepage, name="homepage"),
    
    path("register", cv.register_request, name="register")
]
    



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 



    
