from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [ 'brand', 'model', 'price', 'is_bought', 'buy_time', 'buyer_id'] 
