from PIL import Image, ImageDraw, ImageFont
import os

# 输出目录
out_dir = r"F:\04_数据存储\obsidian存储\kai\quiz_images"
os.makedirs(out_dir, exist_ok=True)

# 字体
font_path = "msyh.ttc"
title_font = ImageFont.truetype(font_path, 40)
subtitle_font = ImageFont.truetype(font_path, 30)
body_font = ImageFont.truetype(font_path, 26)
small_font = ImageFont.truetype(font_path, 22)

# 颜色
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (120, 120, 120)
LINE_COLOR = (200, 200, 200)
ACCENT = (60, 120, 200)

# 页面设置
PAGE_W = 1200
MARGIN = 80
LINE_GAP = 55

def create_image(title, lines, filename, subtitle=None):
    """生成测试图片"""
    # 计算高度
    h = MARGIN + 60 + 20  # 标题
    if subtitle:
        h += 45
    h += 30  # 分割线间距
    for line in lines:
        if line == "---":
            h += 30
        elif line.startswith("词库"):
            h += 45
        else:
            h += LINE_GAP
    h += MARGIN + 40  # 底部留白

    img = Image.new("RGB", (PAGE_W, h), WHITE)
    draw = ImageDraw.Draw(img)

    y = MARGIN

    # 标题
    draw.text((MARGIN, y), title, font=title_font, fill=ACCENT)
    y += 60

    if subtitle:
        draw.text((MARGIN, y), subtitle, font=small_font, fill=GRAY)
        y += 45

    # 分割线
    y += 10
    draw.line([(MARGIN, y), (PAGE_W - MARGIN, y)], fill=LINE_COLOR, width=2)
    y += 25

    # 内容
    for line in lines:
        if line == "---":
            y += 5
            draw.line([(MARGIN, y), (PAGE_W - MARGIN, y)], fill=LINE_COLOR, width=1)
            y += 25
        elif line.startswith("词库"):
            draw.text((MARGIN, y), line, font=small_font, fill=GRAY)
            y += LINE_GAP
        else:
            draw.text((MARGIN, y), line, font=body_font, fill=BLACK)
            y += LINE_GAP

    img.save(os.path.join(out_dir, filename), quality=95)
    print(f"[OK] {filename} ({img.size[0]}x{img.size[1]})")

# ========== 题型一：英译中 ==========
create_image(
    "一、英译中",
    [
        "写出下列单词的中文释义：",
        "---",
        "1.  advance  →  _________________________",
        "2.  agent  →  _________________________",
        "3.  ambiguous  →  _________________________",
        "4.  alter  →  _________________________",
        "5.  amateur  →  _________________________",
        "6.  annual  →  _________________________",
        "7.  anxiety  →  _________________________",
        "8.  adapt  →  _________________________",
        "9.  abandon  →  _________________________",
        "10. bias  →  _________________________",
        "11. candidate  →  _________________________",
        "12. capital  →  _________________________",
        "13. transaction  →  _________________________",
        "14. automation  →  _________________________",
        "15. debate  →  _________________________",
    ],
    "01_英译中.png",
    subtitle="List 1 · 闪过单词"
)

# ========== 题型二：中译英 ==========
create_image(
    "二、中译英",
    [
        "根据中文写出对应英文单词：",
        "---",
        "1.  实际的；真实的  →  _________________________",
        "2.  相互作用；互动  →  _________________________",
        "3.  平行的  →  _________________________",
        "4.  古代的；古老的  →  _________________________",
        "5.  焦虑的；渴望的  →  _________________________",
        "6.  战斗；斗争  →  _________________________",
        "7.  结合；联合  →  _________________________",
        "8.  简短的  →  _________________________",
        "9.  癌症  →  _________________________",
        "10. 职业；生涯  →  _________________________",
        "11. 携带；运送  →  _________________________",
        "12. 先进的；高级的  →  _________________________",
        "13. 代理人；特工  →  _________________________",
        "14. 替代选择  →  _________________________",
        "15. 前进；进步  →  _________________________",
    ],
    "02_中译英.png",
    subtitle="List 1 · 闪过单词"
)

# ========== 题型三：选词填空 ==========
create_image(
    "三、选词填空",
    [
        "从词库中选择合适的单词填入空格：",
        "词库：advance / agent / actual / react / interact / ambiguous / alter",
        "      alternative / ancient / annual / anxiety / adapt / abandon / debate",
        "      bias / combine / brief / candidate / capital / carry",
        "---",
        "1.  The company decided to ________ its marketing strategy.",
        "",
        "2.  The instructions were so ________ that no one understood them.",
        "",
        "3.  She has been working hard to ________ to the new environment.",
        "",
        "4.  The government plans to ________ the two departments into one.",
        "",
        "5.  He had to ________ his plan due to a lack of funding.",
        "",
        "6.  The ________ cost was much higher than expected.",
        "",
        "7.  The ________ meeting will be held next Monday.",
        "",
        "8.  She is a strong ________ for the position of CEO.",
        "",
        "9.  People tend to ________ differently under pressure.",
        "",
        "10. The discovery of ________ artifacts attracted researchers.",
        "",
        "11. There is a growing ________ about the impact of AI.",
        "",
        "12. He wants to build a ________ in software engineering.",
        "",
        "13. A real estate ________ helped them find their dream home.",
        "",
        "14. The report should be ________ and to the point.",
        "",
        "15. The research shows a clear ________ against younger applicants.",
        "",
        "16. Beijing is the ________ of China.",
        "",
        "17. Children learn to ________ with each other through play.",
        "",
        "18. Please ________ this package to the post office.",
        "",
        "19. She felt a deep sense of ________ before the final exam.",
        "",
        "20. ________ emissions are a major contributor to global warming.",
    ],
    "03_选词填空.png",
    subtitle="List 1 · 闪过单词"
)

