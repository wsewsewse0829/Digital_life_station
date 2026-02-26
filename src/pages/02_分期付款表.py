"""
分期付款表页面
Installment Payment Page
"""

import streamlit as st

# 页面配置
st.set_page_config(
    page_title="分期付款表 - Digital Life Station",
    page_icon="💳",
    layout="wide"
)

st.title("💳 分期付款表")
st.markdown("---")

st.info("🚧 此功能正在开发中，敬请期待！")

st.markdown("""
**计划功能：**
- 输入分期付款计划表
- 显示年化利率
- 可勾稽至资产负债表和损益表
- 可选择提前还款
- 备注功能
""")