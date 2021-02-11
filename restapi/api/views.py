from django.shortcuts import render
from .serializers import serializers 
from rest_framework.authtoken.models import Token

# Create your views here.

class register(APIView):

    def post(self,request,format=None):
        serializers=UserRegister(data=request.data) 
        data={}
        if serializers.is_valid():
            account=serializers.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializers.error
        return Response(data)
        

