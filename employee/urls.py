from django.conf.urls import include, url
from rest_framework import routers

from employee.views import EmployeeViewSet, index

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'', index, name='index'),
]