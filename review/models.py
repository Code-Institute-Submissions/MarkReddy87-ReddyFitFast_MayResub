from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Review(models.Model):
    """ Model for reviews """
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="review_from")
    created_on = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    # def auto_slug(self):
    #     """ auto slugify title """
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save()

    class Meta:
        """ Setting ordering """
        ordering = ['-created_on']
