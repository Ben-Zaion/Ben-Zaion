
#!/usr/bin/env python3
"""
ZAION // CYBER DESKTOP
Generate an animated retro-terminal banner.

Requires: Pillow
Run: python3 generate_banner.py
Output: assets/cyber-desktop.gif
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math
import random

# ==========================================
# CONFIGURATION
# ==========================================

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "cyber-desktop.gif"

W, H = 1000, 320
FRAME_COUNT = 48

# Cross-platform monospace fonts
FONT_CANDIDATES = [
    "/System/Library/Fonts/Menlo.ttc",
    "/System/Library/Fonts/Supplemental/Courier New.ttf",
    "/Library/Fonts/Courier New.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "C:/Windows/Fonts/consola.ttf",
]

BOLD_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
    "/Library/Fonts/Courier New Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "C:/Windows/Fonts/consolab.ttf",
]

def find_font(candidates):
    for path in candidates:
        if Path(path).exists():
            return path
    return None

FONT = find_font(FONT_CANDIDATES)
BOLD = find_font(BOLD_CANDIDATES) or FONT

if FONT is None:
    raise RuntimeError("No compatible monospace font found.")

def fnt(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


# ==========================================
# ANIMATION GENERATOR
# ==========================================

def main():

    random.seed(21)

    stars = [
        (
            random.randint(25, W - 25),
            random.randint(25, H - 25),
            random.uniform(.5, 1.8),
            random.uniform(0, math.tau)
        )
        for _ in range(90)
    ]

    frames = []

    for frame in range(FRAME_COUNT):

        # Background
        im = Image.new("RGB", (W, H), "#030713")
        d = ImageDraw.Draw(im)

        # Grid
        for x in range(0, W, 32):
            d.line((x, 0, x, H), fill="#07162b")

        for y in range(0, H, 24):
            d.line((0, y, W, y), fill="#07162b")

        # Animated stars
        for x, y, r, p in stars:
            a = int(50 + 80 * (
                .5 + .5 * math.sin(frame * .16 + p)
            ))

            d.ellipse(
                (x-r, y-r, x+r, y+r),
                fill=(5, a//2, a)
            )

        # Desktop frame
        d.rectangle(
            (15, 14, W-16, H-15),
            outline="#075b83",
            width=2
        )

        d.rectangle(
            (20, 19, W-21, H-20),
            outline="#062a49"
        )

        # Header
        d.rectangle(
            (22, 21, W-23, 54),
            fill="#081b35"
        )

        d.text(
            (38, 29),
            "ZAION // CYBER DESKTOP",
            font=fnt(18, True),
            fill="#27e6ff"
        )

        d.text(
            (W-250, 32),
            "SYS 01  |  ONLINE",
            font=fnt(11),
            fill="#61f5b1"
        )

        d.line(
            (25, 56, W-25, 56),
            fill="#0a5c82"
        )

        # Terminal window
        d.rectangle(
            (42, 75, 958, 279),
            fill="#071426",
            outline="#12d8f5",
            width=2
        )

        d.rectangle(
            (44, 77, 956, 101),
            fill="#102849"
        )

        d.text(
            (58, 82),
            "C:\\ZAION\\PROFILE.EXE",
            font=fnt(11),
            fill="#c7e8f4"
        )

        d.text(
            (905, 81),
            "_  □  ×",
            font=fnt(11),
            fill="#c7e8f4"
        )

        # Terminal content
        d.text(
            (65, 119),
            "WELCOME TO ZAION OS",
            font=fnt(25, True),
            fill="#55ffad"
        )

        lines = [
            ("USER", "BEN-ZAION"),
            ("ROLE", "SOFTWARE DEVELOPER"),
            ("FOCUS", "ENTERPRISE SYSTEMS"),
            ("EXPLORING", "CYBERSECURITY / AI / QUANTUM"),
        ]

        y = 163

        for label, value in lines:

            d.text(
                (68, y),
                label,
                font=fnt(13),
                fill="#65cce9"
            )

            d.text(
                (175, y),
                ":",
                font=fnt(13),
                fill="#65cce9"
            )

            d.text(
                (195, y),
                value,
                font=fnt(13),
                fill="#d2e5f0"
            )

            y += 25

        # ==================================
        # ANIMATED CYBER RADAR
        # ==================================

        cx, cy = 790, 190

        pulse = .75 + .25 * math.sin(
            frame * math.tau / 24
        )

        glow = Image.new(
            "RGBA",
            (W, H),
            (0, 0, 0, 0)
        )

        gd = ImageDraw.Draw(glow)

        rad = int(44 * pulse)

        for rr, alpha in [
            (rad*2, 22),
            (rad, 38),
            (rad//2, 55)
        ]:

            gd.ellipse(
                (cx-rr, cy-rr, cx+rr, cy+rr),
                fill=(0, 180, 255, alpha)
            )

        glow = glow.filter(
            ImageFilter.GaussianBlur(16)
        )

        im = Image.alpha_composite(
            im.convert("RGBA"),
            glow
        )

        d = ImageDraw.Draw(im)

        # Radar light rays
        for angle in [
            0,
            math.pi/4,
            math.pi/2,
            3*math.pi/4
        ]:

            length = (
                64 if angle in (0, math.pi/2)
                else 43
            ) * pulse

            dx = math.cos(angle) * length
            dy = math.sin(angle) * length

            d.line(
                (cx-dx, cy-dy, cx+dx, cy+dy),
                fill="#16dfff",
                width=2
            )

        d.ellipse(
            (cx-5, cy-5, cx+5, cy+5),
            fill="#b4fbff"
        )

        # Bunny signature
        d.text(
            (865, 147),
            " /) /)",
            font=fnt(14, True),
            fill="#57ffb1"
        )

        d.text(
            (865, 166),
            "( o.o )",
            font=fnt(14, True),
            fill="#57ffb1"
        )

        d.text(
            (865, 185),
            " > ^ <",
            font=fnt(14, True),
            fill="#57ffb1"
        )

        # ==================================
        # STATUS BAR
        # ==================================

        d.rectangle(
            (42, 290, 958, 307),
            fill="#0b1e35",
            outline="#125477"
        )

        d.text(
            (55, 292),
            "START",
            font=fnt(10),
            fill="#c8e4ee"
        )

        d.text(
            (130, 292),
            "SYSTEM READY",
            font=fnt(10),
            fill="#55ffad"
        )

        cursor = "_" if (frame // 8) % 2 == 0 else " "

        d.text(
            (780, 292),
            "SCANNING" + cursor,
            font=fnt(10),
            fill="#28dfff"
        )

        # ==================================
        # CRT SCANLINES
        # ==================================

        overlay = Image.new(
            "RGBA",
            (W, H),
            (0, 0, 0, 0)
        )

        od = ImageDraw.Draw(overlay)

        for sy in range(0, H, 4):
            od.line(
                (0, sy, W, sy),
                fill=(0, 0, 0, 30)
            )

        # Moving scan beam
        by = int((frame * 7) % H)

        od.rectangle(
            (0, by, W, by+2),
            fill=(0, 210, 255, 22)
        )

        im = Image.alpha_composite(
            im,
            overlay
        )

        frames.append(im.convert("RGB"))

    # ======================================
    # EXPORT GIF
    # ======================================

    OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=85,
        loop=0,
        optimize=True
    )

    print(f"\n[ OK ] Generated: {OUT}")
    print(f"[ OK ] Resolution: {W}x{H}")
    print(f"[ OK ] Frames: {FRAME_COUNT}")
    print("[ OK ] ZAION SYSTEM ONLINE\n")


if __name__ == "__main__":
    main()
