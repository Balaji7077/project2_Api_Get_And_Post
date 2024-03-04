from django.shortcuts import render
from app.models import *
from app.serializer import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.

class GetProducts(APIView):
    def get(self,request):
        POD=Product.objects.all()
        PJO=productmodelserializers(POD,many=True)
        return Response(PJO.data)

    def post(self,request):
        SJD= productmodelserializers(data=request.data)
        if SJD.is_valid():
            SJD.save()
            return Response({'insert': 'Data inserted successfully'})
        else:
            return Response({'error': 'Data not inserted'})

        