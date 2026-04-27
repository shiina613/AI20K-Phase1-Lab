# =============================================================================
# pipeline/quality_checks.py  —  Day 10
# =============================================================================
# Vai trò: Kiểm tra chất lượng data trước khi nạp vào vector store.
#
# Chạy như một bộ "unit test cho data" — nếu fail thì etl.py dừng lại,
# không nạp data xấu vào knowledge base.
#
# Các kiểm tra:
#   - Không có chunk rỗng hoặc quá ngắn (< 50 ký tự)
#   - Không có chunk trùng lặp
#   - Metadata đầy đủ (grade, topic, source)
#   - Tỷ lệ ký tự toán học hợp lý (không phải file bị corrupt)
#   - Tổng số chunk trong khoảng kỳ vọng (phát hiện mất data)
#
# Được dùng bởi:
#   - pipeline/etl.py  (gọi trước bước Load)
# =============================================================================
