# Research Agent Workspace

目标：把 Jupyter 作为“人的研究界面”，Trae Agent 作为“受约束的执行器”，
Git 作为审计记录，tests/specs 作为护栏，SSH 作为远程计算通道。

## 目录约定

- `theory/`：你的手推公式、定义、假设。默认由人维护。
- `specs/`：实验规格与验收标准。默认由人维护。
- `notebooks/`：Jupyter/Jupytext 实验记录。
- `src/`：正式算法代码。
- `tests/`：数值与单元测试。
- `results/`：实验输出，不作为“真理来源”。
- `scripts/`：辅助脚本，包括 Trae 启动器。
- `AGENTS.md`：给 Agent 的工作边界。

## 第一次启动

1. 把整个目录上传到 GitHub 仓库。
2. 在 GitHub 中选择 **Code → Codespaces → Create codespace**。
3. 等待 devcontainer 初始化完成。
4. 在 Codespaces 终端运行：

```bash
pytest -q
jupyter lab --ip=0.0.0.0 --no-browser
```

5. 打开 `notebooks/01_ols.py`。Jupytext 会把它作为 Notebook 使用。
6. 运行：

```bash
./scripts/trae --help
```

如 Trae 安装成功，会显示 CLI 帮助。

## 第一个 Agent 任务

不要让 Agent “帮我把模型全部做完”。从这个任务开始：

```text
阅读 AGENTS.md、theory/01_ols.md 和 specs/01_ols_spec.md。
不要修改 theory/ 或 specs/。
检查 src/ols.py 与 tests/test_ols.py。
先运行 pytest -q。
如果测试失败，只修复 src/ols.py；不得改变测试阈值、真实参数或数据生成机制。
修复后再次运行 pytest -q，并总结你改了什么、为什么。
```

## API Key

不要把 API Key 写进仓库，也不要提交 `.env`。
建议用 GitHub Codespaces Secrets 注入环境变量，再让 Trae 从环境变量读取。
