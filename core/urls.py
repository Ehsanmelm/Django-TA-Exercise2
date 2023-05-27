from . import views
from django.urls import path

urlpatterns = [
    path('create-user' , views.CreateUser_view.as_view() , name='create_userd'),
    path('Login-user' , views.LoginUser_view.as_view() , name='login_userd'),
    path('show_info/<token>' , views.show_info_Veiw.as_view() , name='show_info'),
]