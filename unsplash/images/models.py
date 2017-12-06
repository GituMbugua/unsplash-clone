from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    @classmethod
    def get_tags(cls):
        tags = cls.objects.all()
        return tags

    @classmethod
    def search_by_tags(cls, search_term):
        tag = cls.objects.filter(name__icontains = search_term)
        return tag

class Image(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    location = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
