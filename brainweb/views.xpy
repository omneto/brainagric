from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Crop
from .models import RuralProducer
from .serializers import CropSerializer
from .serializers import RuralProducerSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Listar Produtores': 'producers/',
        'Dados por Estado':'producers/?data=state',
        'Dados por Cultura': 'producers/?data=crop',
        'Dados por Uso de Solo':'producers/?data=area',
        'Adicionar': 'producers/create',
        'Atualizar': 'producers/update/id',
        'Excluir': 'producers/delete/id'
    }

    return Response(api_urls)

class CropList(generics.ListCreateAPIView):

    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class RealProducerListApiView(APIView):

    def get(self, request, *args, **kwargs):
        ruralProducers = RuralProducer.objects.filter(id = request.id)
        serializer = RuralProducerSerializer(ruralProducers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class RuralProducerList(generics.ListCreateAPIView):

#    queryset = RuralProducer.objects.all()
#    serializer_class = RuralProducerSerializer
