# [Tên Product] — AI Chatbot / Agent

## Nhóm ___ · Lớp ___ · Day 06

| Thành viên | MSSV |
| --- | --- |
| | |
| | |
| | |
| | |

---

## Cấu trúc nộp bài

```
[Tên nhóm]/
│
├── spec-final.md               ← [NỘP] SPEC 6 phần đầy đủ
├── prototype-readme.md         ← [NỘP] Mô tả prototype + link + phân công
├── demo-slides.pdf             ← [NỘP] Poster demo
│
├── PLAN.md                     ← (optional) Kiến trúc chi tiết + API contract
├── test_cases.md               ← (optional) Bộ test cases
├── tools_list.md               ← (optional) Danh sách tools thiết kế
│
└── Prototype/                  ← (optional) Source code working prototype
    ├── [frontend]/
    └── [backend]/
```

---

## Giới thiệu

*[Mô tả product — giải quyết vấn đề gì, cho ai, tính năng chính]*

---

## Kiến trúc

```text
[UI] (Framework · :port)
           │  POST /chat, /feedback
           ▼
    [Backend] (:port)
           │  function calling (___ tools)
           ▼
     [LLM Provider]
           │
     ┌─────┴──────────┐
     Tools         Mock Data
```

---

## Yêu cầu

- **Python** 3.10+
- **Node.js** 18+
- **[LLM] API Key**

---

## Hướng dẫn chạy

### Bước 1 — Cài đặt & chạy Backend

```bash
cd Prototype/[backend]
cp .env.example .env
# Điền API key vào .env
pip install -r requirements.txt
uvicorn main:app --reload
```

### Bước 2 — Cài đặt & chạy Frontend

```bash
cd Prototype/[frontend]
npm install
npm run dev
```

---

## Câu hỏi mẫu để test

| Tính năng | Câu hỏi mẫu |
| --- | --- |
| | |
| | |
| | |

---

## Endpoints Backend

| Method | Path | Mô tả |
| --- | --- | --- |
| GET | `/` | Health check |
| POST | `/chat` | Gửi tin nhắn, nhận phản hồi |
| POST | `/feedback` | Ghi nhận feedback |

---

## Lưu ý

- *[Ghi chú quan trọng về data, API key, giới hạn,...]*
