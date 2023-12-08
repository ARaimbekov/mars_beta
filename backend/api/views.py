from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import CdrSerializer
from .models import Cdr
from django.http import HttpResponse

class CdrCreateView(CreateAPIView):
    serializer_class = CdrSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            call = serializer.save()
            return Response(call.to_dict(), status=200)
        else:
            return Response(serializer.errors, status=404)
