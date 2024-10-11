from django.urls import path

from analysis.views import BudgetStatusView

urlpatterns = [
    path("budget-status/", BudgetStatusView.as_view(), name="budget-status"),
]