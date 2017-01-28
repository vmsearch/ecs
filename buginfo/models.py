from django.db import models

# Create your models here.
class BugInfo(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    info = models.TextField()
    owner = models.CharField(max_length=200) 
    status = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='published time')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return ('bug_detail/%s/') % self.id
