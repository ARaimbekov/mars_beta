from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .serializers import CdrSerializer
from .models import Cdr
from django.http import HttpResponse
import logging
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


logger = logging.getLogger(__name__)

class CdrCreate(CreateAPIView):
    serializer_class = CdrSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            call = serializer.save()
            logger.info('SUCCESS')
            logger.info(request.data)
            return Response(status=200)
        else:
            logger.info(serializer.errors)
            logger.info(request.data)
            return Response(serializer.errors, status=404)

class CdrList(generics.ListCreateAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CdrListById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    