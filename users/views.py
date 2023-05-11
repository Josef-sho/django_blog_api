from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
class CustomUserView(APIView):
    def get(self, request):
        # Implement your logic to retrieve and return user data
        users = CustomUser.objects.all()
        # You can serialize the users data if needed
        serialized_users = UserSerializer(users, many=True).data
        return Response(serialized_users)
