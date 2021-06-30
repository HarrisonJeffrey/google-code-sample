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
