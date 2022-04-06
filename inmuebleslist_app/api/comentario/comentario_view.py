
from inmuebleslist_app.utils.pagination import EdificacionPagination,EdificacionPaginationOffset
from inmuebleslist_app.models import Comentario
from rest_framework.response import Response
from inmuebleslist_app.api.serializers import ComentarioSerializer
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from inmuebleslist_app.utils.throttling import ComentarioCreateThrottle,ComentarioListThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Comentario.objects.all()
    #filter_backends=[DjangoFilterBackend]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['comentario_user__username','active','texto']
    #throttle_classes=[ComentarioListThrottle]
    #permission_classes=[IsAuthenticated]
    pagination_class=EdificacionPaginationOffset #EdificacionPagination
    serializer_class=ComentarioSerializer
    
    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)