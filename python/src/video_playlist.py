"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, title):
        self._title = title
        self._videos = {}

    @property
    def title(self):
        return self._title

    @property
    def videos(self):
        return self._videos

    def add_video(self, video):
        self._videos[video.video_id] = video

    def remove_video(self, video, playlist_name):
        deleted = self._videos.pop(video.video_id, None)
        if deleted is None:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            print(f"Removed video from {playlist_name}: {video.title}")

    def __str__(self):
        return self.title
