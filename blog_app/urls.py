from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/update/<int:id>/', views.update_post, name='update_post'),
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('post/<int:id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:id>/like/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
