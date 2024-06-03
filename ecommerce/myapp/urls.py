from django.urls import path
from .views import (update_todo, post_todo, delete_todo,
                     ListView, mark_complete, completed_task, signup, login_page, logout_view)




urlpatterns = [
    path('index/', ListView.as_view(), name='index' ),
    path('post/', post_todo, name='post' ),
    path('update/<int:pk>/', update_todo, name='update'),
    path('delete/<int:pk>/', delete_todo, name='delete'),
    path('complete/<int:pk>/', mark_complete, name='complete'),
    path('completedtask/', completed_task, name='completed_task'),
    path('signup/', signup, name="signup"),
    path('login/', login_page, name="login"),
    path('logout/', logout_view, name="logout"),


   
]
