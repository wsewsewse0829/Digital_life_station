"""
资产负债表和损益表页面
Balance Sheet and Income Statement Page
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_subjects, save_subjects, load_entries, save_entries, get_categories, get_category_display_names

# 页面配置
st.set_page_config(
    page_title="财务报表 - Digital Life Station",
    page_icon="📊",
    layout="wide"
)

st.title("📊 资产负债表和损益表")
st.markdown("---")

# 创建标签页
tab1, tab2 = st.tabs(["科目管理", "数据录入"])

# ============ 科目管理 ============
with tab1:
    st.subheader("📝 科目管理")
    
    # 加载科目数据
    subjects_df = load_subjects()
    
    # 显示现有科目
    if not subjects_df.empty:
        st.write("**现有科目列表：**")
        display_df = subjects_df.copy()
        display_df['category'] = display_df['category'].map(get_category_display_names())
        st.dataframe(display_df, use_container_width=True)
    else:
        st.info("暂无科目，请添加新科目。")
    
    # 添加科目表单
    st.markdown("#### ➕ 添加新科目")
    with st.form("add_subject_form"):
        col1, col2, col3 = st.columns([2, 2, 2])
        
        with col1:
            account_id = st.text_input("科目编号 *", help="唯一的科目编号，如：1001, 2001")
        
        with col2:
            account_name = st.text_input("科目名称 *", help="科目名称，如：现金、银行存款")
        
        with col3:
            category = st.selectbox("科目类别 *", get_categories(), 
                                   format_func=lambda x: get_category_display_names()[x])
        
        note = st.text_area("备注", placeholder="可选，添加备注信息...")
        
        col_submit, col_clear = st.columns([1, 4])
        with col_submit:
            submitted = st.form_submit_button("添加科目", type="primary")
        
        if submitted:
            if not account_id or not account_name:
                st.error("科目编号和科目名称为必填项！")
            elif account_id in subjects_df['account_id'].values:
                st.error("该科目编号已存在！")
            else:
                new_subject = pd.DataFrame([{
                    'account_id': account_id,
                    'account_name': account_name,
                    'category': category,
                    'note': note
                }])
                subjects_df = pd.concat([subjects_df, new_subject], ignore_index=True)
                save_subjects(subjects_df)
                st.success(f"科目「{account_name}」添加成功！")
                st.rerun()
    
    # 删除科目
    if not subjects_df.empty:
        st.markdown("#### 🗑️ 删除科目")
        subject_to_delete = st.selectbox(
            "选择要删除的科目",
            options=subjects_df['account_id'].tolist(),
            format_func=lambda x: f"{x} - {subjects_df[subjects_df['account_id'] == x]['account_name'].values[0]}"
        )
        
        if st.button("删除选中科目", type="secondary"):
            subjects_df = subjects_df[subjects_df['account_id'] != subject_to_delete]
            save_subjects(subjects_df)
            st.success("科目删除成功！")
            st.rerun()

# ============ 数据录入 ============
with tab2:
    st.subheader("💰 数据录入")
    
    # 加载科目和条目数据
    subjects_df = load_subjects()
    entries_df = load_entries()
    
    if subjects_df.empty:
        st.warning("请先在「科目管理」标签页中创建科目。")
    else:
        # 显示现有数据
        if not entries_df.empty:
            st.write("**现有数据记录：**")
            display_entries = entries_df.merge(
                subjects_df[['account_id', 'account_name', 'category']],
                left_on='subject_account_id',
                right_on='account_id',
                how='left'
            )
            display_entries['category'] = display_entries['category'].map(get_category_display_names())
            display_entries['entry_type'] = display_entries['entry_type'].map({
                'actual': '实际',
                'estimate': '预测'
            })
            display_entries = display_entries[['account_name', 'category', 'month', 'amount', 'entry_type', 'note']]
            display_entries.columns = ['科目名称', '科目类别', '月份', '金额', '类型', '备注']
            st.dataframe(display_entries, use_container_width=True)
        else:
            st.info("暂无数据记录。")
        
        # 添加数据表单
        st.markdown("#### ➕ 添加数据记录")
        with st.form("add_entry_form"):
            col1, col2 = st.columns([2, 2])
            
            with col1:
                subject_options = subjects_df['account_id'].tolist()
                subject_display = [f"{x} - {subjects_df[subjects_df['account_id'] == x]['account_name'].values[0]}" 
                                  for x in subject_options]
                
                selected_subject_display = st.selectbox("选择科目 *", subject_display)
                subject_account_id = subject_options[subject_display.index(selected_subject_display)]
            
            with col2:
                month = st.date_input("会计期间 *", value=datetime.now(), 
                                     format="YYYY-MM", key="entry_month")
                month_str = month.strftime("%Y-%m")
            
            col3, col4 = st.columns([2, 2])
            
            with col3:
                amount = st.number_input("金额 *", min_value=0.0, step=100.0, value=0.0)
            
            with col4:
                entry_type = st.selectbox("类型", ['actual', 'estimate'], 
                                        format_func=lambda x: '实际' if x == 'actual' else '预测')
            
            note = st.text_area("备注", placeholder="可选，添加备注信息...")
            
            col_submit, col_clear = st.columns([1, 4])
            with col_submit:
                submitted = st.form_submit_button("添加记录", type="primary")
            
            if submitted:
                if amount == 0:
                    st.error("金额不能为0！")
                else:
                    new_entry = pd.DataFrame([{
                        'subject_account_id': subject_account_id,
                        'month': month_str,
                        'amount': amount,
                        'entry_type': entry_type,
                        'note': note
                    }])
                    entries_df = pd.concat([entries_df, new_entry], ignore_index=True)
                    save_entries(entries_df)
                    st.success("数据记录添加成功！")
                    st.rerun()