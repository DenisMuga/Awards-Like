from django.urls import path
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('',views.home, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<username>/profile/', views.user_profile, name='userprofile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('project/<post>/', views.project, name='project'),
    
    
]