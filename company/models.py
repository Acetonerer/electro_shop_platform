from django.db import models

NULLABLE = {'null': True, 'blank': True}
SUBJECT_CHOICES = (
    ('0', 'Factory'),
    ('1', 'Retail'),
    ('2', 'Individual entrepreneur')
)


class Contacts(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Company(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    subs_electro_net = models.CharField(max_length=100, choices=SUBJECT_CHOICES, verbose_name='Субъект торговой сети')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Долг перед поставщиком', **NULLABLE)
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')

    def __str__(self):
        return f'{self.title} - модель {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
