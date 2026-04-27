# SPEC — AI Product Hackathon

**Nhóm:** ___

**Track:** ☐ VinFast · ☐ Vinmec · ☐ VinUni-VinSchool · ☐ XanhSM · ☐ NEO chatbot VN/A

**Problem statement (1 câu):** *Ai gặp vấn đề gì, hiện giải thế nào, AI giúp được gì*

---

## 1. AI Product Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi** | User nào? Pain gì? AI giải gì? | Khi AI sai thì sao? User sửa bằng cách nào? | Cost/latency bao nhiêu? Risk chính? |
| **Trả lời** | *[Điền vào đây]* | *[Điền vào đây]* | *[Điền vào đây]* |

**Automation hay augmentation?** ☐ Automation · ☐ Augmentation

Justify: *[Giải thích lý do chọn]*

**Learning signal:**

1. User correction đi vào đâu? *[Điền vào đây]*
2. Product thu signal gì để biết tốt lên hay tệ đi? *[Điền vào đây]*
3. Data thuộc loại nào?
 ☐ User-specific · ☐ Domain-specific · ☐ Real-time · ☐ Human-judgment · ☐ Khác: *___*
   Có marginal value không? (Model đã biết cái này chưa?) *[Điền vào đây]*

---

## 2. User Stories — 4 paths

Mỗi feature chính = 1 bảng. AI trả lời xong → chuyện gì xảy ra?

### Feature: *[Tên feature]*

**Trigger:** *[Mô tả trigger]*

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | *[Điền vào đây]* |
| Low-confidence — AI không chắc | System báo "không chắc" bằng cách nào? User quyết thế nào? | *[Điền vào đây]* |
| Failure — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | *[Điền vào đây]* |
| Correction — user sửa | User sửa bằng cách nào? Data đó đi vào đâu? | *[Điền vào đây]* |

### Feature: *[Tên feature]*

**Trigger:** *[Mô tả trigger]*

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | *[Điền vào đây]* |
| Low-confidence — AI không chắc | System báo "không chắc" bằng cách nào? User quyết thế nào? | *[Điền vào đây]* |
| Failure — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | *[Điền vào đây]* |
| Correction — user sửa | User sửa bằng cách nào? Data đó đi vào đâu? | *[Điền vào đây]* |

### Feature: *[Tên feature]*

**Trigger:** *[Mô tả trigger]*

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | *[Điền vào đây]* |
| Low-confidence — AI không chắc | System báo "không chắc" bằng cách nào? User quyết thế nào? | *[Điền vào đây]* |
| Failure — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | *[Điền vào đây]* |
| Correction — user sửa | User sửa bằng cách nào? Data đó đi vào đâu? | *[Điền vào đây]* |

### Feature: *[Tên feature]*

**Trigger:** *[Mô tả trigger]*

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | *[Điền vào đây]* |
| Low-confidence — AI không chắc | System báo "không chắc" bằng cách nào? User quyết thế nào? | *[Điền vào đây]* |
| Failure — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | *[Điền vào đây]* |
| Correction — user sửa | User sửa bằng cách nào? Data đó đi vào đâu? | *[Điền vào đây]* |

*Lặp lại cho feature thứ 2-3 nếu có.*

---

## 3. Eval metrics + threshold

**Optimize precision hay recall?** ☐ Precision · ☐ Recall
Tại sao? *[Giải thích]*

Nếu sai ngược lại thì chuyện gì xảy ra? *[Điền vào đây]*

| Metric                          | Threshold | Red flag (dừng khi)             |
|---------------------------------|-----------|---------------------------------|
| *[Metric 1]*                    | *___*     | *[Điền vào đây]*                |
| *[Metric 2]*                    | *___*     | *[Điền vào đây]*                |
| *[Metric 3]*                    | *___*     | *[Điền vào đây]*                |

---

## 4. Top 3 failure modes

*Liệt kê cách product có thể fail — không phải list features.*
*"Failure mode nào user KHÔNG BIẾT bị sai? Đó là cái nguy hiểm nhất."*

| # | Trigger                                      | Hậu quả                                      | Mitigation                                   |
|---|----------------------------------------------|---------------------------------------------|---------------------------------------------|
| 1 | *[Điền vào đây]*                             | *[Điền vào đây]*                            | *[Điền vào đây]*                            |
| 2 | *[Điền vào đây]*                             | *[Điền vào đây]*                            | *[Điền vào đây]*                            |
| 3 | *[Điền vào đây]*                             | *[Điền vào đây]*                            | *[Điền vào đây]*                            |

---

## 5. ROI 3 kịch bản

|   | Conservative                          | Realistic                              | Optimistic                              |
|---|---------------------------------------|----------------------------------------|----------------------------------------|
| **Assumption** | *[Điền vào đây]*                     | *[Điền vào đây]*                      | *[Điền vào đây]*                       |
| **Cost**       | *[Điền vào đây]*                    | *[Điền vào đây]*                     | *[Điền vào đây]*                       |
| **Benefit**    | *[Điền vào đây]*                    | *[Điền vào đây]*                     | *[Điền vào đây]*                       |
| **Net**        | *[Điền vào đây]*                    | *[Điền vào đây]*                     | *[Điền vào đây]*                       |

**Kill criteria:** *[Điền điều kiện dừng]*

---

## 6. Mini AI spec (1 trang)

*Tóm tắt tự do — viết bằng ngôn ngữ tự nhiên, không format bắt buộc.*
*Gom lại: product giải gì, cho ai, AI làm gì (auto/aug), quality thế nào (precision/recall), risk chính, data flywheel ra sao.*

*[Điền vào đây]*
