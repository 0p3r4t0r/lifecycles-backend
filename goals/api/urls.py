from django.urls.resolvers import URLPattern
from goals.api import daily, goal
from goals.apps import GoalsConfig
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'goal', goal.Viewset)
router.register(r'daily', daily.Viewset)

app_name = GoalsConfig.name
urlpatterns = [
    path('', include(router.urls)),
]