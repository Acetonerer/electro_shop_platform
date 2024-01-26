from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from company.models import Company, Product
from company.serializers import (CompanySerializer, ProductSerializer,
                                 ContactSerializer, CompanyCreateSerializer)


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Класс создания, просмотра, редактирования и удаления компании
    """
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CompanyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Класс создания, просмотра, редактирования и удаления продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    """
    Класс создания, просмотра, редактирования и удаления контакта
    """
    serializer_class = ContactSerializer
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated]
