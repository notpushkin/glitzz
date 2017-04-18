from wsgiref.simple_server import make_server
from PIL import ImageDraw

from . import Glitzz


app = Glitzz(initial_color="#27365d")


@app.frame
def draw_frame(frame, position, duration):
    draw = ImageDraw.Draw(frame)
    draw.line((0, 0) + frame.size, fill="white")
    draw.line((0, frame.size[1], frame.size[0], 0), fill="white")
    return frame

server = make_server("", 8000, app)
print("Serving at port 8000. Run: ")
print("    %s" % app.get_ffmpeg_command())
server.serve_forever()