# ========== 题型四：词义辨析 ==========
create_image(
    "四、词义辨析",
    [
        "选择正确的单词填空（每题只有一个正确答案）：",
        "---",
        "1. The two roads run ________ to each other for miles.",
        "",
        "   A. parallel     B. ambiguous     C. actual     D. annual",
        "",
        "",
        "2. The government is encouraging ________ in manufacturing.",
        "",
        "   A. anxiety     B. automation     C. bias     D. debate",
        "",
        "",
        "3. We need to find an ________ energy source to replace fossil fuels.",
        "",
        "   A. ancient     B. advanced     C. alternative     D. amateur",
        "",
        "",
        "4. The professor asked the students to ________ the novel into a play.",
        "",
        "   A. adapt     B. alter     C. advance     D. abandon",
        "",
        "",
        "5. The ________ between the two companies was completed last week.",
        "",
        "   A. battle     B. debate     C. transaction     D. career",
    ],
    "04_词义辨析.png",
    subtitle="List 1 · 闪过单词"
)

# ========== 题型五：完形填空 ==========
create_image(
    "五、完形填空",
    [
        "在空格处填入最合适的单词（每空一词，限用 List 1 词表）：",
        "---",
        "Technology is advancing at an unprecedented pace. Companies must",
        "constantly (1)________ their strategies to stay competitive. The",
        "rise of (2)________ has transformed manufacturing, reducing the",
        "need for manual labor. However, this shift creates (3)________",
        "among workers who fear losing their jobs.",
        "",
        "Some argue that technology creates new opportunities, while",
        "others (4)________ this view, claiming it deepens inequality.",
        "The (5)________ remains unresolved. What is clear is that",
        "professionals must (6)________ to new technologies throughout",
        "their (7)________. Those who (8)________ this challenge risk",
        "being left behind.",
        "",
        "In this context, education plays a (9)________ role. Universities",
        "must equip students with skills that are relevant to the",
        "(10)________ job market, not just theoretical knowledge.",
        "",
        "---",
        "(1)________    (2)________    (3)________    (4)________    (5)________",
        "",
        "(6)________    (7)________    (8)________    (9)________    (10)________",
    ],
    "05_完形填空.png",
    subtitle="List 1 · 闪过单词"
)

# ========== 题型六：翻译 ==========
create_image(
    "六、英译中翻译",
    [
        "将下列句子翻译成中文：",
        "---",
        "1. The actual cost of the project exceeded our budget by 30%.",
        "",
        "_______________________________________________________",
        "",
        "_______________________________________________________",
        "",
        "",
        "2. It is important to adapt to new environments quickly in",
        "   today's fast-changing world.",
        "",
        "_______________________________________________________",
        "",
        "_______________________________________________________",
        "",
        "",
        "3. The candidate's ambiguous response raised doubts among",
        "   the interviewers.",
        "",
        "_______________________________________________________",
        "",
        "_______________________________________________________",
        "",
        "",
        "4. Carbon emissions have become a central topic in global",
        "   climate debate.",
        "",
        "_______________________________________________________",
        "",
        "_______________________________________________________",
        "",
        "",
        "5. She decided to abandon her original plan and pursue a",
        "   completely different career.",
        "",
        "_______________________________________________________",
        "",
        "_______________________________________________________",
    ],
    "06_翻译.png",
    subtitle="List 1 · 闪过单词"
)

# ========== 题型七：同根词拓展 ==========
create_image(
    "七、同根词拓展",
    [
        "写出下列单词的派生词：",
        "---",
        "1. advance（前进；进步）",
        "   名词形式：_________________________",
        "   形容词形式：_________________________",
        "   反义词/相关词：_________________________",
        "",
        "",
        "2. anxious（焦虑的）",
        "   名词形式：_________________________",
        "   反义词/相关词：_________________________",
        "",
        "",
        "3. alter（改变）",
        "   名词形式：_________________________",
        "   形容词形式：_________________________",
        "",
        "",
        "4. adapt（适应）",
        "   名词形式：_________________________",
        "   形容词形式：_________________________",
        "",
        "",
        "5. combine（结合）",
        "   名词形式：_________________________",
        "   形容词形式：_________________________",
    ],
    "07_同根词拓展.png",
    subtitle="List 1 · 闪过单词"
)

print(f"\nDone! 7 images saved to: {out_dir}")
