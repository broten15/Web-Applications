from django.db import models

# Create your models here.

class Pizza(models.Model):
    """The types of pizzas that are offered"""
    text = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    
class Topping(models.Model):
    """Toping that you put on the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
        """Return a string representation of the models"""
        if len(self.name) > 50:
            return self.name[:50] + "..."
        else:
            return self.name