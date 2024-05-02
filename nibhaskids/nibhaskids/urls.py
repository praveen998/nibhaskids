from django.contrib import admin
from django.urls import path
from questions_module import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admin_auth/',views.admin_auth,name='admin_auth'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('adminpanel/',views.adminpanel,name='adminpanel'),
    path('sendimage/',views.sendimage,name='sendimage'),
    path('add_pattern/',views.add_pattern,name='add_pattern'),
    path('add_normal/',views.add_normal,name='add_normal'),
]
