from django.db import models

class MpesaPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_number = models.CharField(max_length=30)
    transaction_date = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=50)
    result_code = models.IntegerField()
    result_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.receipt_number} - {self.amount}"
