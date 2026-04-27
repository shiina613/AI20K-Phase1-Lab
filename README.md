# AI20K Phase 1 — Lab Portfolio

Repo này tổng hợp toàn bộ bài lab của khóa học AI20K Phase 1, với mục tiêu cuối cùng là xây dựng một sản phẩm AI hoàn chỉnh từ đầu đến cuối.

---

## Sản Phẩm

Tất cả code sản phẩm nằm trong folder `product/` — một **AI Gia Sư Toán** hướng dẫn học sinh giải bài bằng gợi ý, không cho đáp án thẳng.

→ Xem [`product/README.md`](product/README.md) để biết cách chạy.
→ Xem [`product/PLAN.md`](product/PLAN.md) để biết kế hoạch implementation từng Day.

---

## Cấu Trúc

| Folder | Nội dung |
|--------|----------|
| `product/` | Sản phẩm chính — AI Gia Sư Toán (Day 1–14) |
| `day_01_llm_api_foundation/` | Lab: LLM API cơ bản |
| `day_02_AI_product_labs/` | Lab: AI Product thinking |
| `Day-3-Lab-Chatbot-vs-react-agent/` | Lab: Chatbot vs ReAct Agent |
| `Day-04-Prompt-engineering & Tool call/` | Lab: Prompt engineering & Tool calling |
| `Day-5+6-.../` | Lab: Product spec + prototype |
| `Day-07-Lab-Data-Foundations/` | Lab: Embeddings, chunking, vector store |
| `Lecture-Day-08-09-10/` | Lecture: RAG, Multi-agent, Data pipeline |
| `Day-11-Guardrails-HITL-Responsible-AI/` | Lab: Guardrails, HITL |
| `day12_ha-tang-cloud_va_deployment/` | Lab: Cloud deployment |
| `Lab13-Observability/` | Lab: Logging, tracing, monitoring |
| `Lab14-AI-Evaluation-Benchmarking/` | Lab: Evaluation & benchmarking |

---

## Flow Học → Sản Phẩm

Mỗi Day lab không chỉ là bài tập độc lập — kết quả của từng Day được tích hợp trực tiếp vào `product/`:

```
Day 1  → product/core/llm_client.py
Day 2  → product/docs/problem_statement.md
Day 3  → product/agent/tutor_agent.py
Day 4  → product/agent/prompts.py + tools.py
Day 5-6 → product/docs/spec.md + prototype/
Day 7  → product/core/knowledge_base.py
Day 8  → product/core/rag_pipeline.py
Day 9  → product/agent/supervisor.py + workers/
Day 10 → product/pipeline/etl.py
Day 11 → product/guardrails/ + product/hitl/
Day 12 → product/Dockerfile + docker-compose.yml
Day 13 → product/monitoring/
Day 14 → product/eval/
```

---

## Setup

```bash
git clone <repo-url>
cd AI20K-Phase1-Lab

# Cài dependencies cho product
cd product
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Điền OPENAI_API_KEY vào .env
```
