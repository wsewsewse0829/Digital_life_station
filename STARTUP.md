# Digital Life Station - 启动指南

## 项目简介
Digital Life Station 是一个基于 Streamlit 的个人财务规划应用，采用企业财务管理的思维帮助您进行个人财务规划。

## 技术栈
- Python 3.13+
- Streamlit 1.31.0
- Pandas 2.2.0
- NumPy 1.26.4
- Matplotlib 3.8.3
- Plotly 5.18.0

## 安装依赖

首次运行前，请确保已安装所有依赖：

```bash
pip install -r requirements.txt
```

## 启动应用

在项目根目录下运行：

```bash
streamlit run app.py
```

或者：

```bash
python -m streamlit run app.py
```

## 项目结构

```
Digital_life_station/
├── app.py                          # 主应用入口
├── requirements.txt                # Python 依赖
├── .streamlit/                     # Streamlit 配置
│   └── config.toml
├── src/                            # 源代码目录
│   ├── components/                 # 组件（待开发）
│   ├── pages/                      # 页面
│   │   ├── 01_财务报表.py
│   │   ├── 02_分期付款表.py
│   │   └── 03_理财组合管理表.py
│   ├── hooks/                      # 自定义 Hooks（待开发）
│   ├── utils/                      # 工具函数
│   │   └── __init__.py
│   └── types/                      # 类型定义
│       └── __init__.py
└── data/                           # 数据存储目录（自动创建）
    ├── subjects.csv                # 科目表数据
    └── entries.csv                 # 条目数据
```

## 功能说明

### 当前可用功能
1. **财务报表管理**（页面1）
   - 科目管理：创建、查看、删除财务科目
   - 数据录入：录入月度财务数据
   - 支持实际/预测两种数据类型

### 待开发功能
2. **分期付款表**（页面2）- 开发中
3. **理财组合管理表**（页面3）- 开发中

## 数据存储

所有数据存储在 `data/` 目录下的 CSV 文件中：
- `subjects.csv` - 科目表数据
- `entries.csv` - 月度数据录入

首次运行时，应用会自动创建这些文件。

## 使用说明

1. 启动应用后，浏览器会自动打开 `http://localhost:8501`
2. 首次使用请先在「财务报表」页面的「科目管理」标签中创建科目
3. 然后在「数据录入」标签中录入财务数据
4. 使用左侧导航栏切换不同页面

## 注意事项

- 确保使用 Python 3.13 或更高版本
- 数据文件保存在本地，请定期备份
- 建议使用虚拟环境进行开发

## 故障排除

### 端口被占用
如果 8501 端口被占用，可以指定其他端口：
```bash
streamlit run app.py --server.port 8502
```

### 依赖安装失败
如果依赖安装失败，尝试使用国内镜像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 开发计划

- [ ] 完善财务报表的勾稽关系
- [ ] 添加数据可视化图表
- [ ] 实现分期付款表功能
- [ ] 实现理财组合管理表功能
- [ ] 添加数据导出功能
- [ ] 添加用户认证和多账户管理