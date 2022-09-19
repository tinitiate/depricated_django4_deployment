from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    customer_creditscore = models.IntegerField(blank=True, null=True)
    customer_req_loanamount = models.DecimalField(max_digits=65535, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
