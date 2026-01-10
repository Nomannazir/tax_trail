from django.urls import path
from .views import SimulateView, CRAMetadataView

urlpatterns = [
    path('simulate/', SimulateView.as_view(), name='simulate'),
    path('cra-metadata/', CRAMetadataView.as_view(), name='cra-metadata'),
]
