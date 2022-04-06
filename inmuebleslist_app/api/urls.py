
from django.urls import path,include
#from inmuebles.inmuebleslist_app.api.views import ComentarioDetail, ComentarioList
#from inmuebleslist_app.api.views import inmueble_list,inmueble_detalle
from inmuebleslist_app.api.views import InmuebleListAV,InmuebleDetalleAV,EmpresaListAV
from inmuebleslist_app.api.comentario.comentario_view import ComentarioList
from inmuebleslist_app.api.comentario.comentario_detail_view import ComentarioDetail
from inmuebleslist_app.api.empresa.empresa_view import EmpresaViewSet
from inmuebleslist_app.api.comentario.user_comentario import UsuarioComentario
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('empresa',EmpresaViewSet,basename='empresa')

urlpatterns=[
    
    
    path('',include(router.urls)),
    
    path('list/',InmuebleListAV.as_view(),name="inmueble-list"),
    path('<id>',InmuebleDetalleAV.as_view(),name="inmueble-detalle"),
    #path('empresa/',EmpresaListAV.as_view(),name="empresa"),
    
    
    path('comentarios/',ComentarioList.as_view(),name="comentario-list"),
    #path('comentarios/',ComentarioList.as_view(),name="comentario-list"),
    path('comentario/<pk>',ComentarioDetail.as_view(),name="comentario-detail"),
    #path('usercomentarios/<str:username>/',UsuarioComentario.as_view(),name='usuario-comentario')
    path('usercomentarios/',UsuarioComentario.as_view(),name='usuario-comentario')
]