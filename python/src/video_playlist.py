"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title
