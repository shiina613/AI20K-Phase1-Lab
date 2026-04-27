# PLAN — Xây dựng [Tên Agent / Product]

## 1. Bài toán

*[Mô tả bài toán cần giải quyết — ai gặp vấn đề gì, AI đóng vai trò gì]*

---

## 2. Kiến trúc tổng thể

```text
┌─────────────────────────────────────────────────────────────────┐
│                         [Tên UI]                                 │
│                  (Framework · port ___)                          │
│   Chat Widget ──── POST /chat ──────────────────────────────┐   │
└──────────────────────────────────────────────────────────────┼───┘
                                                               │
                              ┌────────────────────────────────▼───────────────┐
                              │               [Tên Backend]                     │
                              │               (Framework · port ___)            │
                              │                                                  │
                              │   POST /chat       → agent.py                  │
                              │   POST /feedback   → feedback_log.json         │
                              │                                                  │
                              │   [LLM Provider]                               │
                              │     └─ function calling (___ tools)             │
                              └─────────────────────────────────────────────────┘
```

### Luồng xử lý một request

```text
User nhập câu hỏi
    │
    ▼
Frontend gửi POST /chat { message, history }
    │
    ▼
Backend → chat handler
    │
    ▼
LLM nhận system prompt + history + message
    │
    ├─ Cần dữ liệu → chọn tool (function calling)
    │       │
    │       ▼
    │   Tool thực thi → trả JSON
    │       │
    │       ▼
    │   LLM sinh câu trả lời
    │
    └─ Không cần tool → LLM trả lời trực tiếp
    │
    ▼
Frontend render response
```

---

## 3. Công nghệ sử dụng

| Layer | Công nghệ | Lý do chọn |
| --- | --- | --- |
| Frontend | | |
| Backend | | |
| LLM | | |
| Agent pattern | | |
| Data | | |

---

## 4. Cấu trúc thư mục

```text
[Tên project]/
├── PLAN.md
├── README.md
├── spec-final.md
├── test_cases.md
├── tools_list.md
└── Prototype/
    ├── [frontend]/
    └── [backend]/
        ├── main.py
        ├── agent.py
        ├── requirements.txt
        ├── .env.example
        ├── tools/
        └── mock_data/
```

---

## 5. Chi tiết từng Tool

### Tool 1: `[tên_tool]`

*[Mô tả chức năng, input, output]*

### Tool 2: `[tên_tool]`

*[Mô tả chức năng, input, output]*

### Tool 3: `[tên_tool]`

*[Mô tả chức năng, input, output]*

---

## 6. System Prompt — Các cải tiến

| Tính năng | Mô tả |
| --- | --- |
| Phạm vi hỗ trợ | |
| Chống prompt injection | |
| Xử lý thiếu thông tin | |
| Format output | |

---

## 7. Frontend — Tính năng

| Tính năng | Mô tả |
| --- | --- |
| | |
| | |
| | |

---

## 8. API Contract

### `POST /chat`

```json
{ "message": "...", "history": [] }
```

```json
{ "response": "..." }
```

### `POST /feedback`

```json
{ "bot_response": "...", "user_message": "...", "rating": "like/dislike", "comment": "..." }
```

```json
{ "status": "ok" }
```

---

## 9. Test Cases Coverage

| # | Test case | Cách xử lý |
| --- | --- | --- |
| 1 | | |
| 2 | | |
| 3 | | |

---

## 10. Chiến lược Data & Mở rộng

| Tool | Hiện tại | Có thể mở rộng |
| --- | --- | --- |
| | Mock JSON | |
| | Mock JSON | |

---

## 11. Feedback Loop

Mỗi response có feedback bar. Dữ liệu lưu vào `feedback_log.json`:

```json
{
  "timestamp": "...",
  "rating": "like/dislike",
  "comment": "...",
  "user_message": "...",
  "bot_response": "..."
}
```
