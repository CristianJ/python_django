import re
from inmuebleslist_app.models import Inmueble,Empresa,Comentario
from rest_framework.response import Response
from inmuebleslist_app.api.serializers import InmuebleSerializer,EmpresaSerializer,ComentarioSerializer
#from rest_framework.decorators import api_view
from rest_framework  import status
from rest_framework.views import APIView
from rest_framework import generics,mixins


''' class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Comentario.objects.all()
    serializer_class=ComentarioSerializer
    
    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs) '''

    


class EmpresaListAV(APIView):
    def get(self,request):
        empresa=Empresa.objects.all()
        serializer= EmpresaSerializer(empresa,many=True)
        return Response(serializer.data)
    def post(self,request):
        objecto=EmpresaSerializer(data=request.data)
        if objecto.is_valid():
            objecto.save()
            return Response(objecto.data)
        else:
            return Response(objecto.errors,status=status.HTTP_400_BAD_REQUEST)


class InmuebleListAV(APIView):
    def get(self,request):
        inmuebles=Inmueble.objects.all()
        serializer= InmuebleSerializer(inmuebles,many=True)
        return Response(serializer.data)
    def post(self,request):
        objecto=InmuebleSerializer(data=request.data)
        if objecto.is_valid():
            objecto.save()
            return Response(objecto.data)
        else:
            return Response(objecto.errors,status=status.HTTP_400_BAD_REQUEST)
        
class InmuebleDetalleAV(APIView):
    def get(self, request,id):
        try:
            inmuebles=Inmueble.objects.get(pk=id)
            serializer= InmuebleSerializer(inmuebles)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response({'Error' : "El inmueble no existe"},status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,id):
        
                inmuebles=Inmueble.objects.get(pk=id)
                objecto=InmuebleSerializer(inmuebles,data=request.data)
                if objecto.is_valid():
                    objecto.save()
                    return Response(objecto.data)
                else:
                    return Response(objecto.errors,status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self,request,id):
        try:
            inmuebles=Inmueble.objects.get(pk=id)
            inmuebles.delete()
        except Inmueble.DoesNotExist:
            return Response({"Error":"El inmueble no existe"},status=status.HTTP_404_NOT_FOUND)

                

""" @api_view(['GET','POST'])
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles=Inmueble.objects.all()
        serializer= InmuebleSerializer(inmuebles,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        objecto=InmuebleSerializer(data=request.data)
        if objecto.is_valid():
            objecto.save()
            return Response(objecto.data)
        else:
            return Response(objecto.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def inmueble_detalle(request,id):
    if request.method =='GET':
        try:
            inmuebles=Inmueble.objects.get(pk=id)
            serializer= InmuebleSerializer(inmuebles)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response({'Error' : "El inmueble no existe"},status=status.HTTP_404_NOT_FOUND)
            
    
    if request.method =='PUT':
        inmuebles=Inmueble.objects.get(pk=id)
        objecto=InmuebleSerializer(inmuebles,data=request.data)
        if objecto.is_valid():
            objecto.save()
            return Response(objecto.data)
        else:
            return Response(objecto.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='DELETE':
        try:
            inmuebles=Inmueble.objects.get(pk=id)
            inmuebles.delete()
        except Inmueble.DoesNotExist:
            return Response({"Error":"El inmueble no existe"},status=status.HTTP_404_NOT_FOUND)
        
        
        return Response(status=status.HTTP_204_NO_CONTENT) """