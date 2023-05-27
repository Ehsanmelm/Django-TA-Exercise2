from django.shortcuts import render , get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from  .models import User 
from .serializers import Create_User_Serializer  , Show_User_Info_Serializer

# Create your views here.

class CreateUser_view(APIView):

    
    def post(self,request):
        serializer = Create_User_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token , created = Token.objects.get_or_create(user=user)
        user_info = Create_User_Serializer(user).data

        return Response(
            {
                "first_name": user_info["first_name"],
                "last_name": user_info["last_name"],
                "phone": user_info["phone"],
                "token" : token.key
            }
        )
    

class LoginUser_view(APIView):

    def post(self,request ):

        data = request.data
        user = authenticate(phone = data["phone"] , password = data["password"])
        token = get_object_or_404(Token , user =user)
        serializer = Create_User_Serializer(user)
        return Response(
            {
                "first name" : serializer.data["first_name"],
                "last name" : serializer.data["last_name"],
                "phone":serializer.data["phone"],
                "token": token.key
            }
        )


class show_info_Veiw(APIView):
    def get(Self,request,token):
        token = get_object_or_404(Token ,key = token )
        serializer = Show_User_Info_Serializer(token.user)

        return Response(serializer.data)
    