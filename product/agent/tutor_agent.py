# =============================================================================
# agent/tutor_agent.py  —  Day 3
# =============================================================================
# Vai trò: Entry point chính của sản phẩm — agent gia sư toán.
#
# Implement ReAct loop (Thought → Action → Observation) để xử lý câu hỏi
# của học sinh theo từng bước, gọi đúng tool, không bao giờ cho đáp án thẳng.
#
# Flow xử lý một câu hỏi:
#   1. Nhận câu hỏi từ học sinh
#   2. guardrails/input.py kiểm tra input
#   3. supervisor.py route đến đúng worker
#   4. worker lấy context từ rag_pipeline, tạo gợi ý qua llm_client
#   5. guardrails/output.py kiểm tra output
#   6. hitl/router.py quyết định trả về hay escalate
#   7. monitoring ghi log + trace
#   8. Trả về gợi ý cho học sinh
#
# Đây là file "dây nối" — kết hợp tất cả các module lại thành một luồng.
#
# Được dùng bởi:
#   - prototype/backend/main.py  (API endpoint /chat gọi vào đây)
#   - eval/benchmark.py          (chạy agent trên golden dataset)
# =============================================================================
