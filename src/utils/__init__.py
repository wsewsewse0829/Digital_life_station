"""Utility functions for data management"""

import pandas as pd
import os
from typing import List

# 数据文件路径
DATA_DIR = "data"
SUBJECTS_FILE = os.path.join(DATA_DIR, "subjects.csv")
ENTRIES_FILE = os.path.join(DATA_DIR, "entries.csv")

def ensure_data_dir():
    """确保数据目录存在"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # 如果文件不存在，创建空文件
    if not os.path.exists(SUBJECTS_FILE):
        pd.DataFrame(columns=['account_id', 'account_name', 'category', 'note']).to_csv(SUBJECTS_FILE, index=False)
    
    if not os.path.exists(ENTRIES_FILE):
        pd.DataFrame(columns=['subject_account_id', 'month', 'amount', 'entry_type', 'note']).to_csv(ENTRIES_FILE, index=False)

def load_subjects() -> pd.DataFrame:
    """加载科目数据"""
    ensure_data_dir()
    return pd.read_csv(SUBJECTS_FILE)

def save_subjects(df: pd.DataFrame):
    """保存科目数据"""
    ensure_data_dir()
    df.to_csv(SUBJECTS_FILE, index=False)

def load_entries() -> pd.DataFrame:
    """加载条目数据"""
    ensure_data_dir()
    return pd.read_csv(ENTRIES_FILE)

def save_entries(df: pd.DataFrame):
    """保存条目数据"""
    ensure_data_dir()
    df.to_csv(ENTRIES_FILE, index=False)

def get_categories() -> List[str]:
    """获取所有科目类别"""
    return ['asset', 'liability', 'net_asset', 'income', 'expense', 'net_income']

def get_category_display_names() -> dict:
    """获取类别显示名称映射"""
    return {
        'asset': '资产',
        'liability': '负债',
        'net_asset': '净资产',
        'income': '收入',
        'expense': '支出',
        'net_income': '净利润'
    }