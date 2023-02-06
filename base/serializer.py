from rest_framework import serializers

from base.models import UserNew, Product, Documents, CreditTest, StatusCredit, History


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNew
        fields = ['id', 'username', 'first_name', 'last_name', 'sur_name', 'email',
                  'avatar', 'salary', 'date_of_birth', 'mobil_phone_number', 'city_phone_number',
                  'sex', 'type_document', 'number_passport', 'identification_number', 'date_of_issue',
                  'validity', 'issuing_authority', 'city', 'type_street', 'street', 'home',
                  'frame', 'apartment', 'index', 'is_the_registration_address_the_same_as_the_residence_address',
                  'privacy_police', 'personal_data', 'resident_rb', 'resident_usa']
        depth = 1


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


class HistorySerializer(serializers.ModelSerializer):
    credit = CreditTestSerializer(read_only=True)
    user = AccountSerializer(read_only=True)

    class Meta:
        model = History
        fields = ['user', 'product', 'shop', 'price', 'credit', 'date', 'status']
        depth = 1


class StatusCreditSerializer(serializers.ModelSerializer):
    name = CreditTestSerializer(read_only=True)

    class Meta:
        model = StatusCredit
        fields = ['name', 'text']
        depth = 1
