from rest_framework import serializers
from .models import Crop
from .models import RuralProducer

class CropSerializer(serializers.ModelSerializer):

    class Meta:

        model = Crop
        fields = '__all__'


class RuralProducerSerializer(serializers.ModelSerializer):

    class Meta:

        model = RuralProducer
        fields = '__all__'


    def validate(self, data):
        if (data['plantingArea'] + data['preservationArea']) > data['totalArea']:
            raise serializers.ValidationError({
	        'totalArea': 'A soma das áreas Agrícultável e Vegetação não pode ultrapassar a área total!'})

        return data
