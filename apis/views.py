# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import CustomerSerializer, ProductSerializer
from store.models import Customer, Product

# create a viewset


class CustomerViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Customer.objects.all()

	# specify serializer to be used
	serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Product.objects.all()

	# specify serializer to be used
	serializer_class = ProductSerializer