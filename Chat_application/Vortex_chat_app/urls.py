from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('create_chatroom/', views.create_chatroom, name='create_chatroom'),
    path('create_default_chatroom/', views.create_default_chatroom, name='create_default_chatroom'),
    path('api/chat_room/<str:room_name>/', views.api_get_chat_room, name='api_get_chat_room'),
    path('api/chat_rooms/', views.api_list_chat_rooms, name='api_list_chat_rooms'),
    path('api/create_chatroom/', views.api_create_chatroom, name='api_create_chatroom'),
    path('api/login/', views.api_user_login, name='api_user_login'),
    path('api/logout/', views.api_user_logout, name='api_user_logout'),
    path('api/signup/', views.Signup, name='Signup'),


    
]
