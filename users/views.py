import jwt
import json
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .serializers import UserSerializer
from rest_framework import viewsets, permissions
from products.serializers import ProductSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)  
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({ "username": request.user.username })

class LoginView(APIView):
    permission_classes = []  # No authentication needed for login view

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"detail": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }

        try:
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        except Exception as e:
            return Response({"detail": f"Error generating token: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'token': token})

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            email = data.get("email")

            print("Registering user:", username, email)

            if not username or not password or not email:
                return JsonResponse({"error": "All fields are required."}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists."}, status=400)

            user = User.objects.create_user(username=username, password=password, email=email)
            return JsonResponse({"message": "User created successfully."})
        except Exception as e:
            print("Registration error:", str(e))  # 🔍 Add print for debugging
            return JsonResponse({"error": str(e)}, status=500)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)

def dashboard_view(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('/login/')
    return render(request, 'dashboard.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')

def products_page(request):
    return render(request, 'products.html')

def create_product_view(request):
    return render(request, 'create_product.html')