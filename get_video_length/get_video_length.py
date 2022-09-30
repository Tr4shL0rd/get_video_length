"""Main module."""
import cv2
class gvl:
    """
        Help on package gvl\n
        NAME
            gvl
        DESCRIPTION
            gvl (get video length) is a package for fetching the length of videos
    """
    
    def video_file(filename:str) -> tuple[float, int, float]:
        """
            PARAMETERS
            ----------
                filename : str
                    the location of the video file

            RETURN
            ------
                duration : float
                    the video length in seconds
                fram_count : int
                    the amount of frames in the video
                fps : float
                    the videos FPS

            USAGE
            -----
                >>> gvl.video_file("videos/superAwsomeSong.mp4")
                (9.8, 294, 30.0)
        """
        video = cv2.VideoCapture(filename)

        fps         = video.get(cv2.CAP_PROP_FPS)
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        duration    = frame_count/fps

        return (duration, int(frame_count),fps)
    
    def video_url(url:str) -> tuple[float,int,float]:
        ...