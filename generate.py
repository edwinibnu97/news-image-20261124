#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news image (1024x1024) with Pillow.

Run:  python3 generate.py   ->  writes entry.png next to this file.

The four stories of Tuesday 24 November 2026, as first reported that day:
  1. NVIDIA - Jensen Huang returns as CEO after Donald Trump
     intervenes; shares jump 31%.
  2. UKRAINE - seven sea drones sink the Russian corvette Merkury
     off the Libyan coast.
  3. NATO - the alliance vows to defend against threats in space
     after reports of a Russian nuclear satellite.
  4. ICJ - the world court rules Myanmar committed genocide
     against the Rohingya.

This is a build-time script only. The graded entrypoint (main.py) is
standard-library-only and just copies the finished entry.png.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
GOLD = (252, 163, 17)
WHITE = (255, 255, 255)
GREY = (96, 96, 96)
BORDER = (214, 208, 190)
GREEN = (118, 185, 0)
GREEN_DARK = (74, 122, 0)
BLUE = (0, 87, 183)
SKY = (186, 220, 244)
SEA = (18, 92, 158)
SPACE = (11, 29, 51)
MAROON = (123, 45, 38)

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def fb(size):
    return ImageFont.truetype(FONT_B, size)


def fr(size):
    return ImageFont.truetype(FONT_R, size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centre(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


def draw_chip(d, cx, cy):
    """Green GPU chip with pins and a rising +31% arrow."""
    # pins
    for i in range(4):
        yy = cy - 45 + i * 30
        d.line([(cx - 105, yy), (cx - 78, yy)], fill=GREEN_DARK, width=6)
        d.line([(cx + 78, yy), (cx + 105, yy)], fill=GREEN_DARK, width=6)
    for i in range(4):
        xx = cx - 45 + i * 30
        d.line([(xx, cy - 82), (xx, cy - 55)], fill=GREEN_DARK, width=6)
        d.line([(xx, cy + 55), (xx, cy + 82)], fill=GREEN_DARK, width=6)
    # body
    d.rounded_rectangle([cx - 78, cy - 55, cx + 78, cy + 55],
                        radius=12, fill=GREEN, outline=GREEN_DARK, width=4)
    d.rounded_rectangle([cx - 48, cy - 32, cx + 48, cy + 32],
                        radius=8, fill=(140, 205, 30), outline=GREEN_DARK,
                        width=3)
    centre(d, cx, cy - 24, "AI", fb(44), WHITE)
    # rising arrow, upper right of the chip
    d.line([(cx + 92, cy + 18), (cx + 128, cy - 18), (cx + 158, cy - 48)],
           fill=GOLD, width=9)
    d.polygon([(cx + 158, cy - 48), (cx + 138, cy - 50), (cx + 156, cy - 28)],
              fill=GOLD)
    centre(d, cx + 128, cy - 96, "+31%", fb(34), GREEN_DARK)


def draw_sea(d, x, y, w, h):
    """Waves, a small drone boat and a sinking grey warship."""
    # sky band
    d.rectangle([x, y, x + w, y + 58], fill=SKY)
    d.ellipse([x + w - 78, y + 10, x + w - 28, y + 60], fill=(255, 214, 90))
    # sea
    d.rectangle([x, y + 58, x + w, y + h], fill=SEA)
    for k, yy in enumerate((y + 96, y + 128, y + 160)):
        pts = []
        for px in range(x, x + w + 1, 12):
            pts.append((px, yy + (10 if (px // 12 + k) % 2 else -10)))
        d.line(pts, fill=(120, 190, 235), width=5)
    # drone boat (small, left)
    bx, by = x + 52, y + 118
    d.polygon([(bx, by), (bx + 64, by), (bx + 54, by + 18), (bx + 10, by + 18)],
              fill=(40, 40, 40))
    d.line([(bx + 32, by), (bx + 32, by - 26)], fill=(40, 40, 40), width=4)
    d.ellipse([bx + 26, by - 34, bx + 38, by - 22], fill=(220, 60, 60))
    # sinking ship (tilted, right)
    sx, sy = x + w - 190, y + 92
    d.polygon([(sx, sy), (sx + 150, sy + 34), (sx + 132, sy + 62),
               (sx + 18, sy + 28)], fill=(110, 110, 110))
    d.line([(sx + 52, sy + 8), (sx + 40, sy - 26)], fill=(80, 80, 80),
           width=6)
    d.polygon([(sx + 40, sy - 26), (sx + 78, sy - 14), (sx + 40, sy - 6)],
              fill=(200, 60, 60))
    # bubbles
    for bx2, by2, r in ((sx + 30, sy + 74, 7), (sx + 58, sy + 88, 5),
                        (sx + 84, sy + 76, 6)):
        d.ellipse([bx2 - r, by2 - r, bx2 + r, by2 + r],
                  outline=(180, 220, 245), width=3)


def draw_space(d, x, y, w, h):
    """Dark sky, stars, a satellite and the Earth rising below."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=SPACE)
    stars = [(24, 22), (70, 60), (130, 26), (190, 66), (250, 30),
             (310, 58), (360, 24), (410, 70), (46, 110), (340, 112),
             (150, 104), (230, 120), (400, 130), (90, 140)]
    for sx, sy in stars:
        r = 3 if (sx + sy) % 3 else 2
        d.ellipse([x + sx - r, y + sy - r, x + sx + r, y + sy + r],
                  fill=WHITE)
    # Earth arc at the bottom
    d.ellipse([x + 60, y + h - 30, x + w - 60, y + h + 150],
              fill=(36, 110, 200))
    d.ellipse([x + 130, y + h - 6, x + 210, y + h + 40], fill=(70, 160, 90))
    d.ellipse([x + 300, y + h - 16, x + 360, y + h + 22], fill=(70, 160, 90))
    # satellite
    cx, cy = x + w // 2, y + 78
    d.rectangle([cx - 92, cy - 12, cx - 34, cy + 12], fill=(52, 120, 200),
                outline=(140, 190, 255), width=2)
    d.rectangle([cx + 34, cy - 12, cx + 92, cy + 12], fill=(52, 120, 200),
                outline=(140, 190, 255), width=2)
    d.rounded_rectangle([cx - 34, cy - 20, cx + 34, cy + 20], radius=6,
                        fill=(200, 205, 210), outline=WHITE, width=2)
    d.line([(cx, cy - 20), (cx, cy - 44)], fill=WHITE, width=3)
    d.ellipse([cx - 5, cy - 50, cx + 5, cy - 40], fill=GOLD)


def draw_scales(d, cx, cy):
    """Scales of justice in maroon."""
    c = MAROON
    d.line([(cx, cy - 78), (cx, cy + 78)], fill=c, width=7)
    d.line([(cx - 86, cy - 58), (cx + 86, cy - 58)], fill=c, width=7)
    d.ellipse([cx - 9, cy - 88, cx + 9, cy - 70], fill=c)
    d.line([(cx - 56, cy + 78), (cx + 56, cy + 78)], fill=c, width=7)
    for sx in (cx - 86, cx + 86):
        d.line([(sx, cy - 58), (sx - 34, cy + 6)], fill=c, width=4)
        d.line([(sx, cy - 58), (sx + 34, cy + 6)], fill=c, width=4)
        d.line([(sx, cy - 58), (sx, cy + 6)], fill=c, width=4)
        d.pieslice([sx - 36, cy - 8, sx + 36, cy + 34], start=0, end=180,
                   fill=c)


def card(img, d, x, y, w, h, accent, headline, caption, picture):
    """One news panel: accent bar, pictogram, headline, caption."""
    d.rounded_rectangle([x + 4, y + 6, x + w + 4, y + h + 6], radius=14,
                        fill=(228, 222, 206))
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=WHITE,
                        outline=BORDER, width=2)
    d.rounded_rectangle([x, y, x + w, y + 10], radius=6, fill=accent)
    d.rectangle([x, y + 5, x + w, y + 10], fill=accent)
    pic_h = 200
    # render the pictogram on its own layer and paste it clipped to a
    # rounded box, so no drawing can spill into the headline below
    layer = Image.new("RGBA", (w - 32, pic_h), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    # opaque white base: paste() with a mask ignores the layer's own
    # alpha, so transparent pixels would otherwise show up as black
    ld.rectangle([0, 0, w - 33, pic_h - 1], fill=(255, 255, 255, 255))
    picture(ld, 0, 0, w - 32, pic_h)
    mask = Image.new("L", (w - 32, pic_h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, w - 33, pic_h - 1], radius=10, fill=255)
    img.paste(layer, (x + 16, y + 26), mask)
    ty = y + 26 + pic_h + 14
    for line in wrap(d, headline, fb(30), w - 48):
        centre(d, x + w // 2, ty, line, fb(30), INK)
        ty += 38
    ty += 6
    for line in wrap(d, caption, fr(22), w - 48):
        centre(d, x + w // 2, ty, line, fr(22), (64, 64, 64))
        ty += 30


def pic_chip(d, x, y, w, h):
    draw_chip(d, x + w // 2 - 10, y + h // 2 + 8)


def pic_sea(d, x, y, w, h):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=SKY)
    draw_sea(d, x, y, w, h)


def pic_space(d, x, y, w, h):
    draw_space(d, x, y, w, h)


def pic_scales(d, x, y, w, h):
    draw_scales(d, x + w // 2, y + h // 2 + 4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.rectangle([0, 128, W, 134], fill=GOLD)
    centre(d, W // 2, 22, "THE WORLD IN ONE DAY", fb(52), WHITE)
    centre(d, W // 2, 88, "TUESDAY  •  24 NOVEMBER 2026", fb(28), GOLD)

    px, py, pw, ph, gap = 20, 150, 482, 410, 16
    card(img, d, px, py, pw, ph, GREEN, "HUANG BACK AT NVIDIA",
         "Jensen Huang returns as chief executive after Donald Trump "
         "intervenes. Shares jump 31%.", pic_chip)
    card(img, d, px + pw + gap, py, pw, ph, BLUE,
         "UKRAINE SINKS RUSSIAN SHIP",
         "Seven sea drones sink the corvette Merkury off the Libyan "
         "coast.", pic_sea)
    card(img, d, px, py + ph + gap, pw, ph, GOLD,
         "NATO VOWS TO DEFEND SPACE",
         "The alliance vows to answer threats in orbit after reports of "
         "a Russian nuclear satellite.", pic_space)
    card(img, d, px + pw + gap, py + ph + gap, pw, ph, MAROON,
         "ICJ: MYANMAR GUILTY OF GENOCIDE",
         "The world court rules Myanmar committed genocide against the "
         "Rohingya people.", pic_scales)

    centre(d, W // 2, 994, "FOUR STORIES  •  ONE DAY  •  24 NOVEMBER 2026",
           fb(17), GREY)
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
