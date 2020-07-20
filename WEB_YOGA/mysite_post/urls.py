from . import views
from django.urls import path

urlpatterns = [

    # path('signup/', views.signup, name='signup'),
    path('post_create/', views.post_create, name='post_create'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')

]