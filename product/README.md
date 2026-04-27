# AI Gia Sư Toán — Hướng Dẫn Giải Bài Bằng Gợi Ý

> Một agent toán học thông minh, hướng dẫn học sinh giải bài toán 10-12 bằng gợi ý từng bước, không cho đáp án thẳng.

---

## 🚀 Bắt Đầu Nhanh

### 1. Cài Đặt

```bash
# Clone repo
cd product

# Tạo virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Cài dependencies
pip install -r requirements.txt

# Cấu hình API keys
cp .env.example .env
# Mở .env và điền OPENAI_API_KEY
```

### 2. Chạy Backend

```bash
# Chạy API server
uvicorn main:app --reload

# Server chạy tại http://localhost:8000
```

### 3. Chạy Frontend (nếu có)

```bash
cd prototype/frontend
npm install
npm run dev
```

---

## 📁 Cấu Trúc Thư Mục

```
product/
├── core/                    # Lõi hệ thống
│   ├── llm_client.py       # Wrapper gọi OpenAI
│   ├── knowledge_base.py   # Vector store
│   └── rag_pipeline.py     # Retrieval nâng cao
├── agent/                   # Agent logic
│   ├── tutor_agent.py      # Entry point chính
│   ├── supervisor.py       # Multi-agent router
│   ├── prompts.py          # System prompts
│   ├── tools.py            # Function calling
│   └── workers/            # Specialized workers
├── guardrails/              # Safety layer
│   ├── input.py            # Input validation
│   └── output.py           # Output checking
├── hitl/                    # Human-in-the-loop
│   └── router.py           # Escalation logic
├── pipeline/                # Data pipeline
│   ├── etl.py              # Ingest + chunk + embed
│   └── quality_checks.py   # Data validation
├── monitoring/              # Observability
│   ├── logging_config.py   # Structured logging
│   ├── tracing.py          # Langfuse tracing
│   └── slo.yaml            # Quality thresholds
├── eval/                    # Evaluation
│   ├── benchmark.py        # Run golden dataset
│   ├── regression_gate.py  # Release gate
│   ├── rag_scorecard.csv   # Retrieval metrics
│   └── golden_set.jsonl    # Test cases
├── data_for_rag/            # Knowledge base (toan10/11/12)
├── docs/                    # Documentation
│   ├── problem_statement.md
│   └── spec.md
├── prototype/               # UI (optional)
├── Dockerfile              # Container image
├── docker-compose.yml      # Full stack
├── requirements.txt        # Dependencies
├── .env.example            # Environment template
├── PLAN.md                 # Implementation plan
└── main.py                 # FastAPI entry point
```

---

## 🔧 Các Lệnh Chính

```bash
# Chạy API server
python main.py

# Ingest data từ data_for_rag/
python pipeline/etl.py

# Chạy benchmark trên golden dataset
python eval/benchmark.py

# Kiểm tra release gate
python eval/regression_gate.py

# Chạy tests
pytest tests/ -v

# Build Docker image
docker build -t tutor-ai .

# Chạy toàn bộ stack
docker compose up
```

---

## 📊 Kiến Trúc

```
[UI/Chat Interface]
        │
        ▼
[tutor_agent.py] ← Entry point
        │
    ┌───┴───┬──────────┐
    ▼       ▼          ▼
[Input   [Supervisor] [Output
Guardrails]  │      Guardrails]
             ▼
        [Workers]
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
[Retrieval] [Hint] [Check]
    │
    ▼
[RAG Pipeline]
    │
    ▼
[Knowledge Base]
    │
    ▼
[data_for_rag/]
```

---

## 🎯 Nguyên Tắc Cốt Lõi

1. **Không cho đáp án thẳng** — chỉ gợi ý hướng suy nghĩ
2. **Kiểm tra hiểu bài** — không phải chỉ nhớ công thức
3. **Escalate khi cần** — giáo viên vào khi agent không chắc
4. **Đo lường mọi thứ** — logging + tracing + eval

---

## 📈 Chất Lượng

Các SLO được định nghĩa trong `monitoring/slo.yaml`:

- Response time p95 < 3s
- Guardrail block rate < 5%
- RAG hit rate > 80%
- Answer leak rate = 0% (zero tolerance)

---

## 🚢 Deployment

### Local

```bash
docker compose up
```

### Cloud (Railway / Render)

```bash
# Build image
docker build -t tutor-ai .

# Push to registry
docker tag tutor-ai your-registry/tutor-ai
docker push your-registry/tutor-ai

# Deploy (xem hướng dẫn từng platform)
```

---

## 📚 Tài Liệu

- `PLAN.md` — Kế hoạch implementation từng Day
- `docs/problem_statement.md` — Vấn đề + giải pháp
- `docs/spec.md` — Specification đầy đủ

---

## 🤝 Đóng Góp

Mỗi Day (1-14) có một phần cụ thể để implement. Xem `PLAN.md` để biết thứ tự.

---

## 📝 License

MIT

---

**Chúc bạn xây dựng được một AI Gia Sư thực sự hữu ích!**
