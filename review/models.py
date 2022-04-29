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

    # def save(self, *args, **kwargs):
    #     self.slug = self.slug or slugify(self.title)
    #     super().save(*args, **kwargs)

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
