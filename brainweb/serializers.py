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

class RuralProducerListStateSerializer(serializers.ModelSerializer):

    count_state = serializers.IntegerField()

    class Meta:

        model = RuralProducer
        fields = ['state','count_state']

class RuralProducerListCropSerializer(serializers.ModelSerializer):

    crop_list = CropSerializer(many=True, read_only=True)
    crop_name = serializers.CharField(max_length=50)
    count_crop = serializers.IntegerField()

    class Meta:

        model = RuralProducer
        fields = ['crop_list','crop_name','count_crop']

class RuralProducerListAreaSerializer(serializers.ModelSerializer):

    total_area = serializers.DecimalField(max_digits=13,decimal_places=2)

    class Meta:

        model = RuralProducer
        fields = ['id','producerName','total_area']
