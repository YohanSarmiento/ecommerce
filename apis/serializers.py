# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from store.models import Customer, Product

# Create a model serializer
class CustomerSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = Customer
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = Product
		fields = ('url', 'name', 'price', 'digital') 

