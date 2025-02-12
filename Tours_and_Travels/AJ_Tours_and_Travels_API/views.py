from django.shortcuts import render, redirect,HttpResponse
#import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from AJ_Tours_and_Travels_API.models import Car_Reservation,Send_Your_Message,RegisterUser
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from .serializers import Car_ReservationSerializer,Send_Your_MessageSerializer,UserRegisterSerializer,GelUserDetailsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils import timezone  
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic import  View
from rest_framework.views import APIView
from django.http import Http404


class CreateUserRegister(CreateAPIView):
    model = RegisterUser
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response([serializer.data], status=status.HTTP_200_OK)
            return Response({
                "CreateUser": serializer.data,
                "message": "register successfully!",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        # print(serializer.errors)
        try:
            return Response({'Error': serializer.errors['email'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            return Response({'Error': serializer.errors['password2'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            return Response({'Error': serializer.errors['mob_no'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        return Response({'Error': "Something Went Wrong !"}, status=status.HTTP_400_BAD_REQUEST)


class AppToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            password = serializer.validated_data['password']

            token, created = Token.objects.get_or_create(user=user)

            registerUser = RegisterUser.objects.filter(userId=token.user.id, email=token.user).values('userId','id',
                                                                                                      'email',
                                                                                                      'first_name',
                                                                                                      'last_name',
                                                                                                      'mob_no')
            # print(registerUser[0])
            context = {"token": token.key, "userId": registerUser[0]['userId'], "email": registerUser[0]['email'],
                       "first_name": registerUser[0]['first_name'], "last_name": registerUser[0]['last_name'],
                       "mob_no": registerUser[0]['mob_no'], "id": registerUser[0]['id'],
                       }

            #return Response([context], status=status.HTTP_200_OK)
            return Response({
                "Login": context,
                "message": "Login successfully!",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        try:
            return Response({'Error': serializer.errors['non_field_errors'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error': "Please Provide Username and Password"}, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse({'message':'ok'}, status=status.HTTP_400_BAD_REQUEST)

class GetUserProfileDetails(APIView):
    # parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            pk = pk
            return RegisterUser.objects.get(pk=pk)
        except RegisterUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        data = RegisterUser.objects.filter(userId=request.user.id)
        serializer = GelUserDetailsSerializer(data, many=True)
        if data:
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"something went wrong!"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        id = pk
        instance = self.get_object(id)

        serializer = GelUserDetailsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                "Userprofile": serializer.data,
                "message": "updated successfully!",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Car_ReservationView(APIView): 
      #permission_classes = (IsAuthenticated,)

      def get(self, request, format=None):

          snippets = Car_Reservation.objects.all()
          serializer = Car_ReservationSerializer(snippets, many=True)
          return Response(serializer.data)

      def post(self, request, format=None):
          serializer = Car_ReservationSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class Car_ReservationViewDetail(APIView):
#      permission_classes = (IsAuthenticated,)

      def get_object(self, pk):
          try:
              return Car_Reservation.objects.get(pk=pk)
          except Snippet.DoesNotExist:
              raise Http404

      def get(self, request, pk, format=None):
          snippet = self.get_object(pk)
          serializer = Car_ReservationSerializer(snippet)
          return Response(serializer.data)

      def put(self, request, pk, format=None):
          snippet = self.get_object(pk)
          serializer = Car_ReservationSerializer(snippet, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, pk, format=None):
         snippet = self.get_object(pk)
         snippet.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


class Send_Your_MessageView(APIView): 
      permission_classes = (IsAuthenticated,)

      def get(self, request, format=None):

          snippets = Send_Your_Message.objects.all()
          serializer = Send_Your_MessageSerializer(snippets, many=True)
          return Response(serializer.data)

      def post(self, request, format=None):
          serializer = Send_Your_MessageSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class Send_Your_MessageViewDetail(APIView):
#      permission_classes = (IsAuthenticated,)

      def get_object(self, pk):
        try:
             return Send_Your_Message.objects.get(pk=pk)
        except Snippet.DoesNotExist:
              raise Http404

      def get(self, request, pk, format=None):
          snippet = self.get_object(pk)
          serializer = Send_Your_MessageSerializer(snippet)
          return Response(serializer.data)

      def put(self, request, pk, format=None):
          snippet = self.get_object(pk)
          serializer = Send_Your_MessageSerializer(snippet, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, pk, format=None):
         snippet = self.get_object(pk)
         snippet.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)