"""
LLM Technical Reports - Timeline Logo Generator
Run: python skills/logo-generation/scripts/generate.py
Output: logo.png in repo root
"""
import sys
from pathlib import Path

# ensure repo root importable
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use('Agg')

OUTPUT = REPO_ROOT / "logo.png"
DPI = 300
FIG_W, FIG_H = 20, 8

BG = "#0d1117"
TIMELINE = "#21262d"
TICK_CLR = "#484f58"
DIM = "#6e7681"
TEXT_CLR = "#e6edf3"

COLORS = {
    "OpenAI":"#74b9ff","Google":"#ffeaa7","Anthropic":"#dfe6e9",
    "Meta":"#55efc4","DeepSeek":"#81ecec","Qwen":"#fd79a8",
    "InternLM":"#a29bfe","ByteDance":"#00cec9","Zhipu":"#e17055",
    "Moonshot":"#fdcb6e","Baidu":"#6c5ce7","Tencent":"#00b894",
    "MiniMax":"#e84393","Mistral":"#fab1a0","xAI":"#b0b0b0",
    "Microsoft":"#0984e3","Amazon":"#ff7675","Nvidia":"#a3cb38",
    "AI21":"#12CBC4","Databricks":"#ED4C67","TII":"#B53471",
    "Reka":"#9980FA","Cohere":"#FFC312","Apple":"#b2bec3",
    "Baichuan":"#e056fd","01.AI":"#7ed6df","Meituan":"#f9ca24",
    "StepFun":"#22a6b3","InclusionAI":"#5758BB","Xiaomi":"#ff6348",
    "Zhijiang":"#7158e2",
}

LANDMARKS = {
    "Transformer","GPT-3","GPT-4","GPT-4o","GPT-5",
    "Claude 3","Claude 4","LLaMA","Llama 2","Llama 3","Llama 4",
    "Gemini 1.0","Gemini 1.5","Gemini 2.5",
    "DS-V3","DS-R1","Qwen2.5","Qwen3","Grok-3","Mistral 7B","BERT",
}

from models import MODELS
from draw import draw_logo

draw_logo(MODELS, COLORS, LANDMARKS, OUTPUT, DPI, FIG_W, FIG_H,
          BG, TIMELINE, TICK_CLR, DIM, TEXT_CLR)
