# =============================================================================
# agent/supervisor.py  —  Day 9
# =============================================================================
# Vai trò: Supervisor trong kiến trúc Multi-Agent — điều phối các worker.
#
# Nhận câu hỏi từ tutor_agent, phân tích loại câu hỏi và route đến
# đúng worker. Không tự xử lý — chỉ điều phối.
#
# Workers hiện có (trong agent/workers/):
#   - retrieval_worker  : tìm tài liệu liên quan từ rag_pipeline
#   - hint_worker       : tạo gợi ý từng bước dựa trên context
#   - check_worker      : kiểm tra học sinh đã hiểu đúng chưa
#
# Logic route:
#   - Câu hỏi mới → retrieval_worker → hint_worker
#   - Học sinh trả lời → check_worker
#   - Câu hỏi về khái niệm → retrieval_worker → hint_worker (explain mode)
#
# Ghi trace_log để debug tại sao route đến worker nào.
#
# Được dùng bởi:
#   - agent/tutor_agent.py  (gọi supervisor.route() thay vì gọi worker trực tiếp)
# =============================================================================
