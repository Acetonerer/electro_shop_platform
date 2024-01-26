from rest_framework.routers import DefaultRouter
from company.apps import CompanyConfig
from company.views import CompanyViewSet, ProductViewSet, ContactViewSet


app_name = CompanyConfig.name

router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('products', ProductViewSet, basename='products')
router.register('contacts', ContactViewSet, basename='contacts')

urlpatterns = [

] + router.urls
