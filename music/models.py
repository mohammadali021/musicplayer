from django.db import models


# Create your models here.
class Artist(models.Model):
    artistName = models.CharField(max_length=50, verbose_name="نام هنرمند")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "هنرمند"
        verbose_name_plural = "هنرمندان"

    def __str__(self):
        return self.artistName


class Album(models.Model):
    artist = models.ForeignKey("Artist", verbose_name="خواننده", on_delete=models.CASCADE)
    albumName = models.CharField(max_length=50, verbose_name="نام آلبوم")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "آلبوم"
        verbose_name_plural = "نام آلبوم"

    def __str__(self):
        return self.albumName


class Song(models.Model):
    album = models.ForeignKey("Album", on_delete=models.CASCADE, verbose_name="نام آلبوم")
    songThumbnail = models.ImageField(upload_to='thmbnail/', help_text=".jpg , .png , .jpeg supported",
                                      verbose_name="تصویر")
    song = models.FileField(upload_to='songs/', help_text="mp3 supported only", verbose_name="موزیک")
    songName = models.CharField(max_length=50, verbose_name="نام موزیک")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "موزیک"
        verbose_name_plural = "نام موزیک"

    def __str__(self):
        return self.songName
