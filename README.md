# Glitzz

**A video generator in Python. Don't ask me why.**

```py
from PIL import ImageDraw
from glitzz import Glitzz


app = Glitzz(initial_color="#27365d")


@app.frame
def draw_frame(canvas, position, duration):
    """
    `canvas` is a PIL image. It's your canvas, draw on it
    `position` is current frame's time in seconds
    `duration` is length of the clip
    """
    draw = ImageDraw.Draw(canvas)
    draw.line((0, 0) + frame.size, fill="white")
    draw.line((0, frame.size[1], frame.size[0], 0), fill="white")
    return canvas


print("Serving at port 8000. Run: ")
print("    %s" % app.get_ffmpeg_command())
app.run()
```

This creates a 10-second video with frames like this:

![This is art](https://cloud.githubusercontent.com/assets/1298948/25152659/6a29e4c4-2492-11e7-8726-3bcca4ba3fef.png)

Let's run it:

```
$ python yourapp.py  # `python -m glitzz` to just run the default demo
Serving at port 8000. Run:
    ffmpeg -framerate 25 -f image2 -i http://localhost:8000/%d.bmp -vframes 250 filename.mp4
```

```
$ ffmpeg ...
Copyright (c) 2000-2017 the FFmpeg developers
Input #0, image2, from 'http://localhost:8000/%d.bmp'
Output #0, mp4, to 'filename.mp4'
Stream mapping:
  Stream #0:0 -> #0:0 (bmp (native) -> h264 (libx264))
Press [q] to stop, [?] for help
...
```
