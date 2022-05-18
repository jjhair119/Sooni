from django.urls import path

from . import views

#pybo - app url
app_name = 'pybo'

urlpatterns = [
    path('', views.celebrities, name='celebrities'),
    path('<str:celebrity_name>', views.post, name='post'),
    path('<str:celebrity_name>/<int:post_id>', views.detail, name='detail'),
    path('<str:celebrity_name>/<int:post_id>/comment/create/', views.comment_create, name='comment_create'),
    path('<str:celebrity_name>/newpost', views.newpost, name='newpost'),
    path('<str:celebrity_name>/newpost/create', views.post_create, name='post_create'),
    path('new/celebrity/create', views.celebrity_create, name='celebrity_create'),
    path('celebrity/new/', views.newcel, name='newcel'),
]