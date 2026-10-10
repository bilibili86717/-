# -*- coding: utf-8 -*-
"""生成辽河能碳管理系统 PWA 图标（工业风）"""
from PIL import Image, ImageDraw

BG = (15, 23, 42, 255)          # #0f172a 深蓝
ORANGE = (249, 115, 22, 255)    # #f97316 橙色（电力）
GREEN = (34, 197, 94, 255)      # #22c55e 绿色（绿电/碳中和）

# 闪电多边形（归一化坐标，中心对齐）
LIGHTNING = [
    (0.60, 0.14), (0.36, 0.52), (0.52, 0.52),
    (0.43, 0.86), (0.70, 0.45), (0.54, 0.45), (0.66, 0.14)
]


def draw_icon(size, maskable=False):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    if maskable:
        # 铺满全屏（安全区为中央 80%）
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=0, fill=BG)
        cx0, cy0, cx1, cy1 = size * 0.1, size * 0.1, size * 0.9, size * 0.9
    else:
        # 居中圆角矩形，留出边距
        pad = int(size * 0.06)
        radius = int(size * 0.20)
        d.rounded_rectangle([pad, pad, size - 1 - pad, size - 1 - pad],
                            radius=radius, fill=BG)
        cx0, cy0, cx1, cy1 = pad, pad, size - 1 - pad, size - 1 - pad

    w = cx1 - cx0
    h = cy1 - cy0

    # 绿色弧线（底部半圆环，代表绿电/碳中和）
    arc_w = int(size * 0.045)
    ax0 = cx0 + w * 0.20
    ay0 = cy0 + h * 0.62
    ax1 = cx0 + w * 0.80
    ay1 = cy0 + h * 0.98
    d.arc([ax0, ay0, ax1, ay1], start=0, end=180, fill=GREEN, width=arc_w)

    # 橙色闪电（主视觉，居中偏上）
    pts = [(cx0 + w * x, cy0 + h * y) for x, y in LIGHTNING]
    d.polygon(pts, fill=ORANGE)

    return img


for size in (192, 512):
    draw_icon(size, maskable=False).save(f'icons/icon-{size}.png')
    draw_icon(size, maskable=True).save(f'icons/icon-maskable-{size}.png')

print('图标生成完成')
import os
for f in sorted(os.listdir('icons')):
    print(' ', f, os.path.getsize(f'icons/{f}'), 'bytes')
