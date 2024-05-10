from django.contrib import admin
from django.urls import path
from questions_module import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admin_auth/',views.admin_auth,name='admin_auth'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('adminpanel/',views.adminpanel,name='adminpanel'),
    path('add_pattern/',views.add_pattern,name='add_pattern'),
    path('add_normal/',views.add_normal,name='add_normal'),
    path('logout/',views.logout,name='logout'),
    path('question/',views.question,name='question'),
    path('checktext/',views.checktext,name='checktext'),
    path('session_auth/',views.session_auth,name='session_auth'),
]
