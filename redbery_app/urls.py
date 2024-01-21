from django.urls import path,include
from .views import BlogView, CategoryView, LoginView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'blogs', BlogView)
router.register(r'categories', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]

