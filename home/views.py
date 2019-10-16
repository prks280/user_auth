from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Neta, Rating
from .permissions import NetaPermission
from .serializers import NetaSerializer, UserSerializer, RatingSerializer


class NetaViewSet(viewsets.ModelViewSet):
    queryset = Neta.objects.all()
    serializer_class = NetaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (NetaPermission,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    # def get_queryset(self):
    #     return Rating.objects.filter(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

    @action(methods=['post'], detail=False)
    def login(self, request, pk=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if not (username and password):
            return Response({'message': 'please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = User.objects.get(username=username)
            serialize_user = UserSerializer(user)
            return_user = serialize_user.data

            token, created = Token.objects.get_or_create(user=user)
            return Response({'user': return_user, 'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': 'failed to logged in'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['post'], detail=False)
    def logout(self, request, pk=None):
        logout(request)
        return Response({'message': 'successfully logged out'}, status=status.HTTP_200_OK)


# class TemplateTest(ListAPIView):
#     queryset = Neta.objects.all()
#     serializer_class = NetaSerializer
#
#     # renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
#
#     @action(methods=['get'], detail=True)
#     def test_api(self, request, *args, **kwargs):
#         if request.accepted_renderer.format == 'html':
#             return Response({'test': '123'}, template_name='test.html')
