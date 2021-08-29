from django.urls.resolvers import URLPattern
from goals.api import one_off, over_interval
from goals.apps import GoalsConfig
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'one-off', one_off.Viewset)
router.register(r'over-interval', over_interval.Viewset)

app_name = GoalsConfig.name
urlpatterns = [
    path('', include(router.urls)),
]