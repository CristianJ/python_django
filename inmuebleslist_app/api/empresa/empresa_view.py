
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from inmuebleslist_app.models import Empresa
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from inmuebleslist_app.api.serializers import EmpresaSerializer
from rest_framework  import status
from inmuebleslist_app.permissions.permissions import AdminOrReadOnly


class EmpresaViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Empresa.objects.all()
    serializer_class=EmpresaSerializer
    ''' def list(self,request):
        queryset=Empresa.objects.all()
        serializer=EmpresaSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        queryset=Empresa.objects.all()
        edificacionlist=get_object_or_404(queryset,pk=pk)
        serializer=EmpresaSerializer(edificacionlist)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({"error":"Empresa no encontrada"} ,status=status.HTTP_404_NOT_FOUND)

        serializer=EmpresaSerializer(empresa,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
            
    def destroy(self,request,pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error':"Empresa no encontrada"},status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    ''' 