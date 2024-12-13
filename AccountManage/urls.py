from django.urls import path
from . import views

urlpatterns = [
    path('Board/', views.Move_Board, name='move_board'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),  # 홈 페이지
]