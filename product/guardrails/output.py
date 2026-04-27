# =============================================================================
# guardrails/output.py  —  Day 11
# =============================================================================
# Vai trò: Kiểm tra output của agent TRƯỚC khi trả về cho học sinh.
#
# Đây là lớp bảo vệ quan trọng nhất — đảm bảo agent không vô tình
# vi phạm nguyên tắc gia sư (không cho đáp án thẳng).
#
# Các kiểm tra:
#   - Answer leak detection  : phát hiện nếu response chứa đáp án hoàn chỉnh
#   - LLM-as-Judge           : dùng GPT-4o-mini đánh giá response có phải gợi ý không
#   - Content filter         : lọc nội dung không phù hợp
#   - Hallucination check    : response có dựa trên retrieved context không
#
# Trả về: { approved: bool, reason: str, revised_response: str | None }
# Nếu approved=False, hitl/router.py quyết định escalate hay retry.
#
# Được dùng bởi:
#   - agent/tutor_agent.py  (bước cuối trước khi trả về cho học sinh)
# =============================================================================
