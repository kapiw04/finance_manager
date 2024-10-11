from django.urls import path

from user_prefs.views import PrefsUpdateView

urlpatterns = [
    path("update", PrefsUpdateView.as_view(), name="user_prefs_update"),
]