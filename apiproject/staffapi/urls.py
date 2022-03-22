from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from staffapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/getall', views.StaffList.as_view()),
    path('api/getall/<int:pk>/', views.StaffDetails.as_view()),
    path('api/login', views.login),
    path('api/display-staff', views.display_staff),
]

urlpatterns = format_suffix_patterns(urlpatterns)
