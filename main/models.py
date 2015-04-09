from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
