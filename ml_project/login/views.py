import base64
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ml_system_client import apis


class ImageToBase64View(APIView):
    def post(self, request):
        result = {

        }
        try:
            files = request.FILES.getlist('image')
            if files:
                for x in files:
                    # Read the image file and convert it to base64
                    image_data = x.read()
                    resp = apis.job_execution_req(image_data)
                    result = eval(resp.result)
                    x.seek(0)

            return Response(    result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
