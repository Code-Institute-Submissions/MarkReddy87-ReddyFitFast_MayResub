from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """ Model for reviews """
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Setting ordering """
        ordering = ['-created_on']

    def __str__(self):
        return self.title
