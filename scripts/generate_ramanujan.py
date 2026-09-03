"""
Renders the Ramanujan prime staircase: the counting function
pi(x) - pi(x/2) sweeping left to right, with each Ramanujan prime R_n
lighting up at the point where the curve crosses level n for the last time.

That "last crossing" is the whole definition -- R_n is the least x beyond
which pi(y) - pi(y/2) never drops below n again -- so the animation is the
definition, drawn. Pure Pillow, same cheap-on-CI budget as the epicycles.
"""
import os
from PIL import Image, ImageDraw

W, H = 480, 250
PAD_L, PAD_R = 34, 12
PAD_T, PAD_B = 18, 26
XMAX = 200
LIMIT = 6000          # compute f() far past XMAX so each R_n is provably correct
FRAMES = 110
HOLD = 18

BG = (13, 17, 23)
GRID = (30, 36, 46)
AXIS = (70, 78, 92)
CURVE = (0, 230, 200)
CURVE_DIM = (0, 230, 200, 70)
MARK = (108, 99, 255)
MARK_SOFT = (108, 99, 255, 115)
NODE = (255, 255, 255)
LABEL = (140, 148, 165)


def sieve(n):
    flags = bytearray([1]) * (n + 1)
    flags[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if flags[p]:
            flags[p * p:: p] = bytearray(len(flags[p * p:: p]))
        p += 1
    return flags


def counting_function(limit):
    """f[x] = pi(x) - pi(x//2), for x = 0..limit."""
    flags = sieve(limit)
    pi = [0] * (limit + 1)
    total = 0
    for x in range(limit + 1):
        total += flags[x]
        pi[x] = total
    return [pi[x] - pi[x // 2] for x in range(limit + 1)]


def ramanujan_primes(f, limit, count):
    """R_n = least x with f(y) >= n for every y >= x."""
    out = []
    for n in range(1, count + 1):
        last_below = 0
        for x in range(limit, 0, -1):
            if f[x] < n:
                last_below = x
                break
        out.append(last_below + 1)
    return out


def main():
    f = counting_function(LIMIT)
    fmax = max(f[: XMAX + 1])
    rps = [r for r in ramanujan_primes(f, LIMIT, fmax) if r <= XMAX]

    # sanity check against the known head of OEIS A104272
    known = [2, 11, 17, 29, 41, 47, 59, 67, 71, 97, 101, 107, 127, 149, 151]
    assert rps[: len(known)] == known[: len(rps)], rps[:15]

    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B

    def px(x):
        return PAD_L + plot_w * x / XMAX

    def py(y):
        return PAD_T + plot_h - plot_h * y / (fmax + 1)

    frames = []
    for frame in range(FRAMES + HOLD):
        t = min(frame, FRAMES - 1) / (FRAMES - 1)
        head = t * XMAX

        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img, "RGBA")

        # horizontal level lines, one per n that has an R_n on screen
        for n in range(1, fmax + 1):
            draw.line([PAD_L, py(n), W - PAD_R, py(n)], fill=GRID, width=1)
        draw.line([PAD_L, py(0), W - PAD_R, py(0)], fill=AXIS, width=1)
        draw.line([PAD_L, PAD_T, PAD_L, py(0)], fill=AXIS, width=1)

        # Ramanujan prime markers, revealed as the sweep reaches them
        for n, r in enumerate(rps, start=1):
            if r > head:
                continue
            draw.line([px(r), py(0), px(r), py(n)], fill=MARK_SOFT, width=1)
            draw.ellipse(
                [px(r) - 3.2, py(n) - 3.2, px(r) + 3.2, py(n) + 3.2],
                fill=MARK, outline=NODE, width=1,
            )

        # the staircase itself, drawn up to the sweep head
        pts = []
        for x in range(0, XMAX + 1):
            if x > head:
                break
            pts.append((px(x), py(f[x])))
            pts.append((px(min(x + 1, XMAX)), py(f[x])))
        if len(pts) > 2:
            draw.line(pts, fill=CURVE, width=2, joint="curve")
            hx, hy = pts[-1]
            draw.ellipse([hx - 6, hy - 6, hx + 6, hy + 6], fill=(0, 230, 200, 45))
            draw.ellipse([hx - 2.5, hy - 2.5, hx + 2.5, hy + 2.5], fill=NODE)

        draw.text((PAD_L - 26, PAD_T - 10), "n", fill=LABEL)
        draw.text((W - PAD_R - 74, H - PAD_B + 8), "x -> %d" % XMAX, fill=LABEL)
        draw.text((PAD_L + 4, H - PAD_B + 8), "pi(x) - pi(x/2)", fill=CURVE)
        shown = sum(1 for r in rps if r <= head)
        draw.text((W - PAD_R - 96, PAD_T - 10),
                  "R_n found: %2d" % shown, fill=MARK)

        frames.append(img)

    out_dir = "dist"
    os.makedirs(out_dir, exist_ok=True)
    frames[0].save(
        os.path.join(out_dir, "ramanujan.gif"),
        save_all=True,
        append_images=frames[1:],
        duration=45,
        loop=0,
    )
    print("wrote dist/ramanujan.gif  |  R_n on screen:", rps)


if __name__ == "__main__":
    main()
