from django.urls import path

from app.views import article_list_view,article_create_view,article_update_view,article_detail_view,article_delete_view,change_password



app_name= 'app'
urlpatterns = [
    path('list/', article_list_view, name='list'),
    path('create/', article_create_view, name='article-create-view'),
    path('update/<int:id>/', article_update_view, name='article-update-view'),
    path('detail/<int:id>/', article_detail_view, name='article-detail-view'),
    path('delete/<int:id>/', article_delete_view, name='article-delete-view'),
    path('changepassword/', change_password, name='change_password'),
    
]

