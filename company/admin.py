from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from company.models import Company, Product, Contacts


@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ('title', 'subs_electro_net', 'provider_link',
                    'debt', 'date_created', 'contacts_city',)
    list_filter = ('contacts__city',)
    actions = ['debt_removal']

    def provider_link(self, obj):
        if obj.provider:
            url = reverse('admin:company_company_change', args=[obj.provider.pk])
            return format_html('<a href="{}">{}</a>', url, obj.provider.title)
        return '-'
    provider_link.short_description = 'Поставщик'

    def contacts_city(self, obj):
        if obj.contacts.city:
            return obj.contacts.city
        return '-'
    contacts_city.short_description = 'Город'

    @admin.action(description='Удалить долг')
    def debt_removal(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'company',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country',)
