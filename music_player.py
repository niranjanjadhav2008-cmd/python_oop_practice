class MediaPlayer:
    def __init__(self,media_player_name,content):
        self.media_player_name = media_player_name
        self.content = content
        self.current_content_name = None
        self.current_volume = 75
        self.is_content_playing = False
        self.is_content_paused = False
        self.media_player_is_turned_on = False
        self.previous_volume = 0
        self.is_muted = False
    def show_current_volume(self):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is turned off..Turn it on to see volume"
        else:
            return f"Volume : {self.current_volume}"    
    def turn_on(self):
        if self.media_player_is_turned_on:
            return f"{self.media_player_name} is already turned on"
        self.media_player_is_turned_on = True
        return f"{self.media_player_name} turned on.."
    def turn_off(self):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is already turned off"
        self.is_content_playing = False
        self.media_player_is_turned_on = False
        return f"{self.media_player_name} turned off.."
    def play_content(self,content_name):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is turned off..Please turn on first to play a {self.content}"
        else:
            self.current_content_name = content_name
            self.is_content_playing = True
            self.is_content_paused = False
            return f"Playing : {self.current_content_name}"
    def pause_content(self):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is turned off..Please turn on and play a {self.content} first to pause a {self.content}"
        elif not self.is_content_playing:
            return f"Please play a {self.content} first to pause a {self.content}"
        elif self.is_content_paused:
            return f"{self.content} is already paused"
        else:
            self.is_content_playing = False 
            self.is_content_paused = True
            return f"{self.content} paused"
    def resume_content(self):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is turned off..Please turn on and pause a {self.content} first to resume a {self.content}"
        if self.current_content_name == None:
            return f"No {self.content} has been played"
        if not self.is_content_paused:
            return f"{self.content} is not paused"
        self.play_content(self.current_content_name)
        return f"{self.current_content_name} is resumed"
    def increase_volume(self,volume_to_be_increased_by):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is turned off..Please turn it on to increase the volume."
        elif volume_to_be_increased_by<0:
            return f"Please enter positive value"
        elif (self.current_volume + volume_to_be_increased_by) > 100:
            return f"Volume cannot be increased by {volume_to_be_increased_by}"
        else:
            self.current_volume += volume_to_be_increased_by
            return f"Volume increased to {self.current_volume}"
    def decrease_volume(self,volume_to_be_decreased_by):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is turned off..Please turn it on to decrease the volume."
        elif volume_to_be_decreased_by<0:
            return f"Please enter positive value"
        elif (self.current_volume - volume_to_be_decreased_by) < 0:
            return f"Volume cannot be decreased by {volume_to_be_decreased_by}"
        else:
            self.current_volume -= volume_to_be_decreased_by
            return f"Volume decreased to {self.current_volume}"
    def mute(self):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is currently turned off..Turn it on first to use this feature"
        if self.current_volume != 0:
            self.is_muted = True
            self.previous_volume = self.current_volume
            self.current_volume = 0
            return f"Muted"
        else:
            return f"{self.media_player_name} is already muted"
    def unmute(self):
        if not self.media_player_is_turned_on:
            return f"{self.media_player_name} is currently turned off..Turn it on first to use this feature"
        if not self.is_muted:
            return f"Not Muted..Current Volume : {self.current_volume}"
        self.is_muted = False
        self.current_volume = self.previous_volume
        return f"Unmuted"
class MusicPlayer(MediaPlayer):
    def __init__(self,music_player_name):
        self.music_player_name = music_player_name
        super().__init__(music_player_name,"Song")
    def play_song(self,song_name):
        self.current_song = song_name
        return super().play_content(self.current_song)
    def pause_song(self):
        return super().pause_content()
    def resume_song(self):
        return super().resume_content()
class VideoPlayer(MediaPlayer):
    def __init__(self,video_player_name):
        self.video_player_name = video_player_name
        super().__init__(video_player_name,"Video")
    def play_video(self,video_name):
        self.current_video = video_name
        return super().play_content(self.current_video)
    def pause_video(self):
        return super().pause_content()
    def resume_video(self):
        return super().resume_content()
class PodcastPlayer(MediaPlayer):
    def __init__(self,podcast_player_name):
        self.podcast_player_name = podcast_player_name
        super().__init__(podcast_player_name,"Podcast")
    def play_podcast(self,podcast_name):
        self.current_podcast = podcast_name
        return super().play_content(self.current_podcast)
    def pause_podcast(self):
        return super().pause_content()
    def resume_podcast(self):
        return super().resume_content()
M = MusicPlayer("Vanced")
print(M.turn_on())
print(M.increase_volume(15))
print(M.decrease_volume(20))
print(M.show_current_volume())
M.play_song("Jab Tak")
print(M.music_player_name)
print(M.mute())
print(M.show_current_volume())
print(M.decrease_volume(1))
print(M.unmute())
print(M.show_current_volume())
V = VideoPlayer("Youtube")
print(V.turn_on())
print(V.increase_volume(15))
print(V.decrease_volume(20))
print(V.show_current_volume())
V.play_video("Techno Gamerz")
print(V.video_player_name)
print(V.mute())
print(V.show_current_volume())
print(V.decrease_volume(1))
print(V.unmute())
print(V.show_current_volume())