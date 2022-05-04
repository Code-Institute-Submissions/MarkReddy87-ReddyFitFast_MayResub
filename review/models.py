""" imports below """
from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """ Model for reviews """
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="review_from", null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        """ Setting ordering """
        ordering = ['-created_on']
