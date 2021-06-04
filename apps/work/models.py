from django.db import models


class Tag(models.Model):
    """
    Tag model
    """

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "A - Tags"

    def __str__(self):
        return self.name


class WorkType(models.Model):
    """
    Work type model
    """

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Work type"
        verbose_name_plural = "B - Work types"

    def __str__(self):
        return self.name


class Picture(models.Model):
    """
    Picture model
    """

    image = models.ImageField(upload_to="pictures", max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "C - Pictures"

    def __str__(self):
        return self.image.url


class Work(models.Model):
    """
    Work model
    """

    artwork = models.FileField(null=True, blank=True, upload_to="artworks")
    cover_image = models.ImageField(
        null=True, blank=True, upload_to="cover_images", max_length=255
    )
    cover_description = models.TextField(blank=True)
    is_featured_in_dashboard = models.BooleanField(default=False)
    # Work type foreign key
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT)
    # Tag and pictures
    tags = models.ManyToManyField(Tag)
    picture = models.ManyToManyField(Picture)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "D - Works"

    def __str__(self):
        # String representation of press dossier
        return str(self.id)
