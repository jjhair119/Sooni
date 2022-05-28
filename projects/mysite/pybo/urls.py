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
    path('new/celebrityList/create', views.celebrityList_create, name='celebrityList_create'),
    path('new/celebrityList/delete', views.celebrityList_del, name='celebrityList_del'),
    path('celebrity/new/', views.newcel, name='newcel'),
    path('manager/admin/09uwqeojiqweflkj2308213oi23494', views.manager, name='manager'),
    path('manager/admin/09uwqeojiqweflkj2308213oi23494/cel/del', views.celebrity_del, name='celebrity_del'),
    path('manager/admin/09uwqeojiqweflkj2308213oi23494/cel/cre', views.celebrityList_createM, name='celebrityList_createM'),
]