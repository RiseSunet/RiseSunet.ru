#!/usr/bin/env python3
"""Генератор обложек для игры «Глубина 4.0» — без внешних зависимостей, только PIL."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = "/home/mihail/Игры/Глубина/PressStart2P-Regular.ttf"
if not os.path.exists(FONT_PATH):
    FONT_PATH = "/home/mihail/Игры/Глубина/сайт/игры/глубина/PressStart2P-Regular.ttf"


def font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except Exception:
        return ImageFont.load_default()


def gradient(w, h, top, bottom):
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=c)
    return img


def draw_grid(img, step, color):
    d = ImageDraw.Draw(img)
    w, h = img.size
    for x in range(0, w, step):
        d.line([(x, 0), (x, h)], fill=color, width=1)
    for y in range(0, h, step):
        d.line([(0, y), (w, y)], fill=color, width=1)


def draw_pixel_miner(d, x, y, scale=6):
    """Простой пиксельный буровик, нарисованный квадратами."""
    body = [
        "....######....",
        "...########...",
        "..##..##..##..",
        "..##..##..##..",
        "..##########..",
        "...########...",
        "....######....",
        "....#....#....",
        "...##....##...",
    ]
    colors = {"#": (232, 238, 252), ".": None}
    for row, line in enumerate(body):
        for col, ch in enumerate(line):
            if colors[ch]:
                d.rectangle(
                    [x + col * scale, y + row * scale,
                     x + (col + 1) * scale - 1, y + (row + 1) * scale - 1],
                    fill=colors[ch],
                )
    # жёлтый шлем
    d.rectangle([x + 4 * scale, y, x + 9 * scale, y + 1 * scale - 1], fill=(255, 210, 61))
    # глаза
    d.rectangle([x + 4 * scale, y + 2 * scale, x + 5 * scale, y + 3 * scale - 1], fill=(17, 22, 31))
    d.rectangle([x + 8 * scale, y + 2 * scale, x + 9 * scale, y + 3 * scale - 1], fill=(17, 22, 31))


def center_text(d, text, y, w, fnt, fill, shadow=(0, 0, 0), shadow_off=4):
    box = d.textbbox((0, 0), text, font=fnt)
    tw = box[2] - box[0]
    x = (w - tw) // 2
    d.text((x + shadow_off, y + shadow_off), text, font=fnt, fill=shadow)
    d.text((x, y), text, font=fnt, fill=fill)


def youtube():
    w, h = 1280, 720
    img = gradient(w, h, (10, 16, 32), (42, 10, 10))
    draw_grid(img, 48, (26, 36, 60))
    d = ImageDraw.Draw(img)
    # боковые «слои пор»
    for i, col in enumerate([(139, 90, 43), (160, 140, 107), (95, 100, 110), (255, 68, 26)]):
        y = h - 120 - i * 40
        d.rectangle([0, y, w, y + 30], fill=col)
    draw_pixel_miner(d, 150, 300, 14)
    center_text(d, "ГЛУБИНА 4.0", 120, w, font(96), (255, 210, 61), shadow_off=8)
    center_text(d, "АРКАДНАЯ БУРОВАЯ", 250, w, font(40), (92, 225, 255), shadow_off=5)
    # рекорд
    d.rounded_rectangle([w - 470, 60, w - 60, 180], radius=18, fill=(10, 16, 28), outline=(255, 210, 61), width=4)
    d.text((w - 440, 78), "РЕКОРД", font=font(28), fill=(154, 165, 189))
    d.text((w - 440, 115), "1270 м", font=font(46), fill=(255, 210, 61))
    d.text((60, 640), "Играть бесплатно в браузере", font=font(24), fill=(232, 238, 252))
    img.save(os.path.join(HERE, "preview-youtube.png"))
    print("✓ preview-youtube.png")


def tiktok():
    w, h = 1080, 1920
    img = gradient(w, h, (10, 16, 32), (23, 10, 42))
    draw_grid(img, 60, (26, 36, 60))
    d = ImageDraw.Draw(img)
    draw_pixel_miner(d, w // 2 - 84, 420, 12)
    center_text(d, "ГЛУБИНА", 180, w, font(86), (255, 210, 61), shadow_off=7)
    center_text(d, "4.0", 300, w, font(70), (92, 225, 255), shadow_off=6)
    center_text(d, "БУРИ ГЛУБЖЕ!", 700, w, font(52), (255, 255, 255), shadow_off=5)
    center_text(d, "КОМБО x5", 800, w, font(44), (255, 210, 61), shadow_off=4)
    center_text(d, "5 БИОМОВ", 880, w, font(44), (92, 225, 255), shadow_off=4)
    center_text(d, "ДОСТИЖЕНИЯ", 960, w, font(44), (95, 224, 138), shadow_off=4)
    center_text(d, "ССЫЛКА В ПРОФИЛЕ", 1650, w, font(40), (255, 210, 61), shadow_off=5)
    img.save(os.path.join(HERE, "preview-tiktok.png"))
    print("✓ preview-tiktok.png")


def square():
    w = h = 1080
    img = gradient(w, h, (10, 16, 32), (42, 10, 10))
    draw_grid(img, 54, (26, 36, 60))
    d = ImageDraw.Draw(img)
    draw_pixel_miner(d, w // 2 - 84, 360, 12)
    center_text(d, "ГЛУБИНА", 140, w, font(82), (255, 210, 61), shadow_off=7)
    center_text(d, "4.0", 250, w, font(64), (92, 225, 255), shadow_off=6)
    center_text(d, "ИГРАЙ БЕСПЛАТНО", 740, w, font(34), (232, 238, 252), shadow_off=4)
    img.save(os.path.join(HERE, "cover-glubina.png"))
    print("✓ cover-glubina.png")


if __name__ == "__main__":
    youtube()
    tiktok()
    square()
    print("Готово!")
