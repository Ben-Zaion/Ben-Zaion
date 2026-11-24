
from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 900, 560
FRAMES = 36

BG = (5, 9, 18)
PANEL = (13, 20, 34)
CYAN = (55, 225, 255)
GREEN = (96, 255, 157)
WHITE = (220, 235, 245)
BLUE = (20, 45, 86)
BORDER = (44, 92, 125)

font_path = "/System/Library/Fonts/Menlo.ttc"

def font(size):
    return ImageFont.truetype(font_path, size)

def draw_window(draw, x, y, w, h, title):
    draw.rectangle(
        (x, y, x+w, y+h),
        fill=PANEL,
        outline=CYAN,
        width=2
    )
    draw.rectangle(
        (x+2, y+2, x+w-2, y+30),
        fill=BLUE
    )
    draw.text(
        (x+12, y+7),
        title,
        font=font(12),
        fill=WHITE
    )
    draw.text(
        (x+w-65, y+6),
        "_  □  ×",
        font=font(12),
        fill=WHITE
    )

def make_frame(frame):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Cyber desktop grid
    for y in range(0, HEIGHT, 4):
        draw.line(
            (0, y, WIDTH, y),
            fill=(7, 13, 22)
        )

    draw.text(
        (24, 18),
        "ZAION // CYBER DESKTOP",
        font=font(20),
        fill=CYAN
    )

    draw.text(
        (25, 47),
        "PERSONAL WORKSTATION | USER: BEN-ZAION",
        font=font(10),
        fill=(112, 142, 164)
    )

    # Desktop icons
    icons = [
        ("MY COMPUTER", 100),
        ("JOURNAL.TXT", 190),
        ("PROJECTS", 280),
        ("BUNNY.EXE", 370)
    ]

    for name, y in icons:
        draw.rectangle(
            (28, y, 86, y+48),
            fill=(18, 29, 47),
            outline=BORDER
        )

        draw.text(
            (40, y+10),
            "[*]",
            font=font(16),
            fill=GREEN
        )

        draw.text(
            (25, y+53),
            name,
            font=font(10),
            fill=WHITE
        )

    # Profile window
    draw_window(
        draw, 155, 92, 690, 360,
        r"C:\ZAION\PROFILE.EXE"
    )

    draw.text(
        (178, 139),
        "WELCOME TO ZAION OS",
        font=font(25),
        fill=GREEN
    )

    draw.text(
        (178, 190),
        "USER       : BEN-ZAION",
        font=font(15),
        fill=WHITE
    )

    draw.text(
        (178, 220),
        "ROLE       : SOFTWARE DEVELOPER",
        font=font(15),
        fill=WHITE
    )

    draw.text(
        (178, 250),
        "FOCUS      : ENTERPRISE SYSTEMS",
        font=font(15),
        fill=WHITE
    )

    draw.text(
        (178, 280),
        "EXPLORING  : CYBERSECURITY / AI",
        font=font(15),
        fill=WHITE
    )

    # ASCII rabbit
    rabbit = [
        " /)_/)",
        "( o.o )",
        " > ^ <"
    ]

    for i, line in enumerate(rabbit):
        draw.text(
            (710, 220 + i*25),
            line,
            font=font(18),
            fill=GREEN
        )

    # Terminal popup
    if frame >= 8:
        draw_window(
            draw, 330, 335, 390, 145,
            "SYSTEM TERMINAL"
        )

        messages = [
            "C:\\ZAION> boot journal.exe",
            "Loading curiosity.dll ... OK",
            "Learning mode: ACTIVE"
        ]

        for i, message in enumerate(messages):
            draw.text(
                (348, 375 + i*25),
                message,
                font=font(12),
                fill=GREEN
            )

        cursor = "_" if frame % 2 == 0 else " "

        draw.text(
            (348, 450),
            "C:\\ZAION> " + cursor,
            font=font(12),
            fill=GREEN
        )

    # Windows-like taskbar
    draw.rectangle(
        (24, 475, 875, 520),
        fill=(18, 29, 47),
        outline=BORDER
    )

    draw.text(
        (38, 490),
        "START",
        font=font(12),
        fill=WHITE
    )

    draw.text(
        (120, 490),
        "SYSTEM READY",
        font=font(12),
        fill=GREEN
    )

    # Animated scanline
    scan_y = 60 + (frame * 9) % 420

    draw.line(
        (12, scan_y, 888, scan_y),
        fill=(14, 43, 55)
    )

    return img


frames = [
    make_frame(i)
    for i in range(FRAMES)
]

os.makedirs("assets", exist_ok=True)

frames[0].save(
    "assets/zaion-desktop.gif",
    save_all=True,
    append_images=frames[1:],
    duration=130,
    loop=0,
    optimize=True
)

print("ZAION desktop animation generated!")
