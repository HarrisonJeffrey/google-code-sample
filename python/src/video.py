"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._flagged = False
        self._flagged_reason = None

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flagged(self):
        if self._flagged:
            return self._flagged_reason
        else:
            return None

    def flag(self, flagged_reason):
        self._flagged = True
        self._flagged_reason = flagged_reason

    def allow(self):
        self._flagged = False
        self._flagged_reason = None

    def __str__(self):
        """Changes string representation to title (video_id) [tags]"""
        str_representation = f"{self.title} ({self.video_id}) [{' '.join(self.tags)}]"
        if self.flagged is None:
            return str_representation
        else:
            return f"{str_representation} - FLAGGED (reason: {self._flagged_reason})"
