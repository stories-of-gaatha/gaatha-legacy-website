from django.db import models


class SocialMedia(models.Model):
    """
    Social media model
    """

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="social_media_icons")

    class Meta:
        verbose_name = "Social media"
        verbose_name_plural = "A - Social medias"

    def __str__(self):
        return self.name


class People(models.Model):
    """
    People model
    """

    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    social_medias = models.ManyToManyField(SocialMedia)

    class Meta:
        verbose_name = "People"
        verbose_name_plural = "B - People"

    def __str__(self):
        return self.name
