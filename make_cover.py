"""
인스타그램 카드뉴스 표지 생성 스크립트 (Pillow)
- 크기: 1080 x 1350 (인스타 세로형 4:5)
- 결과: cover_ai_trend.png

실행: python make_cover.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ===== 설정 (여기만 바꿔서 재사용) =====
WIDTH, HEIGHT = 1080, 1350
TITLE = "AI 트렌드"
TAG = "CARD NEWS · 2026"
SUBTITLE = "지금 꼭 알아야 할\n인공지능 핵심 흐름 5가지"
HANDLE = "@my_ai_news"
OUTPUT = Path(__file__).parent / "cover_ai_trend.png"

BG_TOP = (18, 16, 54)        # 진한 남색
BG_BOTTOM = (76, 29, 149)    # 보라
ACCENT = (56, 232, 255)      # 시안
WHITE = (255, 255, 255)
GRAY = (200, 200, 230)

FONT_BOLD = "C:/Windows/Fonts/malgunbd.ttf"
FONT_REGULAR = "C:/Windows/Fonts/malgun.ttf"


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        print(f"[경고] 폰트를 찾을 수 없음: {path} → 기본 폰트 사용(한글 깨질 수 있음)")
        return ImageFont.load_default()


def vertical_gradient(w, h, top, bottom):
    """위→아래 그라데이션 배경"""
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / (h - 1)
        color = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(0, y), (w, y)], fill=color)
    return img


def add_glow_circles(img):
    """흐릿한 빛 번짐 원으로 분위기 연출"""
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    d.ellipse((620, -120, 1220, 480), fill=(56, 232, 255, 90))
    d.ellipse((-200, 900, 400, 1500), fill=(236, 72, 153, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    return Image.alpha_composite(img.convert("RGBA"), glow)


def add_grid(img, step=60):
    """테크 느낌의 옅은 격자 무늬"""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for x in range(0, img.width, step):
        d.line([(x, 0), (x, img.height)], fill=(255, 255, 255, 12))
    for y in range(0, img.height, step):
        d.line([(0, y), (img.width, y)], fill=(255, 255, 255, 12))
    return Image.alpha_composite(img, layer)


def main():
    img = vertical_gradient(WIDTH, HEIGHT, BG_TOP, BG_BOTTOM)
    img = add_glow_circles(img)
    img = add_grid(img)
    draw = ImageDraw.Draw(img)

    margin = 90

    # 상단 태그 (둥근 테두리 박스)
    tag_font = load_font(FONT_BOLD, 34)
    tb = draw.textbbox((0, 0), TAG, font=tag_font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    pad_x, pad_y = 28, 16
    box = (margin, 140, margin + tw + pad_x * 2, 140 + th + pad_y * 2)
    draw.rounded_rectangle(box, radius=40, outline=ACCENT, width=3)
    draw.text((margin + pad_x, 140 + pad_y - tb[1]), TAG, font=tag_font, fill=ACCENT)

    # 메인 제목 (그림자 + 본문)
    title_font = load_font(FONT_BOLD, 190)
    title_y = 470
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((margin + 8, title_y + 10), TITLE, font=title_font, fill=(0, 0, 0, 160))
    img = Image.alpha_composite(img, shadow.filter(ImageFilter.GaussianBlur(12)))
    draw = ImageDraw.Draw(img)
    draw.text((margin, title_y), TITLE, font=title_font, fill=WHITE)

    # 제목 아래 강조 바
    title_box = draw.textbbox((margin, title_y), TITLE, font=title_font)
    bar_y = title_box[3] + 40
    draw.rounded_rectangle((margin, bar_y, margin + 160, bar_y + 14), radius=7, fill=ACCENT)

    # 부제목
    sub_font = load_font(FONT_REGULAR, 56)
    draw.multiline_text((margin, bar_y + 60), SUBTITLE, font=sub_font, fill=GRAY, spacing=22)

    # 하단: 계정명 + 넘기기 안내
    foot_font = load_font(FONT_BOLD, 34)
    foot_y = HEIGHT - 130
    draw.line([(margin, foot_y - 40), (WIDTH - margin, foot_y - 40)], fill=(120, 100, 190), width=2)
    draw.text((margin, foot_y), HANDLE, font=foot_font, fill=WHITE)
    draw.text((WIDTH - margin, foot_y), "밀어서 보기  →", font=foot_font, fill=ACCENT, anchor="ra")

    img.convert("RGB").save(OUTPUT, quality=95)
    print(f"저장 완료: {OUTPUT}")


if __name__ == "__main__":
    main()
