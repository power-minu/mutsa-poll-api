from django.shortcuts import render
from .api.serializers import PollSerializer, PollRequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Poll

@api_view(['GET', 'POST'])
def pollList(request):
    match request.method:
        case 'GET':
            order = request.query_params.get('order')
            
            if order == 'oldest':
                poll = Poll.objects.all().order_by('createdAt')
            elif order == 'agree':
                poll = Poll.objects.all().order_by('-agree')
            elif order == 'disagree':
                poll = Poll.objects.all().order_by('-disagree')
            elif order == 'latest':
                poll = Poll.objects.all().order_by('-createdAt')
            else:
                poll = Poll.objects.all().order_by('-createdAt')
            
            serializer = PollSerializer(poll, many=True)
        
            return Response(serializer.data)
        case 'POST':
            serializer = PollSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def getOne(request, id):
    match request.method:
        case 'GET':
            poll = Poll.objects.get(id=id)
            serializer = PollSerializer(poll)
            return Response(serializer.data)
        case 'PUT':
            poll = Poll.objects.get(id=id)
            serializer = PollSerializer(poll, data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        case 'DELETE':
            Poll.objects.get(id=id).delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
            
@api_view(['POST'])
def voteAgree(request, id):
    poll = Poll.objects.get(id=id)
    poll.agree += 1
    poll.save()
    serializer = PollSerializer(poll)
    return Response(serializer.data)

@api_view(['POST'])
def voteDisagree(request, id):
    poll = Poll.objects.get(id=id)
    poll.disagree += 1
    poll.save()
    serializer = PollSerializer(poll)
    return Response(serializer.data)