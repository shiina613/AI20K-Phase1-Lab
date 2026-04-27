# Kế Hoạch Sản Phẩm: AI Gia Sư

> Hướng dẫn giải bài bằng gợi ý — không cho đáp án thẳng

---

## Tổng Quan Flow

```
Day 1-2   → Nền tảng & Ý tưởng sản phẩm
Day 3-4   → Lõi agent (ReAct + Tool calling)
Day 5-6   → Spec & Prototype
Day 7     → Knowledge base (RAG data layer)
Day 8-10  → RAG pipeline + Multi-agent + Data pipeline
Day 11    → Guardrails & HITL
Day 12    → Deploy lên cloud
Day 13    → Observability & Monitoring
Day 14    → Evaluation & Benchmarking
```

---

## Chi Tiết Từng Day

**Day 1 — Nền tảng LLM API**
Xây `core/llm_client.py` — wrapper gọi OpenAI với streaming, so sánh model, quản lý cost.
Output: `core/llm_client.py`

**Day 2 — AI Product Thinking**
Điền đầy đủ Problem Scan → chọn bài toán gia sư AI → viết Problem Statement chính thức.
Output: `docs/problem_statement.md`

**Day 3 — ReAct Agent**
Xây agent lõi với Thought-Action-Observation loop. Agent biết khi nào cần gợi ý, khi nào cần hỏi lại.
Output: `agent/tutor_agent.py`

**Day 4 — Prompt Engineering & Tool Calling**
Thiết kế system prompt gia sư (không cho đáp án thẳng). Định nghĩa các tools: `hint_tool`, `check_understanding_tool`, `explain_concept_tool`.
Output: `agent/prompts.py`, `agent/tools.py`

**Day 5-6 — Product Spec & Prototype**
Viết spec đầy đủ 6 phần cho gia sư AI. Build prototype kết nối trực tiếp với `data_for_rag/` — không dùng mock data.
Output: `docs/spec.md`, `prototype/`

**Day 7 — Data Foundations**
Xây knowledge base từ `data_for_rag/` (toan10, toan11, toan12 — các file `.md` thực tế). Implement chunking + vector store + RAG agent. Không dùng mock data.
Output: `core/knowledge_base.py`

**Day 8 — RAG Pipeline**
Nâng cấp retrieval trên `data_for_rag/` — hybrid search, reranking, grounded prompting. Đo faithfulness + relevance với data toán thực tế.
Output: `core/rag_pipeline.py`, `eval/rag_scorecard.csv`

**Day 9 — Multi-Agent**
Tách agent thành Supervisor + Workers: `retrieval_worker` (tìm tài liệu liên quan), `hint_worker` (tạo gợi ý), `check_worker` (kiểm tra hiểu bài). Supervisor route theo loại câu hỏi.
Output: `agent/supervisor.py`, `agent/workers/`

**Day 10 — Data Pipeline**
ETL pipeline để ingest tài liệu mới (PDF, markdown). Data quality checks. Freshness monitor để biết khi nào knowledge base cũ.
Output: `pipeline/etl.py`, `pipeline/quality_checks.py`

**Day 11 — Guardrails & HITL**
Thêm input guardrails (chặn prompt injection, lọc topic ngoài phạm vi). Output guardrails (không để agent vô tình cho đáp án thẳng). HITL: khi confidence thấp thì escalate cho giáo viên.
Output: `guardrails/input.py`, `guardrails/output.py`, `hitl/router.py`

**Day 12 — Deployment**
Dockerize toàn bộ product. Deploy lên cloud (Railway hoặc Render). API gateway với auth + rate limiting.
Output: `Dockerfile`, `docker-compose.yml`, `deploy/`

**Day 13 — Observability**
Structured logging với correlation ID. Langfuse tracing cho mỗi session gia sư. SLO: response time < 3s, guardrail block rate < 5%.
Output: `monitoring/logging_config.py`, `monitoring/tracing.py`, `monitoring/slo.yaml`

**Day 14 — Evaluation & Benchmarking**
Golden dataset gồm 50+ câu hỏi toán thực tế (lấy từ `data_for_rag/`) + expected hints (không phải đáp án). Multi-judge eval: hint có hữu ích không, có vô tình leak đáp án không. Regression gate trước mỗi lần release.
Output: `eval/golden_set.jsonl`, `eval/benchmark.py`, `eval/regression_gate.py`

---

## Cấu Trúc Folder `product/` Cuối Cùng

```
product/
├── core/
│   ├── llm_client.py          ← Day 1
│   ├── knowledge_base.py      ← Day 7
│   └── rag_pipeline.py        ← Day 8
├── agent/
│   ├── prompts.py             ← Day 4
│   ├── tools.py               ← Day 4
│   ├── tutor_agent.py         ← Day 3
│   ├── supervisor.py          ← Day 9
│   └── workers/               ← Day 9
├── guardrails/
│   ├── input.py               ← Day 11
│   └── output.py              ← Day 11
├── hitl/
│   └── router.py              ← Day 11
├── pipeline/
│   ├── etl.py                 ← Day 10
│   └── quality_checks.py      ← Day 10
├── monitoring/
│   ├── logging_config.py      ← Day 13
│   ├── tracing.py             ← Day 13
│   └── slo.yaml               ← Day 13
├── eval/
│   ├── golden_set.jsonl       ← Day 14
│   ├── benchmark.py           ← Day 14
│   └── regression_gate.py     ← Day 14
├── data_for_rag/              ← Data thực tế (toan10, toan11, toan12)
├── docs/
│   ├── problem_statement.md   ← Day 2
│   └── spec.md                ← Day 5-6
├── prototype/                 ← Day 5-6
├── deploy/                    ← Day 12
├── Dockerfile                 ← Day 12
└── docker-compose.yml         ← Day 12
```
