from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from random import choice

from account.api.serializers import RegistrationSerializer, GetListSerializer
from account.models import Account

@api_view(['POST'])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
		else:
			data = serializer.errors
		return Response(data)

@api_view(['GET'])
def list_registration_view(request):
	if request.method == 'GET':
		account = Account.objects.all()
		account_serializer = GetListSerializer(account, many=True)
		return JsonResponse(account_serializer.data, safe=False)

@api_view(['GET'])
def winner_registration_view(request):
	if request.method == 'GET':
		account = Account.objects.values_list('pk', flat=True)
		random_pk = choice(account)
		random_obj = Account.objects.get(pk=random_pk)
		account_serializer = GetListSerializer(random_obj)
		return JsonResponse(account_serializer.data) 

@api_view(['GET', 'DELETE'])
def detail_registration_view(request, pk):
	try:
		account = Account.objects.get(pk=pk)
	except Account.DoesNotExist:
		return JsonResponse({'message': 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		account_serializer = GetListSerializer(account)
		return JsonResponse(account_serializer.data) 

	elif request.method == 'DELETE':
		account.delete()
		return JsonResponse({'message': 'El usuario se a eliminado con exito!'}, status=status.HTTP_204_NO_CONTENT)