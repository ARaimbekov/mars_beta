from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .serializers import CdrSerializer
from .models import Cdr
from django.http import HttpResponse


# create and save CDR
class CdrCreate(CreateAPIView):
    serializer_class = CdrSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            call = serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=404)


# list via get/ CDRs
class CdrList(generics.ListCreateAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer


# list via get/pk CDRs by id 
class CdrListById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer

    