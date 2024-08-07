from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.loader, name='loader'),
    path('home/', views.helo, name='helo'),
    path('big-code/', views.home, name='home'),
    path('run_code/', views.run_code, name='run_code'),
    path('submit-infa/', views.submit_infa, name='submit_infa'),
    path('delete_infa/<int:infa_id>/', views.delete_infa, name='delete_infa'),
    path('doc/', views.doc, name='doc'),
    path('Code_submit/', views.publish_code_submit, name='public_code_submit'),
    path('public/', views.public_view, name='public'),
    path('public_list/', views.public_list, name='public_list'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('add_like/<int:post_id>/', views.add_like, name='add_like'),
    path('messenger/', views.messenger, name='messenger'),
    

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
