# Problem Statement — AI Gia Sư Toán

> **Day 2 — AI Product Thinking**

## Vấn đề

Học sinh toán 10-12 thường gặp khó khăn khi tự học:
- Không biết bắt đầu từ đâu khi gặp bài toán mới
- Cần hướng dẫn từng bước, không phải đáp án thẳng
- Muốn kiểm tra hiểu bài hay chỉ nhớ công thức
- Không có gia sư 24/7 để hỏi

## Giải pháp

Xây dựng **AI Gia Sư** — agent toán học thông minh:
- Nhận câu hỏi từ học sinh
- Tìm tài liệu liên quan từ knowledge base (data_for_rag/)
- Tạo gợi ý từng bước thay vì cho đáp án
- Kiểm tra học sinh đã hiểu đúng chưa
- Escalate cho giáo viên nếu cần

## Thành công được đo bằng

- Hint có hữu ích không (multi-judge eval)
- Có vô tình leak đáp án không (zero tolerance)
- Response time < 3 giây
- Hit rate retrieval > 80%

---

**Được điền trong Day 2, dùng bởi tất cả các Day sau.**
