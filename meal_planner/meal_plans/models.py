from django.db import models

# Create your models here.

class Day(models.Model):
    """The day of the week that a meal is scheduled for"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Meal(models.Model):
    """A meal that you eat on a specific day"""
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'meals'

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text        