from django.db import models

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.pk}] {self.title}"
    def get_absolute_url(self):
        return f"/program/{self.pk}/"