import lyricsgenius

genius=lyricsgenius.Genius("vgaC3VxDr9BIOEfYDxlTtiBiJxIvZKQYDb4tln0QrRKg8DzyFBkFQdVaQ5MYrnp8")
artist = genius.search_artist("Madd", max_songs=0, sort="title")
song = artist.song("lowlife")
with open("lowlife.txt","w") as f:
	f.write(song.lyrics)
