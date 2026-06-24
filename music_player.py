class MusicPlayer():
    def __init__(self,music_player_name):
        self.music_player_name = music_player_name
        self.current_volume = 75
        self.music_player_is_turned_on = False
        self.is_song_playing = False
        self.is_song_paused = False
        self.previous_volume = 0
        self.current_song = None
        self.is_muted = False
    def show_current_volume(self):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is turned off..Turn it on to see volume"
        else:
            return f"Volume : {self.current_volume}"
    def turn_on(self):
        if self.music_player_is_turned_on:
            return f"{self.music_player_name} is already turned on"
        self.music_player_is_turned_on = True
        return f"{self.music_player_name} turned on.."
    def turn_off(self):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is already turned off"
        self.music_player_is_turned_on = False
        self.is_song_playing = False
        self.is_song_paused = False
        return f"{self.music_player_name} turned off.."
    def play_song(self,song_name):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is turned off..Please turn on first to play a song"
        else:
            self.current_song = song_name
            self.is_song_playing = True
            self.is_song_paused = False
            return f"Playing : {self.current_song}"
    def pause_song(self):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is turned off..Please turn on and play a song first to pause a song"
        elif not self.is_song_playing:
            return f"Please play a song first to pause a song"
        elif self.is_song_paused:
            return f"{self.current_song} is already paused"
        else:
            self.is_song_playing = False 
            self.is_song_paused = True
            return f"Song paused"
    def resume_song(self):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is turned off..Please turn on and pause a son first to resume a song"
        if self.current_song == None:
            return "No song has been played"
        self.play_song(self.current_song)
        return f"{self.current_song} is resumed"
    def increase_volume(self,volume_to_be_increased_by):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is turned off..Please turn it on to increase the volume."
        elif volume_to_be_increased_by<0:
            return f"Please enter positive value"
        elif (self.current_volume + volume_to_be_increased_by) > 100:
            return f"Volume cannot be increased by {volume_to_be_increased_by}"
        else:
            self.current_volume += volume_to_be_increased_by
            return f"Volume increased to {self.current_volume}"
    def decrease_volume(self,volume_to_be_decreased_by):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is turned off..Please turn it on to decrease the volume."
        elif volume_to_be_decreased_by<0:
            return f"Please enter positive value"
        elif (self.current_volume - volume_to_be_decreased_by) < 0:
            return f"Volume cannot be decreased by {volume_to_be_decreased_by}"
        else:
            self.current_volume -= volume_to_be_decreased_by
            return f"Volume decreased to {self.current_volume}"
    def skip_to_next_song(self,song_name):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is currently turned off..Turn it on first to use this feature"
        return self.play_song(song_name)
    def mute(self):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is currently turned off..Turn it on first to use this feature"
        if self.current_volume != 0:
            self.is_muted = True
            self.previous_volume = self.current_volume
            self.current_volume = 0
            return f"Muted"
        else:
            return f"{self.music_player_name} is already muted"
    def unmute(self):
        if not self.music_player_is_turned_on:
            return f"{self.music_player_name} is currently turned off..Turn it on first to use this feature"
        if not self.is_muted:
            return f"Not Muted..Current Volume : {self.current_volume}"
        self.is_muted = False
        self.current_volume = self.previous_volume
        return f"Unmuted"
    def display_current_status(self):
        print()
        print(f"----------{self.music_player_name} Current Status----------")
        print()
        print(f"Music Player Name : '{self.music_player_name}'")
        print()
        if self.music_player_is_turned_on:
            print(f"{self.music_player_name} is ON")
        else:
            print(f"{self.music_player_name} is OFF")
        print()
        if self.is_song_playing:
            print(f"Playing : {self.current_song} ")
        elif ((not self.is_song_playing) and (self.is_song_paused)):
            print("Song paused")
        else:
            print("Song not played yet")
        print()
        print(f"Volume : {self.current_volume}")
        print(f"----------{self.music_player_name} Current Status end----------")
        print()
if __name__ == "__main__":
    Spotify = MusicPlayer("Spotify")
    print(Spotify.play_song("I think they call this love"))
    print(Spotify.pause_song())
    print(Spotify.turn_on())
    print(Spotify.pause_song())
    print(Spotify.resume_song())
    print(Spotify.play_song("I think they call this love"))
    print(Spotify.increase_volume(20))
    print(Spotify.decrease_volume(120))
    print(Spotify.decrease_volume(12))
    Spotify.display_current_status()
    print(Spotify.skip_to_next_song("I wanna be yours"))
    Spotify.display_current_status()
    print(Spotify.pause_song())
    print(Spotify.current_volume)
    print(Spotify.mute())
    print(Spotify.mute())
    print(Spotify.current_volume)
    print(Spotify.unmute())
    print(Spotify.current_volume)
    Spotify.display_current_status()
    print(Spotify.turn_off())
    print(Spotify.turn_off())
