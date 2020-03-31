from django.db import models
from backend.user.models import User
from backend.post.models import Post


class Vote(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_votes",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        related_name="post_votes",
    )

    class Meta:
        unique_together = ('user', 'post')
