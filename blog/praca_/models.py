from django.db import models
class Page(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.pk} - {self.title} - {self.is_private}"


class Post(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()

    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.name}"

class Literature(models.Model):
    name_book = models.CharField(max_length=150)
    publishing_house = models.CharField(max_length=150)
    year_release = models.PositiveIntegerField()
    post = models.ManyToManyField(Post)

    def __str__(self):
        return f"{self.pk} - {self.name_book} - {self.publishing_house} - {self.year_release}"