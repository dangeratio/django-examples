from django.db import models
from time import time


# method to return a unique filename for each upload
def get_upload_file_name(instance, filename):
    return "uploads/%s_%s" % (str(time()).replace('.', '_'), filename)


class Article (models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)

    # not sure what this is for

    def __unicode__(self):
        return self.title

