from django.db import models

class MenuItem(models.Model):
    TYPE_CHOICES = (
        ('appertizer','appertizer'),
        ('sashimi','sashimi'),
        ('nigiri','nigiri'),
        ('sushi rolls','sushi rolls'),
        ('beverage','beverage'),
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200,choices=TYPE_CHOICES, blank=True, null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return '%s - $%s' % (self.name, self.price)

class Order(models.Model):
    table = models.IntegerField()

    def __str__(self):
        return '%s' % (self.table)

class OrderwMenuItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, blank=True, null=True)
