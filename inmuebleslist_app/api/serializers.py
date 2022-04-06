from dataclasses import fields
from rest_framework import serializers
from inmuebleslist_app.models import Inmueble,Empresa,Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comentario
        fields="__all__"


class InmuebleSerializer(serializers.ModelSerializer):
    comentarios=ComentarioSerializer(many=True,read_only=True)
    empresa_id= serializers.CharField(source='empresa_id.nombre')
    class Meta:
        model=Inmueble
        #fields="__all__"
        exclude=['id']
        
    
    def validate_descripcion(self,data):
        if len(data)<2:
            raise serializers.ValidationError("La descripcion es muy corta")
        else:
            return data
        
class EmpresaSerializer(serializers.ModelSerializer):
    empresas=InmuebleSerializer(many=True,read_only=True)
    #empresas=serializers.StringRelatedField(many=True)
    class Meta:
        model=Empresa
        fields="__all__"
        
        


