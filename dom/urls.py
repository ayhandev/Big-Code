from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('run_code/', views.run_code, name='run_code'),
    path('doc/', views.doc, name='doc'),

]
