# Specification — AI Gia Sư Toán

> **Day 5-6 — Product Spec & Prototype**

## 1. Overview

AI Gia Sư là một agent toán học thông minh, hướng dẫn học sinh giải bài bằng gợi ý, không cho đáp án thẳng.

## 2. User Stories

- **Học sinh**: Hỏi câu hỏi toán → nhận gợi ý từng bước → tự giải
- **Giáo viên**: Monitor session → escalate khi cần → feedback

## 3. Functional Requirements

- Nhận câu hỏi toán (text)
- Retrieve tài liệu liên quan từ data_for_rag/
- Tạo gợi ý không leak đáp án
- Kiểm tra hiểu bài
- Escalate khi confidence thấp

## 4. Non-Functional Requirements

- Response time < 3s (p95)
- Uptime > 99%
- Guardrail block rate < 5%
- Answer leak rate = 0%

## 5. Technical Architecture

```
[UI] → [tutor_agent] → [supervisor] → [workers] → [rag_pipeline] → [knowledge_base]
                ↓
        [guardrails] → [hitl] → [monitoring]
```

## 6. Data & Privacy

- Data: toan10, toan11, toan12 từ data_for_rag/
- PII scrubbing: tự động ẩn thông tin cá nhân
- Logs: JSON structured, correlation ID

---

**Được viết trong Day 5-6, dùng bởi tất cả các Day sau.**
