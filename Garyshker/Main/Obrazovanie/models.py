from django.db import models
from django.utils.text import slugify
from time import time


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




class Item(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
    # slug = models.SlugField(blank=True, unique=True)
    number_of_item = models.IntegerField()
    guest = models.CharField(max_length=120, default='Secret')
    image = models.ImageField(blank=True, upload_to='item-image')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.name)


    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.name)
    #     super().save(*args, **kwargs)
