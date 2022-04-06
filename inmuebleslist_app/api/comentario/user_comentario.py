from rest_framework import generics,mixins
from inmuebleslist_app.api.serializers import ComentarioSerializer
from inmuebleslist_app.models import Comentario
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioComentario(generics.ListAPIView):
    serializer_class=ComentarioSerializer
    filter_backends=[DjangoFilterBackend]
    
    def get_queryset(self):
        #username=self.kwargs['username']
        username=self.request.query_params.get('username',None)
        return Comentario.objects.filter(comentario_user__username=username)