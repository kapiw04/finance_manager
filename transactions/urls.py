from django.urls import path

from transactions import views

urlpatterns = [
    path("create/", views.CreateTransactionView.as_view(), name="transaction_create"),
    path("list/", views.ListTransactionView.as_view(), name="transaction_list"),
    path("delete/<int:pk>", views.DeleteTransactionView.as_view(), name="transaction_delete"),
    path("update/<int:pk>", views.UpdateTransactionView.as_view(), name="transaction_update"),
    path("details/<int:pk>", views.DetailTransactionView.as_view(), name="transaction_details"),
]