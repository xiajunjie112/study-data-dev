学习工作区 — 数据开发 / Python / 实时数据

目标
- 针对“中级”学习者（熟悉 Python 基础与数据处理），系统学习数据工程与实时数据处理的核心技能。
- 通过小型实战项目（端到端实时数据流水线）将理论与实操结合。

初始待办（已加入 session 待办列表）
- 设置 Python 环境（虚拟环境 & 依赖）
- 复习中级 Python（typing、async、生成器、上下文管理）
- 批处理数据（pandas、Parquet、SQLAlchemy）
- 流处理基础（Kafka 概念、生产者/消费者、语义）
- Python 流处理实践（kafka-python + streamz / Apache Beam）
- 编排（Prefect 入门）
- 小项目：实时数据管道（Kafka -> 流处理 -> 存储 -> API）
- 配置 JupyterLab
- 收集学习资源（文档、课程、书籍）

快速开始
1) 在项目根创建并激活虚拟环境（Windows PowerShell）
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2) 安装依赖
   pip install -r requirements.txt

3) 启动 JupyterLab
   jupyter lab

4) 推荐的学习顺序
   - 环境与 Python 复习 -> 批处理数据练习 -> Kafka 基础 -> 小型流处理实验 -> 编排与项目整合

后续
- 如果你同意这套路线，我会：
  1) 帮你生成示例 notebook 和示例代码目录结构
  2) 提供每个待办的细化学习任务与资源链接
  3) 如果需要，生成 Docker-compose 用于本地 Kafka 与 Postgres 环境

如果有偏好（比如想用 Airflow 替代 Prefect，或想优先学习 Spark Structured Streaming），请告诉我。
