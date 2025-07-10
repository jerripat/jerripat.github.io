from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Tag(models.Model):
    captions = models.CharField(max_length=50)
    def __str__(self):
        return self.captions
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.full_name()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='posts', null=True)
    slug = models.SlugField(unique=True, null=True)
    content = models.TextField(validators=[MinLengthValidator(10)], max_length=5000)
    tags = models.ManyToManyField(Tag, related_name='posts')
    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email_name = models.EmailField()
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
