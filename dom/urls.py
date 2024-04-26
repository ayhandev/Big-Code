from django.urls import path
from . import views

urlpatterns = [
    path('', views.helo, name='helo'),
    path('big-code/', views.home, name='home'),
    path('run_code/', views.run_code, name='run_code'),
    path('doc/', views.doc, name='doc'),

]
