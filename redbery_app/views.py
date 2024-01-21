from rest_framework import viewsets,status
from .models import BlogModel, Category
from .serializers import BlogSerializer, CategorySerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .permissions import IsBlogPermisshion, IsCategoryPermisshion
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication
from django_filters import rest_framework as filters


# Create your views here.
class BlogFilter(filters.FilterSet):
    categories = filters.CharFilter(field_name='categories__name', lookup_expr='icontains')

    class Meta:
        model =BlogModel
        fields = ['categories']

class BlogView(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsBlogPermisshion]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BlogFilter

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsCategoryPermisshion]


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


 