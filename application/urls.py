from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'application'
urlpatterns = [
    path('upload', login_required(views.UploadView.as_view(), login_url = '/admin/login/'), name = 'upload'),
    path('success', views.SuccessView.as_view(), name = 'success'),
    path('', views.IndexView.as_view(), name = 'index'),
]
