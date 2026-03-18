# Skill: Logo Generation (Timeline)

为 `llm-tech-report` 仓库生成时间轴 logo。所有模型名按发布时间堆叠在横轴上下，自动避免文字重叠。

## 文件结构

```
skills/logo-generation/
├── SKILL.md                  # 本文件
└── scripts/
    ├── generate.py           # 入口：配置 + 调用
    ├── models.py             # 数据：所有 (year, name, company) 条目
    └── draw.py               # 绘图：时间轴 + 防重叠算法
```

输出：仓库根目录 `logo.png`

## 依赖

```
pip install matplotlib numpy
```

## 使用

```bash
cd D:\Project\info\llm-tech-report
python skills/logo-generation/scripts/generate.py
```

输出 `logo.png`（约 400KB，20x8 英寸，300 DPI）。

## 如何更新

### 新增模型

编辑 `scripts/models.py`，在 `MODELS` 列表中添加：

```python
(2025.50, "ModelName", "CompanyKey"),
```

- **year**：`YYYY + MM/12`（如 2025-06 = `2025.50`）
- **name**：尽量简短（`DS-R1` 而非 `DeepSeek-R1`）
- **company**：必须在 `generate.py` 的 `COLORS` 中存在

无需手动排序，脚本自动按时间排。

### 新增公司

1. `generate.py` 的 `COLORS` 字典添加 `"NewCo": "#hex"`
2. `draw.py` 的 `legend` 列表添加公司名（如需图例显示）

### 调整里程碑

`generate.py` 的 `LANDMARKS` 集合增减即可。里程碑字号 7.5pt，普通 5.8pt。

## 防重叠算法

- **纯数据坐标估算**，不调用 renderer，秒级完成
- 文字宽 = `字符数 x 字号 x 0.55 / 72 x (x_range / fig_w)`
- 文字高 = `字号 x 1.2 / 72 x (y_range / fig_h)`
- 奇偶交替分配轴上/下，碰撞则逐层外推（步长 0.24），最多 30 层

## 注意事项

1. **名称要短**——长名字挤占横向空间，缩写优先
2. **2023-2025 最拥挤**——新增模型可微调 year 小数避免扎堆
3. **模型超 ~150 个**——需加大 `FIG_H` 或减小 `y_step`
4. **暗色背景**——避免用太深的颜色（纯黑、深灰）
5. **每次改数据后重跑**——肉眼确认无溢出
