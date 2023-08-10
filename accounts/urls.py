from django.urls import path
from .views import EnterpriseView, EnterprisesDetailView

urlpatterns = [
    path('enterprises/', EnterpriseView.as_view()),
    path('enterprises/<str:cnpj>', EnterprisesDetailView.as_view())
]