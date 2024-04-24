from django.contrib import admin
from django.urls import path
from questions_module import views
from django.views.decorators.csrf import csrf_protect

urlpatterns = [
     path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admin_auth/',views.admin_auth,name='admin_auth'),
    path('admin_login/',views.admin_login,name='admin_login'),
]
