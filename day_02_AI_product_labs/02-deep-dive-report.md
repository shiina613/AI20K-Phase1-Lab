**Dự án:** [Tên dự án / bài toán bạn chọn]

---
# Phase 4 — DEEP-DIVE

## 4.1 — Current-State Workflow

### Plaintext

```text
┌─────────────┐     ┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│ Bước 1      │     │ Bước 2      │     │ Bước 3       │     │ Bước 4           │
│             │     │             │     │              │     │                  │
│             │ ──→ │             │ ──→ │              │ ──→ │                  │
│ Ai:         │     │ Ai:         │     │ Ai:          │     │ Ai:              │
│ ⏱           │     │ ⏱           │     │ ⏱            │     │ ⏱                │
│ In:         │     │ In:         │     │ In:          │     │ In:              │
│ Out:        │     │ Out:        │     │ Out:         │     │ Out:             │
└─────────────┘     └─────────────┘     └──────────────┘     └──────────────────┘
```

## 🔴 = Bottleneck (Điểm nghẽn)

### Ghi chú bottleneck

- **Bước ___ (___% rủi ro):** [Mô tả tại sao đây là bottleneck]
- **Bước ___ (Tốn kém nhất):** [Mô tả hậu quả]

---

## 4.2 — Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **Actor / Operator** | |
| **Current Workflow** | |
| **Bottleneck** | |
| **Impact** | |
| **Success Metric** | |
| **Operational Boundary** | |

### Sub-goals Decomposition

- **Trước khi dùng AI:** 
- **Trong khi dùng AI:** 

### Metrics

| Loại | Metric | Ngưỡng |
|---|---|---|
| **Efficiency** | | |
| **Quality** | | |

---

## 4.3 — Research

### Existing solution

[Các giải pháp hiện có trên thị trường là gì? Chúng mạnh/yếu ở điểm nào?]

### Case study

[Có team/công ty nào đã giải bài toán tương tự chưa? Họ làm thế nào?]

### Quick poll

[Khảo sát nhanh người dùng thực tế — họ nói gì?]

### Bài học rút ra

[Insight quan trọng nhất từ research là gì?]

---

## 4.4 — Future-State Flow + AI Fit

### AI Fit Check

Bài toán nằm ở: **___ (Complexity) + ___ (Ambiguity) → ___**

### AI Suitability Check

- Cần ___ để ___
- Cần ___ để ___

### UX Check

Nếu AI sai → [Hậu quả là gì? Có chấp nhận được không?]

### Future-State Flow

```text
┌─────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Bước 1      │     │ Bước 2           │     │ Bước 3           │
│             │ ──→ │ 🔵 AI            │ ──→ │ 🔵 AI            │
│             │     │                  │     │                  │
└─────────────┘     └──────────────────┘     └──────────────────┘
                                                       │
                                                       ▼
┌──────────────────┐     ┌─────────────┐     ┌──────────────────┐
│ Bước 6           │     │ Bước 5      │     │ Bước 4           │
│                  │ ←── │ 🟢          │ ←── │ 🟢               │
│                  │     │             │     │                  │
└──────────────────┘     └─────────────┘     └──────────────────┘
```

**➡️ Fallback:** [Nếu AI thất bại thì xử lý thế nào?]

### AI Fit Decision

**Chốt:** [LLM Feature / Agent / Rule-based]

#### Vì sao không phải ___?
[Giải thích]

#### Vì sao không phải ___?
[Giải thích]

### Underspecification Check (Những điều chưa rõ)

| Điều chưa rõ | Hậu quả | Cách tìm ra |
|---|---|---|
| | | |
| | | |



# Phase 5 — EVALUATE

### AI Readiness Checklist

| # | Câu hỏi | Kết quả | Ghi chú |
|---|---|---|---|
| 1 | Có data/input đủ chất lượng? | Yes / No | |
| 2 | Có metric rõ? | Yes / No | |
| 3 | Sai thì hậu quả có chấp nhận được? | Yes / No | |
| 4 | User sẵn sàng dùng AI? | Yes / No | |
| 5 | Có resource để maintain? | Yes / No | |

### Optimization Check

#### Lợi ích

- 
- 

#### Rủi ro nếu optimize sai

- 
- 

### Quyết định

**[Go / Not Yet / No Go]**

### Justify

[Giải thích lý do quyết định]

### Scope pilot đề xuất

- Chỉ áp dụng cho ___
- AI chỉ làm ___ việc:
  1. 
  2. 
  3. 

### Nếu pilot thất bại

- Quay về ___
- Hoặc ___

### Vì sao quyết định này tốt

[Giải thích ngắn gọn]
