from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class CreateTransactionView(CreateAPIView):
    model = Transaction
    serializer_class = TransactionSerializer

class DeleteTransactionView(DestroyAPIView):
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class UpdateTransactionView(UpdateAPIView):
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class ListTransactionView(ListAPIView):
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class DetailTransactionView(RetrieveAPIView):
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()