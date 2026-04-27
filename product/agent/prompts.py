# =============================================================================
# agent/prompts.py  —  Day 4
# =============================================================================
# Vai trò: Nơi tập trung toàn bộ system prompt và prompt template.
#
# Nguyên tắc cốt lõi: agent là GIA SƯ, không phải máy giải toán.
# Tuyệt đối không được cho đáp án thẳng — chỉ gợi ý hướng suy nghĩ.
#
# Chứa:
#   - SYSTEM_PROMPT       : định nghĩa vai trò gia sư, luật không cho đáp án
#   - HINT_PROMPT         : template tạo gợi ý từng bước
#   - CHECK_UNDERSTANDING : template kiểm tra học sinh đã hiểu chưa
#   - EXPLAIN_CONCEPT     : template giải thích khái niệm liên quan
#   - GROUNDED_PROMPT     : template inject retrieved context vào prompt
#
# Được dùng bởi:
#   - agent/tutor_agent.py   (SYSTEM_PROMPT, GROUNDED_PROMPT)
#   - agent/workers/         (mỗi worker dùng template riêng)
#   - guardrails/output.py   (kiểm tra output có vi phạm luật không)
# =============================================================================
