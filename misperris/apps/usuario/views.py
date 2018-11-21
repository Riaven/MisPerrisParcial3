from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroUsuario

import json 
from django.http import HttpResponse
from rest_framework.views import APIView
from apps.usuario.serializers import UserSerializer
class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registrar.html"
    form_class = RegistroUsuario
    success_url = reverse_lazy('rescatado_listar')

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')