# =============================================================================
# guardrails/input.py  —  Day 11
# =============================================================================
# Vai trò: Kiểm tra input của học sinh TRƯỚC khi agent xử lý.
#
# Chặn các input nguy hiểm hoặc ngoài phạm vi, bảo vệ agent khỏi bị lợi dụng.
#
# Các kiểm tra:
#   - Prompt injection detection  : phát hiện lệnh cố tình override system prompt
#   - Topic filter                : chỉ chấp nhận câu hỏi về toán 10/11/12
#   - Input length                : từ chối input quá dài (> 2000 ký tự)
#   - PII detection               : cảnh báo nếu học sinh gửi thông tin cá nhân
#
# Trả về: { allowed: bool, reason: str }
# Nếu allowed=False, tutor_agent trả về thông báo từ chối, không gọi LLM.
#
# Được dùng bởi:
#   - agent/tutor_agent.py  (bước đầu tiên trong flow xử lý)
# =============================================================================
