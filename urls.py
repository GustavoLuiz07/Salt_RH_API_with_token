from django.contrib import admin
from django.urls import include, path
from contrato.views import SaltRh_ClientesViewSet
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Duas views que vão dar acesso ao token 

router = routers.DefaultRouter()
router.register(r'Formulário de contrato da Salt-RH', SaltRh_ClientesViewSet)

urlpatterns = [
    path('saltrh', include(router.urls)),  
    path('api-auth/', include('rest_framework.urls')), 
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),                   # A URL que vai dar acesso ao token
    path('token/refresh/', TokenRefreshView.as_view()),              # URL para ter acesso ao refresh token
] 
