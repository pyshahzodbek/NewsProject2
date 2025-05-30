from django.db import models
from django.urls import reverse
from django.utils import timezone



# Create your models here.
# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return  super().get_queryset().filter(status=News.status.Published)
# class Category(models.Model):
#     name=models.CharField(max_length=150)
#
#
#     def __str__(self):
#         return self.name
#
#
#
#
# class News(models.Model):
#
#     class Status(models.TextChoices):
#         Draft="DF","Draft"
#         Published= "PB","Published"
#     title=models.CharField(max_length=250)
#     slug=models.SlugField(max_length=250)
#     body=models.TextField()
#     image=models.ImageField(upload_to='news/images')
#     category=models.ForeignKey(Category,
#                                on_delete=models.CASCADE
#                                )
#     publish_time=models.DateTimeField(default=timezone.now)
#     created_time=models.DateTimeField(auto_now_add=True)
#     update_time=models.DateTimeField(auto_now=True)
#     status=models.CharField(max_length=2,
#                             choices=Status.choices,
#                             default=Status.Draft
#                             )
#
#     objects=models.Manager() # default manager
#     published=PublishedManager()
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering=["-publish_time"]

# from django.db import models
# from django.utils import timezone
#
# Custom Manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="PB")  # "PB" qiymatini bevosita yozdik

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
    )

    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager


    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
            return self.title


    def get_absolute_url(self):
             return reverse("news_detail_page", args=[self.slug])

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.email