from department.views import EmployeeViewSet, DepartmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'emplyees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
urlpatterns = router.urls