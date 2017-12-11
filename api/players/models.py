from nucleus.models import AbstractBaseModel
from django.conf import settings
from django.db import models
from django.db.models import Count


class PlayerQuerySet(models.QuerySet):
    def have_complete_profile(self):
        return self.annotate(
            num_regions=Count('regions'),
            num_positions=Count('positions')
        ).exclude(user__username='').filter(
            user__username__isnull=False, num_regions__gt=0, num_positions__gt=0
        )


class Player(AbstractBaseModel):
    username = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # TODO:
    # searchable = models.BooleanField(default=True)

    objects = PlayerQuerySet.as_manager()

    # def save(self, *args, **kwargs):
    #     try:
    #         Player.objects.get(pk=self.pk)
    #     except Player.DoesNotExist:
    #         new_player = True
    #     else:
    #         new_player = False
    #
    #     super(Player, self).save(*args, **kwargs)
    #
    #     if new_player:
    #         self.update_mmr()

    # def update_mmr(self):
    #     from .tasks import update_player_mmr
    #     update_player_mmr(self.pk)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return "<{}: {}>".format(type(self).__name__, self.user.username)

    def __str__(self):
        return self.user.username
