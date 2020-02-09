"""schoolmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from schooladmin import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('home/', views.home_view, name='home'),
    path('student/', views.students_data, name='homedata'),

    path('studentcreate/', views.students_create, name='create1'),
    path('studentupdate/<int:id>', views.students_update, name='update1'),
    path('studentdetail/<int:id>', views.students_detail, name='detail1'),
    path('studentdelete/<int:id>', views.students_delete, name='delete'),
    path('homeedit/', views.home_edit, name='home_edit'),

    path('help/', views.help),
    path('calender/', views.calender),
    path('about/', views.about),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('/accounts/login/', views.login, name="login"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    #Password Reset Urls
    # path('password_reset/', auth_views.password_reset, name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/?p<uidb64>/<token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
