"""Generate original artwork images for the three demo websites (no stock photos needed)."""
import os
import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)


def lerp(a, b, t):
    return a + (b - a) * t


def hexrgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float32)


def gradient(w, h, stops):
    """Vertical gradient from list of (pos, hex)."""
    y = np.linspace(0, 1, h)[:, None]
    out = np.zeros((h, 1, 3), np.float32)
    for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
        m = (y >= p0) & (y <= p1)
        t = np.clip((y - p0) / max(p1 - p0, 1e-6), 0, 1)
        col = lerp(hexrgb(c0), hexrgb(c1), t[..., None])
        out = np.where(m[..., None], col, out)
    return np.repeat(out, w, axis=1)


def ridge(w, base, amp, rough, seed):
    r = np.random.default_rng(seed)
    x = np.linspace(0, 1, w)
    y = np.zeros(w)
    for k in range(1, 7):
        f = r.uniform(0.6, 1.4) * 1.3 * 2 ** k
        y += r.uniform(0.4, 1) / (k ** (rough + 0.7)) * np.sin(2 * np.pi * (f * x + r.uniform()))
    y = (y - y.min()) / (np.ptp(y) + 1e-6)
    return base - amp * y


def fill_below(img, line, color, alpha=1.0):
    h, w, _ = img.shape
    yy = np.arange(h)[:, None]
    mask = (yy >= line[None, :]).astype(np.float32)[..., None] * alpha
    img[:] = img * (1 - mask) + hexrgb(color) * mask


def glow(img, cx, cy, r, color, strength=1.0):
    h, w, _ = img.shape
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    a = np.clip(np.exp(-d ** 2) * strength, 0, 1)[..., None]
    img[:] = img * (1 - a) + hexrgb(color) * a


def disc(img, cx, cy, r, color, soft=2.0):
    h, w, _ = img.shape
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    a = np.clip((r - d) / soft, 0, 1)[..., None]
    img[:] = img * (1 - a) + hexrgb(color) * a


def finish(img, name, grain=6, vignette=0.35, blur=0):
    h, w, _ = img.shape
    img = img + rng.normal(0, grain, img.shape)
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    img = img * (1 - vignette * np.clip(d - 0.4, 0, 1)[..., None])
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    path = os.path.join(ROOT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, quality=84, optimize=True, progressive=True)
    print("saved", name)


def mountains(name, w, h, sky, sun, layers, water=None, sun_r=60):
    img = gradient(w, h, sky)
    if sun:
        glow(img, sun[0] * w, sun[1] * h, sun_r * 5, sun[2], 0.55)
        disc(img, sun[0] * w, sun[1] * h, sun_r, sun[3])
    for i, (base, amp, col, alpha) in enumerate(layers):
        fill_below(img, ridge(w, base * h, amp * h, 1.2 + i * 0.2, 11 + i * 5), col, alpha)
    if water:
        wl = int(water[0] * h)
        refl = img[:wl][::-1][: h - wl].copy()
        refl = lerp(refl, hexrgb(water[1]), 0.45)
        img[wl:wl + refl.shape[0]] = refl
        for _ in range(140):
            y = rng.integers(wl, h)
            x0 = rng.integers(0, w)
            ln = rng.integers(20, 120)
            img[y, x0:x0 + ln] = lerp(img[y, x0:x0 + ln], hexrgb("#ffffff"), 0.12)
    return img


def forest(name, w, h):
    img = gradient(w, h, [(0, "#c9d6cf"), (0.6, "#e6e2d3"), (1, "#a9b8a8")])
    for li, (yb, col, a, sc) in enumerate([(0.55, "#8fa597", 0.6, 0.5), (0.68, "#5f7a6a", 0.8, 0.75),
                                            (0.82, "#2f4a3d", 1, 1.0), (0.97, "#16261f", 1, 1.4)]):
        layer = img.copy()
        xs = np.arange(0, w, int(28 * sc))
        for x in xs:
            th = rng.uniform(140, 300) * sc
            tw = th * 0.32
            base = yb * h + rng.uniform(-12, 12)
            yy, xx = np.mgrid[0:h, 0:w]
            inside = (yy <= base) & (yy >= base - th) & (np.abs(xx - x) <= tw * (yy - (base - th)) / th)
            layer[inside] = hexrgb(col)
        layer[int(yb * h):] = hexrgb(col)
        img = lerp(img, layer, a)
        img = lerp(img, hexrgb("#dfe5dc"), 0.12 * (3 - li) / 3)
    return img


def dunes(w, h):
    img = gradient(w, h, [(0, "#f4c9a0"), (0.45, "#f7e1c4"), (1, "#e9b384")])
    glow(img, 0.72 * w, 0.32 * h, 380, "#fff3dc", 0.8)
    disc(img, 0.72 * w, 0.32 * h, 48, "#fff8ea")
    for i, (base, amp, col) in enumerate([(0.62, 0.12, "#e3a46e"), (0.74, 0.14, "#cf8a52"),
                                          (0.88, 0.16, "#b86e3c"), (1.02, 0.18, "#8f4f28")]):
        fill_below(img, ridge(w, base * h, amp * h, 2.2, 40 + i), col)
    return img


