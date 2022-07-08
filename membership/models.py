from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

auth_user = settings.AUTH_USER_MODEL if getattr(settings, "AUTH_USER_MODEL") else User


PAIRS = (
  ('NAS100', 'NAS100'),
  ('US30', 'US30'),
  ('GOLD', 'GOLD'),
  ('USDJPY', 'USDJPY'),
  ('GBPJPY', 'GBPJPY'),
  ('GBPUSD', 'GBPUSD'),
  ('CADCHF', 'CADCHF'),
  ('NZDUSD', 'NZDUSD'),
  ('EURJPY', 'EURJPY'),
  ('EURUSD', 'EURUSD'),
  ('USDCAD', 'USDCAD'),
  ('BTCUSD', 'BTCUSD'),
  ('CHFJPY', 'CHFJPY'),
  ('EURGBP', 'EURGBP'),
  ('AUDUSD', 'AUDUSD'),
  ('USDCHF', 'USDCHF'),
)

CHART =(
  ('GLOBALPRIME', 'GLOBALPRIME'),
  ('FXCM', 'FXCM'),
  ('CURREBCYCOM', 'CURREBCYCOM'),
  ('OANDA', 'OANDA'),
  ('SAXO', 'SAXO'),
)

IDEA_STATUS = (
  ('Not triggered', 'Not triggered'),
  ('Hit tp', 'Hit tp'),
  ('Hit sl', 'Hit sl'),
  ('Pending', 'Pending')
)

ORDER_TYPE = (
  ('Sell', 'Sell'),
  ('Sell Stop', 'Sell Stop'),
  ('Sell Limit', 'Sell Limit'),
  ('Buy', 'Buy'),
  ('Buy Stop', 'Buy Stop'),
  ('Buy Limit', 'Buy Limit'),
)

TIMEFRAME = (
  ('5M', '5M'),
  ('15M', '15M'),
  ('30M', '30M'),
  ('H1', 'H1'),
  ('H4', 'H4'),
  ('Daily', 'Daily'),
  ('Weekly', 'Weekly'),
  ('Monthly', 'Monthly'),

)


class Tradeidea(models.Model):
  pair = models.CharField(max_length=20, choices=PAIRS, default='NAS100')
  chart = models.CharField(max_length=50, choices=CHART, default='GLOBALPRIME')
  order_type = models.CharField(max_length=50, choices=ORDER_TYPE, default='Sell')
  timeframe = models.CharField(max_length=20, choices=TIMEFRAME, default='15M')
  entry = models.CharField(max_length=20, default='0')
  tp1 = models.CharField(max_length=20, default='0')
  tp2 = models.CharField(max_length=20, default='0', blank=True, null=True)
  tp3 = models.CharField(max_length=20, default='0.', blank=True, null=True)
  sl = models.CharField(max_length=20, default='0')
  date_sent = models.DateTimeField(default=timezone.now)
  status = models.CharField(max_length=25, choices=IDEA_STATUS, default='Pending')
  def __str__(self):
    return self.pair

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

Choice_for_reservation = (
  ('Open', 'Open'),
  ('Closed', 'Closed'),
)
class Reservation(models.Model):
  OPEN = 0
  CLOSE = 2
  STATUS = (
        (OPEN, _("Open")),
        (CLOSE, _("Close")),
    )
  user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
  reserved_start_date = models.DateTimeField(default=timezone.now)
  reserved_end_date = models.DateTimeField(default=timezone.now)
  free_users = models.IntegerField(default=3)
  status = models.CharField(max_length=20, choices=Choice_for_reservation, default='None')
  updated_datetime = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "%s  %s  (%s to %s)" % (self.user.get_full_name(),
                                   self.get_status_display(),
                                   self.reserved_start_date.strftime( "%Y/%m/%d %H:%S"),
                                   self.reserved_end_date.strftime(  "%Y/%m/%d %H:%S"),)


STATUS_CHOICES = (
  ('Pending', 'Pending'),
  ('Canceled', 'Canceled'),
  ('Done', 'Done'),
  ('Changed', 'Changed'),
)

class LiveSession(models.Model):
  user = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True, blank=True)
  reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE)
  status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

