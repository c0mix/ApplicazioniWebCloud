from rest_framework import viewsets
from sito.models import Sportivo, Attivita, Risultato, Test
from sito.serializers import SportivoSerializer, AttivitaSerializer, UserSerializer, TestSerializer
#from rest_framework import permissions
from django.contrib.auth.models import User
#from server.sito.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #def user_list(request):
    #    return renderers(request, 'blog/post_list.html', {})

class SportivoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Sportivo.objects.all()
    serializer_class = SportivoSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class AttivitaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Attivita.objects.all()
    serializer_class = AttivitaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class TestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer