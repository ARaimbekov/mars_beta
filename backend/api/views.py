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
        try:
            # Проверка аутентификации пользователя
            if not request.user.is_authenticated:
                logger.info('Unauthorized user attempted to create a CDR.')
                return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            call = serializer.save()
            logger.info('SUCCESS')
            logger.info(request.data)
            return Response(status=status.HTTP_201_CREATED)
        except ValidationError as e:
            logger.error(f'Validation Error: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error during CdrCreate: {str(e)}')
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CdrList(generics.ListCreateAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class CdrListById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    