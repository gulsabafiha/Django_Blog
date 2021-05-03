from django.urls import path
from .views import HomeView,ArticleView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,AddCommnetView


urlpatterns = [
    
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>/',ArticleView.as_view(),name='article_detail'),
    path('add_post/',AddPostView.as_view(), name="add_post"),
    path('add_category/',AddCategoryView.as_view(), name="add_category"),
    path('article_detail/edit/<int:pk>/',UpdatePostView.as_view(),name='update_post'),
    path('article_detail/<int:pk>/remove/',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category-list'),
    path('article/<str:pk>/add_comment',AddCommnetView.as_view(),name='add_comment')

 ]
 