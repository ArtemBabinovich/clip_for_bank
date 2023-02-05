from django.shortcuts import render
from rest_framework import viewsets

from base.models import Documents, Product, CreditTest, UserNew
from base.serializer import DocumentsSerializer, ProductSerializer, CreditTestSerializer, AccountSerializer


# Create your views here.


class DocumentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreditTestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CreditTest.objects.all()
    serializer_class = CreditTestSerializer


class UserNewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserNew.objects.all()
    serializer_class = AccountSerializer
