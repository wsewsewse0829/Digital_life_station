# 个人财务规划应用技术设计

## 技术栈
- 后端/功能层：Python
- 前段/交互层：Streamlit
- 数据处理：Pandas/Numpy
- 存储方式：csv文件
- 可视化：Matplotlib/Plotly
- 文档管理：Markdown
- 云端部署：Steamlit Cloud

## 项目结构

src/
  components/  #组建
  pages/       #页面
  hooks/       #自定义Hooks
  utils/       #工具函数
  types/       #类型定义

## 数据模型

### 科目表(Subject)
- account_id:string  #科目唯一编号
- account_name:string  #科目名称
- category: 'asset'|'liability'|'net_asset'|'income'|'expense'|'net_income'  #所属类表，录入时用户自行选择
- note:string

### 月度数据录入表(Entry)
- subject_account_id:string  # 指向科目表 account_id
- month:date                 # 格式：YYYY-MM
- amount：number             # 金额
- type：'actual'|'estimate'  # 类型，选择是否为预测数据