def city(w, h):
    img = gradient(w, h, [(0, "#0b1030"), (0.55, "#2a2257"), (0.8, "#7b3f6e"), (1, "#e07a5f")])
    for _ in range(220):
        x, y = rng.integers(0, w), rng.integers(0, int(h * 0.5))
        img[y, x] = hexrgb("#ffffff") * rng.uniform(0.4, 1)
    x = 0
    while x < w:
        bw = int(rng.uniform(40, 110))
        bh = rng.uniform(0.18, 0.55) * h
        top = int(h - bh)
        img[top:, x:x + bw] = hexrgb("#0d0f1f") * rng.uniform(0.8, 1.2)
        for wy in range(top + 12, h - 10, 18):
            for wx in range(x + 8, x + bw - 8, 14):
                if rng.random() < 0.35:
                    img[wy:wy + 7, wx:wx + 6] = hexrgb(rng.choice(["#ffd27d", "#ffe9b0", "#9fd3ff"]))
        x += bw + int(rng.uniform(2, 10))
    return img


def aurora(w, h):
    img = gradient(w, h, [(0, "#020617"), (0.7, "#0b1d3a"), (1, "#0f2c3f")])
    for _ in range(300):
        xx, yy = rng.integers(0, w), rng.integers(0, int(h * 0.7))
        img[yy, xx] = hexrgb("#ffffff") * rng.uniform(0.3, 1)
    xs = np.arange(w)
    for k, col in enumerate(["#34d399", "#22d3ee", "#a78bfa"]):
        center = h * (0.32 + 0.08 * k) + 60 * np.sin(xs / w * 6 + k)
        yy = np.arange(h)[:, None]
        band = np.exp(-((yy - center[None, :]) / (90 - 20 * k)) ** 2) * 0.55
        img[:] = img * (1 - band[..., None]) + hexrgb(col) * band[..., None]
    fill_below(img, ridge(w, 0.86 * h, 0.14 * h, 1.4, 77), "#050a12")
    return img


def bokeh(w, h, base_stops, colors, n=70):
    img = gradient(w, h, base_stops)
    lay = np.zeros_like(img)
    for _ in range(n):
        cx, cy = rng.uniform(0, w), rng.uniform(0, h)
        r = rng.uniform(18, 90)
        col = hexrgb(rng.choice(colors))
        yy, xx = np.mgrid[0:h, 0:w]
        d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        a = np.clip((r - d) / 3, 0, 1) * rng.uniform(0.15, 0.45)
        lay = lay * (1 - a[..., None]) + col * a[..., None]
        img = img * (1 - a[..., None]) + col * a[..., None]
    return img


if __name__ == "__main__":
    W, H = 1500, 1000
    P = "photographer/img/"
    finish(mountains("", W, H, [(0, "#2b3a67"), (0.45, "#e98a6b"), (0.62, "#ffd6a5"), (1, "#ffd6a5")],
                     (0.62, 0.5, "#ffb37a", "#fff1d6"),
                     [(0.62, 0.18, "#8c6a8f", 0.85), (0.74, 0.2, "#5b456e", 1), (0.9, 0.22, "#2b2142", 1)]),
           P + "alpine-dawn.jpg")
    finish(mountains("", W, H, [(0, "#0f2027"), (0.5, "#4b6b8a"), (0.62, "#c7d3dd"), (1, "#c7d3dd")],
                     None, [(0.5, 0.12, "#6f8aa1", 0.9), (0.6, 0.14, "#3d566e", 1)],
                     water=(0.62, "#1b2c3c")), P + "still-lake.jpg")
    finish(forest("", W, H), P + "misty-forest.jpg", grain=5)
    finish(dunes(W, H), P + "desert-dunes.jpg")
    finish(city(W, H), P + "city-dusk.jpg", grain=4)
    finish(aurora(W, H), P + "northern-lights.jpg", grain=4)
    finish(mountains("", H, W, [(0, "#1e3c72"), (0.5, "#6dd5ed"), (1, "#f5f7fa")], (0.5, 0.2, "#ffffff", "#ffffff"),
                     [(0.55, 0.25, "#9fb6c9", 0.8), (0.75, 0.3, "#4a6378", 1), (0.95, 0.3, "#1c2a36", 1)], sun_r=34),
           P + "summit-portrait.jpg")
    finish(mountains("", H, W, [(0, "#3a1c71"), (0.5, "#d76d77"), (1, "#ffaf7b")], (0.5, 0.55, "#ffd1a1", "#fff0de"),
                     [(0.7, 0.2, "#6b2f5a", 1), (0.88, 0.22, "#2c1338", 1)], water=None, sun_r=40),
           P + "coast-sunset.jpg")
    finish(bokeh(W, H, [(0, "#1a1210"), (1, "#2a1a14")], ["#ffb347", "#ff8c42", "#ffe0a3", "#ffcf7a"]),
           "photographer/img/hero.jpg", blur=1.5)
    # restaurant hero: warm candlelit bokeh
    finish(bokeh(W, H, [(0, "#1c0f0a"), (1, "#3b1d12")], ["#ffb347", "#ff7b39", "#ffd9a0", "#e8603c"], n=90),
           "restaurant/img/hero.jpg", blur=2)
    # clinic hero: calm teal bokeh
    finish(bokeh(W, H, [(0, "#e6f4f1"), (1, "#cfe9e4")], ["#9fd8cb", "#7cc6b6", "#ffffff", "#b9e3da"], n=60),
           "physio/img/hero.jpg", grain=3, vignette=0.1, blur=2)
