import io
from wsgiref.simple_server import make_server

from PIL import Image


class Glitzz:
    """
    A simple WSGI application that serves Nth frame at /{N}.bmp.
    """

    def __init__(self, framerate=25, duration=10,
                 width=1920, height=1080, initial_color="white"):
        self.framerate = framerate
        self.duration = duration
        self.frame_count = framerate * duration

        self.canvas = Image.new("RGB", (width, height), initial_color)

    def draw_frame(self, canvas, position, duration):
        """
        By default, does nothing.
        """
        return canvas

    def frame(self, f):
        self.draw_frame = f
        return f

    def get_ffmpeg_command(self, port=8000):
        return " ".join([
            "ffmpeg",
            "-framerate %s" % self.framerate,
            "-f image2 -i http://localhost:%d/%%d.bmp" % port,
            "-vframes %s" % self.frame_count,
            "filename.mp4"
        ])

    def __call__(self, environ, start_response):
        frame_number = int(environ["PATH_INFO"].lstrip("/").split(".", 1)[0])
        if not 0 <= frame_number < self.frame_count:
            start_response("404 Not Found", [])
            return []

        start_response("200 OK", [("Content-type", "image/bmp")])

        frame = self.draw_frame(self.canvas,
                                position=frame_number / self.framerate,
                                duration=self.duration)

        f = io.BytesIO()
        frame.save(f, "bmp", compress_level=0)
        return [f.getvalue()]

    def run(self, port=8000):
        server = make_server("", port, self)
        server.serve_forever()
