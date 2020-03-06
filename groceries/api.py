from groceries.models import Groceries
from rest_framework import viewsets,permissions
from .serializers import GroceriesSerializer

class GroceriesViewSet(viewsets.ModelViewSet):
  queryset = Groceries.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = GroceriesSerializer