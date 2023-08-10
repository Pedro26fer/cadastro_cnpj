from rest_framework import serializers
from .utils import validar_cnae, validar_cnpj, editar_cnpj
from .models import Enterprises

class EnterprisesSerialier(serializers.ModelSerializer):
    class Meta:
        model = Enterprises
        fields = '__all__'

 
    def create(self, validated_data):
        cnpj = validated_data.get('cnpj', '')
        cnae = validated_data.get('cnae', '')

        if not validar_cnpj(cnpj):
            raise serializers.ValidationError({"error": "CNPJ inválido"})

        if not validar_cnae(cnae):
            raise serializers.ValidationError({"error": "CNAE inválido"})
        
        validated_data['cnpj'] = editar_cnpj(validated_data['cnpj'])

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        fields_to_update = ['cnae', 'nome_fantasia']
        data_to_update = {}

        for field in fields_to_update:
            if field in validated_data:
                data_to_update[field] = validated_data[field]

        for field in validated_data:
            if field not in fields_to_update:
                raise serializers.ValidationError(
                    f"O campo '{field}' não pode ser atualizado."
                )

        return super().update(instance, data_to_update)