from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Documents, Product, CreditTest, UserNew, History, StatusCredit
from base.serializer import DocumentsSerializer, ProductSerializer, CreditTestSerializer, AccountSerializer, \
    HistorySerializer, StatusCreditSerializer


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


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()

    serializer_class = HistorySerializer


class StatusCreditViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusCredit.objects.prefetch_related(Prefetch('name', queryset=CreditTest.objects.all()))
    serializer_class = StatusCreditSerializer
