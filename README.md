﻿# MusicFinder
This Python script uses the `lyricsgenius` and `musicbrainzngs` libraries to find songs by lyrics and fetch additional information about the song.

## Features
**Lyrics search**: find_song_by_lyrics function takes a string of the lyrics as input and uses the Genius API to fetch for the song + additional information - Song title, artist, release date, and than it searches both Genius and MusicBrainz API. 
**User-friendly Output**: The script prints the results in a user-friendly format, making it easy to understand the output.
# How to use
1. Import the `lyricsgenius` and `musicbrainzngs` libraries.
2. Set up Genius with your Genius API key & MusicBrainz with your MusicBrainz user agent
3. Call the `find_song_by_lyrics` function with your desired lyrics.
