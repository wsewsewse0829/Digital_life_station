"""
个人财务规划应用
Digital Life Station - Personal Financial Planning Application
"""

import streamlit as st
import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.utils import ensure_data_dir

# 页面配置
st.set_page_config(
    page_title="Digital Life Station - 个人财务规划",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化数据目录
ensure_data_dir()

# 主页面
st.title("💰 Digital Life Station")
st.markdown("---")
st.markdown("### 欢迎使用个人财务规划应用")

st.markdown("""
本应用采用企业财务管理的思维帮助您进行个人财务规划。

**核心功能：**
- 📊 资产负债表和损益表管理
- 📈 数据可视化分析
- 💾 数据本地存储（CSV格式）

**导航说明：**
- 使用左侧边栏切换不同页面
- 数据存储在本地 data 目录中

开始使用，请从左侧选择功能页面。
""")

st.info("📌 提示：首次使用请先在「资产负债表/损益表」页面创建科目。")