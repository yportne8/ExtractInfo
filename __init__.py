import subprocess, sys
from pathlib import Path
from ytmusicapi import YTMusic
from mscookies import Browser, Cookies


get_info = [
 ['search','get_home', 'get_artist', 'get_artist_albums'],
 ['get_user', 'get_user_playlists', 'get_album_browse_id'],
 ['get_album', 'get_song', 'get_song_related', 'get_lyrics']]

get_youtubemusic = [
 ['get_charts'],
 ['get_mood_playlists'],
 ['get_watch_playlist'],
 ['get_mood_categories'],
 ['get_watch_playlist_shuffle']]
 
get_library = [
 ['get_library_playlists', 'get_library_songs'],
 ['get_library_albums', 'get_library_artists'],
 ['get_library_subscriptions', 'get_liked_songs'],
 ['get_library_upload_songs', 'get_library_upload_albums'],
 ['get_library_upload_artists', 'get_library_upload_artist'],
 ['get_library_upload_album', 'get_history']]
 
manage_library = [
 ['remove_history_items'],
 ['rate_song'],
 ['edit_song_library_status'],
 ['rate_playlist'],
 ['subscribe_artists'],
 ['unsubscribe_artists'],
 ['get_playlist'],
 ['get_playlist_suggestions'],
 ['create_playlist'],
 ['edit_playlist'],
 ['delete_playlist'],
 ['add_playlist_items'],
 ['remove_playlist_items'],
 ['upload_song'],
 ['delete_upload_entity']]


def extract_info(query):
    sys.path.append(str(Path(__file__).parent))
    proc = subprocess.Popen(f"extract_info.exe {query}",
                            stdout=subprocess.PIPE,
                            shell=False)
    return proc.stdout.read()