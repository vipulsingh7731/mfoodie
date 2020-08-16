from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return f'{self.name} - {str(self.price)}'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_amount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_addr = models.CharField(max_length=200, blank=True)
    orderedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    ORDER_STATE_WAITING = "Waiting"
    ORDER_STATE_PLACED = "Placed"
    ORDER_STATE_ACKNOWLEDGED = "Acknowledged"
    ORDER_STATE_COMPLETED = "Completed"
    ORDER_STATE_CANCELLED = "Cancelled"
    ORDER_STATE_DISPATCHED = "Dispatched"

    ORDER_STATE_CHOICES = (
        (ORDER_STATE_WAITING, ORDER_STATE_WAITING),
        (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
        (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
        (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
        (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
        (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
    )
    status = models.CharField(
        max_length=50, choices=ORDER_STATE_CHOICES, default=ORDER_STATE_WAITING)

    def __str__(self):
        return f'Order of Total {self.total_amount} of customer ({self.orderedBy.username})'


class orderItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Make {self.item_id.name} - {self.quantity}'
