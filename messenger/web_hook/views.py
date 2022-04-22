import logging

from rest_framework.views import APIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class WebHookView(APIView):
    permission_classes = []

    def post(self, request, format=None):
        logger.info("WebHook request")
        logger.info('body: %s', request.data)
        return Response() 

class AuthView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        logger.info("ACL request")
        logger.info('params: %s', request.GET)
        logger.info('body: %s', request.data)
        return Response() 

    def post(self, request, format=None):
        logger.info("Auth request")
        logger.info('body: %s', request.data)
        return Response() 
