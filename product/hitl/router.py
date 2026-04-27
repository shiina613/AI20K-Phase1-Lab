# =============================================================================
# hitl/router.py  —  Day 11
# =============================================================================
# Vai trò: Human-in-the-Loop router — quyết định khi nào cần giáo viên can thiệp.
#
# Không phải mọi câu hỏi đều agent tự xử lý được. Router này phát hiện
# các trường hợp cần escalate để đảm bảo chất lượng giảng dạy.
#
# 3 điểm quyết định:
#   1. Confidence thấp      : agent không chắc về câu trả lời → flag cho giáo viên
#   2. Output bị reject     : guardrails/output.py từ chối 2 lần liên tiếp → escalate
#   3. Học sinh bế tắc      : hỏi cùng một câu > 3 lần → giáo viên vào hỗ trợ
#
# Trả về: { action: "respond" | "escalate" | "retry", reason: str }
#
# Được dùng bởi:
#   - agent/tutor_agent.py  (sau khi guardrails/output.py kiểm tra xong)
# =============================================================================
