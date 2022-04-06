
from inmuebleslist_app.models import Comentario
from rest_framework.response import Response
from inmuebleslist_app.api.serializers import ComentarioSerializer
from rest_framework import generics,mixins


class ComentarioDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Comentario.objects.all()
    serializer_class=ComentarioSerializer
    
    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)