from inmuebleslist_app.models import Inmueble,Empresa,Comentario
from rest_framework.response import Response
from inmuebleslist_app.api.serializers import InmuebleSerializer,EmpresaSerializer,ComentarioSerializer
#from rest_framework.decorators import api_view
from rest_framework  import status
from rest_framework.views import APIView

from rest_framework import generics,mixins


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
