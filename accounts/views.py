from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from .models import Enterprises
from .serializer import EnterprisesSerialier




class EnterpriseView(generics.ListCreateAPIView):
    queryset = Enterprises.objects.all()
    serializer_class = EnterprisesSerialier
    filter_backends = [OrderingFilter]


class EnterprisesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprises.objects.all()
    serializer_class = EnterprisesSerialier
    lookup_field = 'cnpj'
    


