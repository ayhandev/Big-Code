from django.urls import path
from . import views

urlpatterns = [
    path('', views.helo, name='helo'),
    path('big-code/', views.home, name='home'),
    path('run_code/', views.run_code, name='run_code'),
    path('submit-infa/', views.submit_infa, name='submit_infa'),
    path('delete_infa/<int:infa_id>/', views.delete_infa, name='delete_infa'),
    path('doc/', views.doc, name='doc'),

]
