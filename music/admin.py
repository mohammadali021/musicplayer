from django.contrib import admin

from music.models import Album, Artist, Song


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'albumName', 'created', 'last_updated')
    list_editable = ('artist', 'albumName')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artistName', 'created', 'last_updated')
    list_editable = ()


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'songName', 'song', 'songThumbnail', 'album', 'created', 'last_updated')
    list_editable = ('songName', 'song', 'songThumbnail', 'album')


# admin.site.register(Song, SongAdmin)
# admin.site.register(Album, AlbumAdmin)
# admin.site.register(Artist, ArtistAdmin)
