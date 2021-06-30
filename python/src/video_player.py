"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._currently_playing = None
        self._pause_status = False
        self._playlists = {}

    @property
    def currently_playing(self):
        return self._currently_playing

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos_object = self._video_library.get_all_videos()
        videos_formatted = sorted([str(video_info) for video_info in videos_object])
        [print(video_string) for video_string in videos_formatted]

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is not None:
            if self.currently_playing is not None:
                print(f"Stopping video: {self.currently_playing.title}")
            self._currently_playing = video
            self._pause_status = False
            print(f"Playing video: {video.title}")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.currently_playing is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.currently_playing.title}")
            self._currently_playing = None
            self._pause_status = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        random_video = random.choice(self._video_library.get_all_videos())
        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.currently_playing is None:
            print("Cannot pause video: No video is currently playing")
        elif self._pause_status is True:
            print(f"Video already paused: {self.currently_playing.title}")
        else:
            print(f"Pausing video: {self.currently_playing.title}")
            self._pause_status = True

    def continue_video(self):
        """Resumes playing the current video."""
        if self.currently_playing is None:
            print("Cannot continue video: No video is currently playing")
        elif self._pause_status is False:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self.currently_playing.title}")
            self._pause_status = False

    def show_playing(self):
        """Displays video currently playing."""
        playing = self.currently_playing
        if playing is None:
            print("No video is currently playing")
        else:
            playing_str = f"Currently playing: {playing}"
            if self._pause_status is True:
                print(f"{playing_str} - PAUSED")
            else:
                print(playing_str)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        if playlist is None:
            new_playlist = Playlist(playlist_name)
            self._playlists[playlist_name.lower()] = new_playlist
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        video = self._video_library.get_video(video_id)
        if video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif playlist is None:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video_id in playlist.videos:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            playlist.add_video(video)
            print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            [print(playlist.title) for playlist in self._playlists.values()]

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        if playlist is None:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            if len(playlist.videos) == 0:
                print("  No videos here yet")
            else:
                [print(f"  {video}") for video in playlist.videos.values()]

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        video = self._video_library.get_video(video_id)
        if playlist is None:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
