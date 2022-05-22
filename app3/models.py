from django.db import models


class messagemodel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.username


class msgModel(models.Model):
    message = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    created_by = models.ManyToManyField(messagemodel)

    def __str__(self):
        return self.message
