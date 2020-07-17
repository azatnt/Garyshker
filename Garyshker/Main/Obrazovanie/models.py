from django.db import models
from django.utils.text import slugify
from time import time
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()




def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))







class Type(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)



class Genre(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)


class Format(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return str(self.name)



# class VideoPost(models.Model):
#     title = models.CharField(max_length=120)
#     text = models.TextField(blank=True, null=True)
#     clip = models.FileField(upload_to='item-videos')
#     created_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return str(self.title)



class Item(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
    # slug = models.SlugField(blank=True, unique=True)
    number_of_item = models.IntegerField()
    guest = models.CharField(max_length=120, default='Secret')
    image = models.ImageField(blank=True, upload_to='item-image')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='item-videos', default='Please upload video')
    description_video = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    leading = models.CharField(max_length=120, blank=True)
    views = models.PositiveIntegerField(default=0)
    clip = models.CharField(blank=True, max_length=120)




    def __str__(self):
        return str(self.name)


    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.name)
    #     super().save(*args, **kwargs)

# STATUS_CHOICES = (
#     ('CHECKING', 'CHECKING'),
#     ('READY', 'READY'),
# )


class Report(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # slug = models.SlugField(blank=True)
    title = models.CharField(max_length=120)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    # status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Checking')
    wrote_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    moderation = models.BooleanField("Проверено", default=False)
    # restrict_comment = models.BooleanField('Ограничить комментарий', default=False)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)


    def __str__(self):
        return str(self.title)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)



class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}-{}'.format(self.report.title, str(self.user.username))
