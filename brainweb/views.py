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
        'Listar Produtores': 'producers/ [GET]',
        'Adicionar Produtor': 'producers/ [POST]',
        'Atualizar Produtor': 'producers/<id> [PUT]',
        'Excluir Produtor': 'producers/<id> [DELETE]',
        'Listar Produtores por Estado':'producers/list/state',
        'Listar Produtores por Cultura': 'producers/list/crop',
        'Listar Produtores por Uso de Solo':'producers/list/area'
    }

    return Response(api_urls)

class CropList(generics.ListCreateAPIView):

    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class RuralProducerListApiView(APIView):

    def get(self, request, *args, **kwargs):
        ruralProducers = RuralProducer.objects.all()
        serializer = RuralProducerSerializer(ruralProducers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RuralProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RuralProducerDetailApiView(APIView):

    def get_object(self, rural_producer_id):
        try:
            return RuralProducer.objects.get(id=rural_producer_id)
        except RuralProducer.DoesNotExist:
            return None

    def get(self, request, rural_producer_id, *args, **kwargs):

        ruralProducer = self.get_object(rural_producer_id)
        if not ruralProducer:
            return Response(
                {"res": "Rural Producer with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RuralProducerSerializer(ruralProducer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, rural_producer_id, *args, **kwargs):

        ruralProducer = self.get_object(rural_producer_id)
        if not ruralProducer:
            return Response(
                {"res": "Rural Producer with this id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = RuralProducerSerializer(instance = ruralProducer, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rural_producer_id, *args, **kwargs):

        ruralProducer = self.get_object(rural_producer_id)
        if not ruralProducer:
            return Response(
                {"res": "Rural Producer with this id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        ruralProducer.delete()
        return Response(
            {"res": "Rural Producer deleted!"},
            status=status.HTTP_200_OK
        )


class RuralProducerListByState(generics.ListAPIView):

#    queryset = RuralProducer.objects.all()
#    serializer_class = RuralProducerSerializer
    def get_queryset(self):
          return RuralProducer.objects.values('state').annotate(count_state=Count('state')).order_by()
