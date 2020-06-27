from django.db import models
from django.contrib.auth.models import User as Admin


class User(models.Model):
    user_id = models.AutoField(editable=False, verbose_name='User ID', primary_key=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    experience_points = models.IntegerField(default=0, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='profile_picture/%Y/%m/%d/')

    def __str__(self):
        return f"{self.user_id} - {self.first_name} {self.last_name}".strip()


class Organization(models.Model):
    user = models.OneToOneField(Admin, on_delete=models.CASCADE, unique=True, blank=False, null=False)
    org_id = models.AutoField(editable=False, verbose_name='Organization ID', primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Organization Name', blank=False, null=False, unique=True)
    email = models.EmailField()
    org_picture = models.ImageField(upload_to='org_picture/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Event(models.Model):
    event_id = models.AutoField(editable=False, verbose_name='Event ID', primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Event Name', blank=False, null=False)
    time = models.DateTimeField(blank=False, null=False)
    duration = models.TimeField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    banner = models.ImageField(upload_to='event_banners/%Y/%m/%d/')
    managed_by = models.ForeignKey(to="Organization", on_delete=models.DO_NOTHING, blank=False, null=False)

    def __str__(self):
        return str(self.event_id)


class Post(models.Model):
    post_id = models.AutoField(editable=False, verbose_name='Post ID', primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    banner = models.ImageField(upload_to='post_banners/%Y/%m/%d/')
    type = models.CharField(max_length=5, choices=(("VIDEO", "Video"), ("TEXT", "Text")), blank=False, null=False)
    link = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    posted_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.post_id} - {self.title}".strip()