from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# CATEGORY_CHOICES = (
#     ('Fashion & Style','FASHION & STYLE'),
#     ('Cars & Property', 'CARS & PROPERTY'),
#     ('Electronics & Mobiles','ELECTRONICS & MOBILES'),
#     ('Home & Living','HOME & LIVING'),
#     ('Others','Others'),
# )
# class Category(models.Model):
#     category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='Fashion & Style')

class Item(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to='neighimage/', null=True)
    description = models.CharField(max_length = 300)
    price = models.IntegerField(default='$ 0.0')
    # category = models.CharField(max_length = 300)

    posted_time = models.DateTimeField(auto_now_add=True,)
    seller = models.ForeignKey(User, related_name='userholder')

    class Meta:
        ordering = ['-posted_time']

    def __str__(self):
        return self.name

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()

    @classmethod
    def get_items(cls):
        items = cls.objects.all()
        return items



