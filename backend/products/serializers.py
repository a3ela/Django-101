from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]
# change the name ofthe reponse to discount from get discount
    def get_discount(self, obj):
        return obj.get_discount()