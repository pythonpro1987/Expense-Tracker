from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices= TRANSACTION_TYPE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
    
