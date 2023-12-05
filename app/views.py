from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.seriallizers import *
from rest_framework.response import Response

class ProductData(ViewSet):
    def list(self,request):
        PLO=Product.objects.all()
        JSD=ProductModelSerializer(PLO,many=True)
        return Response(JSD.data)
    
    def retrieve(self,request,pk):
        PRO=Product.objects.get(Pid=pk)
        JSDO=ProductModelSerializer(PRO)
        return Response(JSDO.data)
    
    def create(self,request):
        JSD=request.data
        PDO=ProductModelSerializer(data=JSD)
        if PDO.is_valid():
            PDO.save()
            return Response({"message":"Data Inserted Successfully"})
        else:
            return Response({"message":"Data insertion is failed"})
        
    def update(self,request,pk):
        JSD=request.data
        PO=Product.objects.get(Pid=pk)
        PDO=ProductModelSerializer(PO,data=JSD)
        if PDO.is_valid():
            PDO.save()
            return Response({"message":"Data Updated Successfully"})
        else:
            return Response({"message":"Updation is failed"})
        
    def partial_update(self,request,pk):
        JSD=request.data
        PO=Product.objects.get(Pid=pk)
        PDO=ProductModelSerializer(PO,data=JSD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({"message":"Data Updated Partially"})
        else:
            return Response({"message":" Partial Updation is failed"})
        
    def destroy(self,request,pk):
        PO=Product.objects.get(Pid=pk)
        PO.delete()
        return Response({"message":"Data Deleted Successfully"})
    

