"""Type definitions for the financial planning application"""

from typing import Literal
from datetime import datetime

class Subject:
    """科目表数据模型"""
    def __init__(
        self,
        account_id: str,
        account_name: str,
        category: Literal['asset', 'liability', 'net_asset', 'income', 'expense', 'net_income'],
        note: str = ""
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.category = category
        self.note = note

class Entry:
    """月度数据录入表数据模型"""
    def __init__(
        self,
        subject_account_id: str,
        month: str,  # 格式：YYYY-MM
        amount: float,
        entry_type: Literal['actual', 'estimate'] = 'actual',
        note: str = ""
    ):
        self.subject_account_id = subject_account_id
        self.month = month
        self.amount = amount
        self.entry_type = entry_type
        self.note = note