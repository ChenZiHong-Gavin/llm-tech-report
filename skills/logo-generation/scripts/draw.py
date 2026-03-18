# gen_logo_v4_draw.py — drawing logic with analytical overlap avoidance
import matplotlib.pyplot as plt
import numpy as np


def estimate_text_width(name, fontsize, x_range, fig_w_inches):
    """Estimate text width in data coordinates."""
    # approx: each char ~ 0.6 * fontsize points wide
    # convert points -> inches -> data coords
    char_w_pts = fontsize * 0.55
    text_w_pts = len(name) * char_w_pts
    text_w_inches = text_w_pts / 72.0
    data_per_inch = x_range / fig_w_inches
    return text_w_inches * data_per_inch


def estimate_text_height(fontsize, y_range, fig_h_inches):
    """Estimate text height in data coordinates."""
    text_h_pts = fontsize * 1.2
    text_h_inches = text_h_pts / 72.0
    data_per_inch = y_range / fig_h_inches
    return text_h_inches * data_per_inch


def boxes_overlap(b1, b2):
    """b1, b2 = (cx, cy, half_w, half_h)"""
    return (abs(b1[0] - b2[0]) < (b1[2] + b2[2]) and
            abs(b1[1] - b2[1]) < (b1[3] + b2[3]))


def draw_logo(models, COLORS, LANDMARKS, OUTPUT, DPI, FIG_W, FIG_H,
              BG, TIMELINE, TICK_CLR, DIM, TEXT_CLR):

    x_min, x_max = 2016.5, 2026.8
    y_min, y_max = -3.5, 4.0
    x_range = x_max - x_min
    y_range = y_max - y_min

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.axis('off')

    # ── Timeline axis ──
    y_axis = 0.0
    for w, a in [(10, 0.015), (5, 0.04), (2.5, 0.07)]:
        ax.plot([x_min+0.2, x_max-0.2], [y_axis]*2,
                color="#58a6ff", lw=w, alpha=a, solid_capstyle='round', zorder=1)
    ax.plot([x_min+0.2, x_max-0.2], [y_axis]*2,
            color=TIMELINE, lw=2.5, solid_capstyle='round', zorder=2)
    ax.annotate('', xy=(x_max-0.1, y_axis), xytext=(x_max-0.4, y_axis),
                arrowprops=dict(arrowstyle='-|>', color=TICK_CLR, lw=2), zorder=2)

    for yr in range(2017, 2027):
        ax.plot([yr]*2, [y_axis-0.06, y_axis+0.06],
                color=TICK_CLR, lw=1.5, zorder=3)
        ax.text(yr, y_axis-0.20, str(yr), ha='center', va='top',
                fontsize=9, color=DIM, fontfamily='monospace', weight='bold', zorder=3)

    # ── Split above / below ──
    above = [m for i, m in enumerate(models) if i % 2 == 0]
    below = [m for i, m in enumerate(models) if i % 2 == 1]

    placed = []  # (cx, cy, half_w, half_h) in data coords

    def place_group(group, y_start, y_step):
        for x, name, company in group:
            color = COLORS.get(company, "#adb5bd")
            is_lm = name in LANDMARKS
            fs = 7.5 if is_lm else 5.8
            weight = 'heavy' if is_lm else 'bold'
            alpha = 1.0 if is_lm else 0.82

            hw = estimate_text_width(name, fs, x_range, FIG_W) / 2 + 0.02
            hh = estimate_text_height(fs, y_range, FIG_H) / 2 + 0.02

            # find first non-colliding y
            y = y_start
            for _ in range(30):
                box = (x, y, hw, hh)
                if not any(boxes_overlap(box, p) for p in placed):
                    break
                y += y_step
            else:
                y = y_start + 30 * y_step

            placed.append((x, y, hw, hh))

            # connector
            tip = y - y_step * 0.25
            ax.plot([x, x], [y_axis, tip], color=color, alpha=0.10, lw=0.4, zorder=1)
            # dot
            ax.scatter([x], [y_axis], s=5, color=color, alpha=0.45, zorder=4, edgecolors='none')
            # text
            ax.text(x, y, name, ha='center', va='center', fontsize=fs,
                    fontfamily='sans-serif', weight=weight, color=color,
                    alpha=alpha, zorder=6)

    place_group(above, y_start=0.32, y_step=0.24)
    place_group(below, y_start=-0.32, y_step=-0.24)

    # ── Title ──
    ax.text(x_min+0.1, y_max-0.15, "LLM Technical Reports",
            fontsize=24, fontweight='heavy', color=TEXT_CLR,
            fontfamily='sans-serif', ha='left', va='top', zorder=10)
    ax.text(x_min+0.1, y_max-0.60, "150+ reports from 30+ labs  |  2017-2026",
            fontsize=9, color=DIM, fontfamily='monospace',
            ha='left', va='top', zorder=10)

    # ── Legend ──
    legend = ["OpenAI","Google","Anthropic","Meta","DeepSeek","Qwen",
              "Mistral","Microsoft","xAI","Zhipu","ByteDance","Baidu",
              "InternLM","Moonshot","Tencent","MiniMax"]
    cols = 8
    lx0 = x_max - 4.5
    ly0 = y_max - 0.15
    for i, c in enumerate(legend):
        col, row = i % cols, i // cols
        lx = lx0 + col * 0.56
        ly = ly0 - row * 0.28
        ax.scatter([lx-0.05], [ly], s=12, color=COLORS[c], edgecolors='none', zorder=10)
        ax.text(lx, ly, c, fontsize=5, color=COLORS[c],
                fontfamily='sans-serif', va='center', ha='left', alpha=0.8, zorder=10)

    # ── Tagline ──
    ax.text(x_max-0.15, y_min+0.15,
            "curated  |  chronological  |  comprehensive",
            fontsize=6.5, color=DIM, fontfamily='monospace',
            ha='right', va='bottom', zorder=10)

    plt.tight_layout(pad=0.1)
    fig.savefig(OUTPUT, dpi=DPI, facecolor=BG, edgecolor='none',
                bbox_inches='tight', pad_inches=0.15)
    plt.close()
    print("Logo v4 saved to", OUTPUT)
    sz = OUTPUT.stat().st_size
    print("Size:", round(sz/1024), "KB")
    print("Models:", len(models))
