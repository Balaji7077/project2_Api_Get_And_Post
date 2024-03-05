from django.shortcuts import render
from app.models import *
from app.serializer import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.

class GetProducts(APIView):
    def get(self,request,id):
        POD=Product.objects.all()#orm
        PJO=productmodelserializers(POD,many=True)
        #POD=Product.objects.get(id=id)
        #PJO=productmodelserializers(POD)#json
        return Response(PJO.data)

    def post(self,request,id):
        JDO=request.data
        PDO= productmodelserializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert': 'Data inserted successfully'})
        else:
            return Response({'error': 'Data not inserted'})
    
    def put(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=productmodelserializers(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({"update":"Data is updated"})
        else:
            return Response({'error':'update is not done'})
        
    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=productmodelserializers(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({"update":"Data is updated"})
        else:
            return Response({'error':'update is not done'})
        
    def delete(self,request,id):
        PO=Product.objects.get(id=id)
        PO.delete()
        return Response({"delete":"Data is deleted"})

        