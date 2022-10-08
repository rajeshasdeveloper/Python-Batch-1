from django.urls import path, include
from rest_framework import routers
from awesome_api.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]