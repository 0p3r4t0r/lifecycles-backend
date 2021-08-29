from django.urls.resolvers import URLPattern
from goals.api import one_off, over_interval
from goals.apps import GoalsConfig
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'goal', one_off.Viewset)
router.register(r'daily', over_interval.Viewset)

app_name = GoalsConfig.name
urlpatterns = [
    path('', include(router.urls)),
]