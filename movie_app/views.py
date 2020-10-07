from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from .my_database import DatabaseHelper

class profileView(APIView):

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        #DatabaseHelper.insert2(serializer.data)
        return Response(serializer.data)

    def post(self):
        pass

class profileUpdate(UpdateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

class profileCreate(CreateAPIView):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    #def post(self, request):
        #print("siema")  
        #profile = Profile.objects.all()
        #serializer = ProfileSerializer(profile, many=True)
        #print(request.data)
    #values = Profile.objects(queryset)
    #serializer = ProfileSerializer(queryset, many=True)
    #elo = serializer_class.data
    #print(elo)
    
    #DatabaseHelper.insert2(serializer_class.data)

def cos(request):
    DatabaseHelper.insert()
    #DatabaseHelper.update() 
    return render(request, 'movie_app/cos.html')