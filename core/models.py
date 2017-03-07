from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TimestampModelMixin(models.Model):
    """
    Mixin to create models with auto created timestamp
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __unicode__(self):
        return '{}'.format(self.name)


class Post(TimestampModelMixin, models.Model):
    link = models.URLField(max_length=255)
    comment = models.CharField(max_length=255)
    account = models.ForeignKey(Account)
    publication_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return '{}'.format(self.link)



