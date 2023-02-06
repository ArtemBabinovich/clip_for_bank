from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
SEX_CHOICES = [
    ['man', 'man'],
    ['woman', 'woman'],
]

TYPE_DOCUMENT = [
    ['паспорт', 'паспорт'],
    ['вид на жительство', 'вид на жительство'],
]

TYPE_STREET = [
    ['пр-т.', 'пр-т.'],
    ['ул.', 'ул.'],
    ['бульвар', 'бульвар'],
    ['переулок', 'переулок'],
]

ADRESS_REGISTR = [
    ['да', 'да'],
    ['нет', 'нет'],
]


class UserNew(AbstractUser):
    sur_name = models.CharField(verbose_name='Отчество', max_length=100, blank=True, null=True)
    avatar = models.FileField(verbose_name='фотография', upload_to='avatar_user/', blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True, verbose_name='Зарплата')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    mobil_phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    city_phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Городской телефон')
    sex = models.CharField(max_length=5, choices=SEX_CHOICES, null=True, blank=True, verbose_name='Пол')
    type_document = models.CharField(max_length=25, choices=TYPE_DOCUMENT, null=True, blank=True, verbose_name='Тип документа')
    number_passport = models.CharField(max_length=25, null=True, blank=True, verbose_name='Серия и номер паспорта')
    identification_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Индетификационный номер')
    date_of_issue = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    validity = models.DateField(null=True, blank=True, verbose_name='Срок действия')
    issuing_authority = models.CharField(max_length=100, null=True, blank=True, verbose_name='Орган выдавший документ')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Населенный пункт')
    type_street = models.CharField(max_length=20, choices=TYPE_STREET, null=True, blank=True, verbose_name='Тип улицы')
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name='Улица')
    home = models.CharField(max_length=20, null=True, blank=True, verbose_name='Дом')
    frame = models.CharField(max_length=20, null=True, blank=True, verbose_name='Строение/корпус')
    apartment = models.CharField(max_length=20, null=True, blank=True, verbose_name='Квартира')
    index = models.CharField(max_length=20, null=True, blank=True, verbose_name='Индекс')
    is_the_registration_address_the_same_as_the_residence_address = models.CharField(max_length=3, choices=ADRESS_REGISTR, null=True, blank=True, verbose_name='Адрес регистрации совпадает с адресом проживания?')
    privacy_police = models.BooleanField(default=False, verbose_name='Я согласен(а) с Политикой конфиденциальности')
    personal_data = models.BooleanField(default=False, verbose_name='Я даю Согласие на хранение обработку персональных данных')
    resident_rb = models.BooleanField(default=False, verbose_name='Вы резидент РБ')
    resident_usa = models.BooleanField(default=False, verbose_name='Вы налоговый резидент США')

    class Meta:
        db_table = 'user_db'


class CreditTest(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название кредита')
    cost_credit = models.CharField(max_length=25, verbose_name='Размер кредита')
    date_credit = models.IntegerField(verbose_name='Срок кредита в мес.')
    repayment_schedule = models.CharField(max_length=25, verbose_name='график погашения')
    schedule_1_6 = models.CharField(max_length=100, verbose_name='с 1 по 6 месяц кредитования')
    schedule_7 = models.CharField(max_length=100, blank=True, null=True, verbose_name='с 7 месяца по окончание срока КД')

    class Meta:
        db_table = 'credit_test'


class Product(models.Model):
    foto = models.FileField('фотка', upload_to='product/', blank=True, null=True)
    name_product = models.CharField(max_length=200, verbose_name='Название товара')
    cost = models.CharField(max_length=200, verbose_name='Цена товара')
    name_shop = models.CharField(max_length=250, verbose_name='Название магазина партнера')

    class Meta:
        db_table = 'product_shop'


class Documents(models.Model):
    agreement_KI = models.FileField(verbose_name=' Согласие на КИ', upload_to='documents/')
    agreement_personal = models.FileField(verbose_name='Согласие на обработку персональных данных', upload_to='documents/')
    infa_credit = models.FileField(verbose_name='Информация об условиях кредитования', upload_to='documents/')
    infa_individual = models.FileField(verbose_name='Индивидуальные условия договора', upload_to='documents/')

    class Meta:
        db_table = 'documents'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class History(models.Model):
    user = models.ForeignKey(UserNew, on_delete=models.CASCADE, related_name='history')
    product = models.CharField('Продукт', max_length=250)
    shop = models.CharField('Магазин', max_length=250)
    price = models.CharField('Цена', max_length=150)
    credit = models.ForeignKey(CreditTest, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField('статус', max_length=200)

    class Meta:
        db_table = 'history'


class StatusCredit(models.Model):
    name = models.ForeignKey(CreditTest, verbose_name='название продукта', on_delete=models.CASCADE)
    text = models.CharField('Статус', max_length=150)

    class Meta:
        db_table = 'status_credit'
