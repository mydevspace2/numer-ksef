# -*- coding: utf-8 -*-
"""Generuje lokalnie obraz Open Graph 1200x630 i logo 512x512 (PIL, bez usług zewnętrznych)."""
import os
from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/"
BRAND = (23, 71, 201)
GREEN = (34, 197, 94)
WHITE = (255, 255, 255)


def font(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)


def draw_logo(d, x, y, s):
    """Logo NumerKSeF (litera K + zielony znacznik) w kwadracie o boku s."""
    k = s / 32.0
    d.rounded_rectangle([x, y, x + s, y + s], radius=int(8 * k), fill=WHITE)
    pts = [(9, 9), (12, 9), (12, 15.2), (17.6, 9), (21.3, 9), (15.3, 15.6), (21.6, 23), (17.8, 23), (13.2, 17.6), (12, 18.9), (12, 23), (9, 23)]
    d.polygon([(x + px * k, y + py * k) for px, py in pts], fill=BRAND)
    cx, cy, r = x + 24.5 * k, y + 24.5 * k, 4.5 * k
    d.ellipse([cx - r - 1.5 * k, cy - r - 1.5 * k, cx + r + 1.5 * k, cy + r + 1.5 * k], fill=WHITE)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN)
    d.line([(x + 22.4 * k, y + 24.6 * k), (x + 23.8 * k, y + 26 * k), (x + 26.5 * k, y + 23.2 * k)], fill=WHITE, width=max(2, int(1.5 * k)), joint="curve")


def og(path):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), BRAND)
    d = ImageDraw.Draw(im)
    # subtelne koła w tle
    d.ellipse([820, -260, 1460, 380], fill=(30, 84, 220))
    d.ellipse([930, 360, 1330, 760], fill=(28, 79, 212))
    draw_logo(d, 80, 70, 96)
    d.text((196, 86), "NumerKSeF", font=font("DejaVuSans-Bold.ttf", 44), fill=WHITE)
    d.text((198, 140), "darmowe narzędzia KSeF", font=font("DejaVuSans.ttf", 26), fill=(214, 225, 255))
    d.text((80, 225), "Sprawdź numer KSeF", font=font("DejaVuSans-Bold.ttf", 76), fill=WHITE)
    d.text((80, 318), "i przygotuj tytuł przelewu oraz komunikat MPP", font=font("DejaVuSans.ttf", 36), fill=(225, 233, 255))
    # pasek z przykładowym numerem
    d.rounded_rectangle([80, 400, 1010, 478], radius=16, fill=WHITE)
    d.text((110, 419), "5265877635-20250826-0100001AF629-AF", font=font("DejaVuSansMono-Bold.ttf", 34), fill=(15, 23, 42))
    d.ellipse([948, 414, 996, 462], fill=GREEN)
    d.line([(960, 439), (969, 448), (985, 429)], fill=WHITE, width=6, joint="curve")
    d.text((80, 535), "numerksef.dpdns.org  ·  za darmo  ·  bez rejestracji  ·  dane zostają w przeglądarce",
           font=font("DejaVuSans.ttf", 26), fill=(214, 225, 255))
    im.save(path, "PNG", optimize=True)


def logo(path, s=512):
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=s // 4, fill=BRAND)
    k = s / 32.0
    pts = [(9, 9), (12, 9), (12, 15.2), (17.6, 9), (21.3, 9), (15.3, 15.6), (21.6, 23), (17.8, 23), (13.2, 17.6), (12, 18.9), (12, 23), (9, 23)]
    d.polygon([(px * k, py * k) for px, py in pts], fill=WHITE)
    cx, cy, r = 24.5 * k, 24.5 * k, 4.5 * k
    d.ellipse([cx - r - 1.5 * k, cy - r - 1.5 * k, cx + r + 1.5 * k, cy + r + 1.5 * k], fill=WHITE)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN)
    d.line([(22.4 * k, 24.6 * k), (23.8 * k, 26 * k), (26.5 * k, 23.2 * k)], fill=WHITE, width=int(1.5 * k), joint="curve")
    im.save(path, "PNG", optimize=True)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "site-v2", "assets")
    og(os.path.join(out, "og-numerksef.png"))
    logo(os.path.join(out, "logo-512.png"))
    print("ok")
