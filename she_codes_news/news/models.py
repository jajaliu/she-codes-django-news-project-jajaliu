from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER, on_delete=models.CASCADE,
        related_name = "stories"
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(default="")

    # favourited_by = models.ManyToManyField(
    #     USER, related_name="favourites", blank=True 
    # )

# NewsStory.objects.order_by("pub_date")
