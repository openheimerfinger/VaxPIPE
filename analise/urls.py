from django.urls import path
from .views import Dados, Analisar

urlpatterns = [
    path('', Dados.as_view(), name='dadosform'),
    path('recebidos', Analisar.as_view(), name='recebido'),
]