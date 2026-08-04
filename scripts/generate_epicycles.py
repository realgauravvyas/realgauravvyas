"""
Renders a Fourier-epicycle GIF: a chain of rotating vectors (radius 1/n on the
n-th odd harmonic) whose tip traces out a square wave, with the trail drawn as
it goes. Pure Pillow, no matplotlib, so it's cheap to run on every CI tick.
"""
import math
import os
from PIL import Image, ImageDraw

W = 480
IMG_H = 380
CX, CY = W // 2, 130
TRAIL_BASE = 210
SCALE = 65
N_HARMONICS = 9
FRAMES = 100
TRAIL_X = 40

BG = (13, 17, 23)
CIRCLE = (108, 99, 255, 90)
ARM = (108, 99, 255, 200)
TRACE = (0, 230, 200)
NODE = (255, 255, 255)


def epicycle_tip(t):
    x, y = CX, CY
    points = [(x, y)]
    for k in range(N_HARMONICS):
        n = 2 * k + 1
        r = SCALE * (4 / math.pi) * (1 / n)
        angle = n * t
        x += r * math.cos(angle)
        y += r * math.sin(angle)
        points.append((x, y))
    return points


def main():
    trail = []
    frames = []
    for f in range(FRAMES):
        t = 2 * math.pi * f / FRAMES
        pts = epicycle_tip(t)
        tip = pts[-1]
        trail.append((tip[1] - CY) + TRAIL_BASE)
        if len(trail) > TRAIL_X * 4:
            trail.pop(0)

        img = Image.new("RGB", (W, IMG_H), BG)
        draw = ImageDraw.Draw(img, "RGBA")

        for i in range(len(pts) - 1):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            n = 2 * i + 1
            r = SCALE * (4 / math.pi) * (1 / n)
            draw.ellipse([x0 - r, y0 - r, x0 + r, y0 + r], outline=CIRCLE, width=1)
            draw.line([x0, y0, x1, y1], fill=ARM, width=2)
        draw.ellipse([pts[-1][0] - 3, pts[-1][1] - 3, pts[-1][0] + 3, pts[-1][1] + 3], fill=NODE)

        draw.line([pts[-1][0], pts[-1][1], W - TRAIL_X * 4 + len(trail), pts[-1][1]], fill=(80, 80, 90, 60), width=1)

        step = 4
        base_x = W - len(trail) * step
        for i in range(1, len(trail)):
            x0 = base_x + (i - 1) * step
            x1 = base_x + i * step
            draw.line([x0, trail[i - 1], x1, trail[i]], fill=TRACE, width=2)

        frames.append(img)

    out_dir = "dist"
    os.makedirs(out_dir, exist_ok=True)
    frames[0].save(
        os.path.join(out_dir, "epicycles.gif"),
        save_all=True,
        append_images=frames[1:],
        duration=40,
        loop=0,
    )


if __name__ == "__main__":
    main()
