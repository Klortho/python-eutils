from django.db import models
import datetime
from django.utils import timezone

# Each class here inherits from  django.db.models.Model:
# https://docs.djangoproject.com/en/1.5/ref/models/instances/

class Poll(models.Model):
    # Each field is represented by an instance of the Field class - the name
    # depends on the data type.
    # The max_length argument of CharField is required.
    # Model field reference:  https://docs.djangoproject.com/en/1.5/ref/models/fields/
    question = models.CharField(max_length=200)
    # The first, optional positional argument is the human-readable name.
    # If it's not given, the machine-readable name will be used as the label.
    pub_date = models.DateTimeField('date published')

    # This is like toString() in Java (?).  It defines a method to use whenever
    # you want a string representation of the object
    def __unicode__(self):
        return self.question

    # Here's a custom method for demo purposes
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # These method attributes control how this custom field looks in the admin
    # interface (see https://docs.djangoproject.com/en/1.5/intro/tutorial02/)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField('text of the choice', max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text