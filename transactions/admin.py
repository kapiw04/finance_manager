from django.contrib import admin

from transactions.models import Transaction, TransactionCategory


# Register your models here.
@admin.register(Transaction)
class TransactionCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    pass

