from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:pk>', views.category, name="category"),
    path('post/<str:pk>', views.post, name="post"),
    path('delete-comment/<str:pk>', views.deleteComment, name="delete-comment"),
]
