"""Main module."""
import cv2
import os.path
import os
import youtube_dl
import requests
from PIL import Image
from io import BytesIO


class gvl:
    """
    Help on package gvl\n

    NAME
        gvl

    DESCRIPTION
        gvl (get video length) is a package for fetching the length of videos
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def _normalize_link(self, url: str) -> str:
        # shortend link: https://youtu.be/H0dqSl3epvg
        # normal   link: https://www.youtube.com/watch?v=H0dqSl3epvg
        # normal     id: H0dqSl3epvg
        if not url.startswith("https://") and len(url) == 11:
            return f"https://www.youtube.com/watch?v={url}"
        return url

    @classmethod
    def _get_image_dims(self, url: str):
        data = requests.get(url).content
        im = Image.open(BytesIO(data))
        return im.size

    @classmethod
    def _check_offline_video_id_validity(self, url: str) -> bool:
        """
        Checks the video id length
        note, this does not check if the video actually exists
        """
        # checks if the given url is valid and if the video id is 11 characters long
        return (
            url.startswith("https://")
            and len(url.rsplit("v=")[1]) == 11
            or len(url.rsplit("/")) == 11
        )

    @classmethod
    def _get_url_id(self, url: str) -> str:
        if url.startswith("https://"):
            return url.rsplit("v=")[1]
        return url.rsplit("/")

    @classmethod
    def _check_online_video_id_validity(self, url: str) -> bool:
        """
        check if the video exists on youtube
        """
        checker_url = f"https://img.youtube.com/vi/{self._get_url_id(self._normalize_link(url))}/mqdefault.jpg"
        r = requests.get(checker_url)
        invalid_image_dimensions = (120, 90)
        # print(self._get_image_dims(checker_url))
        return (
            True
            if self._get_image_dims(checker_url) != invalid_image_dimensions
            else False
        )

    @classmethod
    def video_file(self, filename: str) -> tuple[float, int, float]:
        """
        gvl.video_file() returns the duration, the frame count and the fps of the givin video file

            PARAMETERS
            ----------
                filename : str
                    The location of the video file

            USAGE
            -----
                >>> gvl.video_file("videos/superAwsomeSong.mp4")
                (9.8, 294, 30.0)

            RETURN
            ------
                duration : float
                    The video length in seconds
                fram_count : int
                    The amount of frames in the video
                fps : float
                    The videos FPS

            RAISE
            -----
                FileNotFoundError : Exception
                    File could not be found
                ZeroDivisionError : Exception
                    File might not be an actual video file
        """
        # Checks if the file exists
        if not os.path.isfile(filename):
            raise FileNotFoundError(f'File "{filename}" could not be found!')

        # Gets the video data
        video = cv2.VideoCapture(filename)
        # Gets the FPS the video is running at
        fps = video.get(cv2.CAP_PROP_FPS)
        # Gets the amount of frames the video have
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        # Checks if either fps or frame_count is 0 or less
        if fps <= 0 or frame_count <= 0:
            raise ZeroDivisionError(
                "either FPS or FRAME_COUNT is 0, are you sure it's a video file?"
            )
        # Calculates the duration by dividing frame_count by fps
        duration = frame_count / fps
        return (duration, int(frame_count), fps)

    @classmethod
    def video_url(self, url: str) -> tuple[float, int, float]:
        """
        gvl.video_url() returns the duration, the frame count and the fps of the givin video
        please note that gvl.video_url() is less precise than gvl.video_file()

            PARAMETERS
            ----------
                url : str
                    the url of the video

            USAGE
            -----
                >>> gvl.video_url("www.example.com/video.mp4")
                (9.8, 294, 30.0)

            RETURN
            ------
                duration : float
                    the video length in seconds
                fram_count : int
                    the amount of frames in the video
                fps : float
                    the videos FPS

            RAISE
            -----
                FileNotFoundError : Exception
                    file could not be found
        """
        ytdl_opts = {
            "forceurl": True,
            "quiet": True,
        }
        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
            r = ytdl.extract_info(self._normalize_link(url), download=False)

            # raise youtube_dl.utils.DownloadError(f"Could not download \"{url}\"")
        fps = r["fps"]
        duration = r["duration"]
        # Calculates the frame count by multiplying the videos frames per second with the duration
        frame_count = int(fps) * float(duration)
        return (duration, int(frame_count), fps)
