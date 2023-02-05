from rest_framework import serializers

from base.models import UserNew, Product, Documents, CreditTest


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNew
        fields = '__all__'


class CreditTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditTest
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
