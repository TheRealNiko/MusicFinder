import lyricsgenius
import musicbrainzngs

# Set up Genius
genius = lyricsgenius.Genius('10225840')

# Set up MusicBrainz
musicbrainzngs.set_useragent("Music Finder", "WnbzCNOGP_Flq47zzI5K6hishxNQSks4", "yzeGY6TrDmcS7Lzh-Ce8Y268BHYB5YAv")

def find_song_by_lyrics(lyrics):
    # Search for songs that contain the lyrics
    song = genius.search_song(lyrics)
    
    if song:
        print(f"Found song: {song.title} by {song.artist}")
        
        # Search for the song on MusicBrainz
        result = musicbrainzngs.search_recordings(query=song.title, artist=song.artist, limit=1)
        
        if result['recording-list']:
            recording = result['recording-list'][0]
            print(f"Found track on MusicBrainz: {recording['title']} by {recording['artist-credit'][0]['artist']['name']}")
            
            # Get the release date of the song
            if 'release-list' in recording and recording['release-list']:
                release = recording['release-list'][0]
                if 'date' in release:
                    print(f"Release date: {release['date']}")
                else:
                    print("Release date not found")
            else:
                print("Release date not found")
        else:
            print("Track not found on MusicBrainz")
    else:
        print("Song not found")

# Text input for lyrics
find_song_by_lyrics("")
