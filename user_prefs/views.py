from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from user_prefs.models import Prefs
from user_prefs.serializers import UserPreferencesSerializer


class PrefsUpdateView(UpdateAPIView):
    model = Prefs
    serializer_class = UserPreferencesSerializer

    def get_object(self):
        return Prefs.get_instance()

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(Prefs.get_instance()).data)