from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.models import User
from users.serializers import UserRegisterSerializer

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

# Create your views here.
