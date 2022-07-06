from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


auth_user = settings.AUTH_USER_MODEL if getattr(settings, "AUTH_USER_MODEL") else User




# Create your models here.
CHOICES = (
  ('Monthly', 'Monthly'),  
  ('Bronze', 'Bronze'),
  ('Silver', 'Silver'),
  ('Gold', 'Gold'),
  ('Lifetime', 'Lifetime'),
  ('Signal only', 'Signal only'),
)

class Packages(models.Model):
    title = models.CharField(max_length=200, choices=CHOICES)
    quantity = models.IntegerField(default=3)
    price = models.FloatField(default=0)
    saving = models.FloatField(default=0)
    tax = models.FloatField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"

PACKAGE_CHOICESS = (
  ('Monthly','Monthly'),
  ('Bronze', 'Bronze'),
  ('Silver', 'Silver'),
  ('Gold', 'Gold'),
  ('Lifetime', 'Lifetime'),
  ('Signal only', 'Signal only'),
  
)
PAYMENT_CHOICES = (
  ('Payoal', 'Payment'),
  ('Stripe', 'Stripe'),
)
STATUS_CHOICES_FOR_PACKAGE = (
    ('Active', 'Active'),
    ('Expired', 'Expired'),
)

class SelectedPackage(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, choices=PACKAGE_CHOICESS ,default='Monthly')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Paypal')
    price = models.FloatField(default=0.0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES_FOR_PACKAGE, default='Active')

    def __str__(self):
        return self.title




