"""
URL configuration for testBankOfBogota project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/', include('users.urls')),
    path('api/', include('inventory.urls')),
    
    # Reset Password Functionality for Django Admin
    url(
        r'^admin/password_reset/$',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    url(
        r'^admin/password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    url(
        r'^admin/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    url(
        r'^admin/reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),

    url(
        r'^password/change/$',
        auth_views.PasswordChangeView.as_view(),
        name='auth_password_change'
    ),

    url(
        r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='auth_password_change_done'
    ),
    
]
