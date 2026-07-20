# 学习工作区 — Python / 数据分析 & 数据开发

> 学习路线分为两大方向，**数据分析学习**为第一优先级。

---

## 📊 一、数据分析学习（第一优先）

系统掌握数据分析全流程：数据获取 → 清洗 → 探索分析 → 可视化 → 报告输出。

### 待办清单

- [x] **Python 基础语法**（已生成学习材料 → `python_basics/`）
  - 10 个 .py 文件，覆盖变量、字符串、容器、控制流、函数、文件、异常、推导式、模块
- [ ] **Python 数据分析进阶**
  - NumPy：数组操作、广播机制、线性代数
  - pandas：DataFrame 操作、分组聚合、缺失值处理
  - 数据可视化：Matplotlib / Seaborn / Plotly
- [ ] **SQL 数据分析**
  - 复杂查询（窗口函数、CTE、子查询）
  - 数据清洗与预处理
- [ ] **统计分析基础**
  - 描述性统计、假设检验、相关性分析
- [ ] **实战项目：探索性数据分析（EDA）**
  - 从 Kaggle / 公开数据集获取数据，完成完整 EDA 报告
- [ ] **配置 JupyterLab 环境**

### 工具栈

| 类别 | 工具 |
|------|------|
| 数据处理 | pandas, NumPy |
| 可视化 | Matplotlib, Seaborn, Plotly |
| 数据库 | PostgreSQL, SQLite |
| 环境 | JupyterLab, VS Code |

---

## ⚙️ 二、数据开发学习（后续跟进）

在数据分析基础扎实后，进入数据工程与实时数据处理方向。

### 待办清单

- [ ] **Python 进阶复习**
  - typing、async/await、生成器、上下文管理
- [ ] **批处理数据处理**
  - pandas 进阶、Parquet 格式、SQLAlchemy
- [ ] **流处理基础**
  - Kafka 概念、生产者/消费者模型、消费语义
- [ ] **Python 流处理实践**
  - kafka-python + streamz / Apache Beam
- [ ] **工作流编排**
  - Prefect 入门（或 Airflow）
- [ ] **实战项目：端到端实时数据管道**
  - Kafka → 流处理 → 存储 → API 输出

### 工具栈

| 类别 | 工具 |
|------|------|
| 消息队列 | Kafka |
| 流处理 | streamz, Apache Beam, Spark Structured Streaming |
| 编排 | Prefect / Airflow |
| 存储 | PostgreSQL, Parquet |

---

## 🚀 快速开始

### 1) 创建并激活虚拟环境（Windows PowerShell）

```powershell
python -m venv .venv
.\\.venv\Scripts\Activate.ps1
```

### 2) 安装依赖

```bash
pip install -r requirements.txt
```

### 3) 启动 JupyterLab

```bash
jupyter lab
```

---

## 📌 推荐学习路线

```
第一阶段（数据分析）: Python 基础复习 → NumPy/pandas → 数据可视化 → SQL → 统计基础 → EDA 实战项目
        ↓
第二阶段（数据开发）: Python 进阶 → 批处理 → Kafka → 流处理 → 工作流编排 → 实时数据管道项目
```

---

## 📚 学习资源

_待补充：文档、课程、书籍推荐_

---

如果有偏好或想调整方向，欢迎随时告诉我。
