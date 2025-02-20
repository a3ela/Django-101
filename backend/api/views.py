from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title'])
        data = ProductSerializer(instance).data
    return Response(data)

@api_view(['POST'])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)
