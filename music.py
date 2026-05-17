import pygame
from globals import channel1

SONG_END = pygame.USEREVENT + 1
pygame.mixer.init()
pygame.mixer.music.set_endevent(SONG_END)

playlist = [
    "assets/music/Elevator_Ride.mp3",
    "assets/music/Swinging_Sixties.mp3",
    "assets/music/Rio_After_Dark.mp3",
    "assets/music/Fancy_Date.mp3",
]

current_track_index = 0

def play_next_song():
    global current_track_index
    # Load and play the current index
    track = pygame.mixer.Sound(playlist[current_track_index])
    channel1.play(track)
    
    # Move to the next index, loop back to 0 if at the end
    current_track_index = (current_track_index + 1) % len(playlist)
