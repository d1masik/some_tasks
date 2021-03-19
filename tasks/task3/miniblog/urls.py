from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, CustomLoginView, CustomLogoutView, CustomRegisterView
from .views import PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register')
]
