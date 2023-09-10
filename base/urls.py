from django.urls import path
from .views import TaskList
from .views import TaskDetail
from .views import TaskCreate
from .views import TaskUpdate
from .views import TaskDelete
from .views import CustomLoginView
from .views import ProfileView
from django.contrib.auth.views import LogoutView
from .views import RegisterPage

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    path('profile/', ProfileView.as_view(), name='profile')
]
