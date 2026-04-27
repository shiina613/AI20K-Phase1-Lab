# =============================================================================
# pipeline/etl.py  —  Day 10
# =============================================================================
# Vai trò: ETL pipeline — đọc data_for_rag/, làm sạch, embed, nạp vào store.
#
# Chạy khi: có tài liệu mới thêm vào data_for_rag/, hoặc cần rebuild store.
#
# Pipeline:
#   1. Extract  : đọc tất cả file .md từ data_for_rag/toan10, toan11, toan12
#   2. Transform: làm sạch markdown, loại bỏ HTML artifacts, chuẩn hoá format
#   3. Chunk    : chia thành đoạn nhỏ (SentenceChunker / RecursiveChunker)
#   4. Validate : chạy quality_checks.py trước khi load
#   5. Load     : embed và nạp vào knowledge_base (vector store)
#
# Metadata gắn vào mỗi chunk: { grade: "10/11/12", topic: "...", source: "..." }
# để sau này search_with_filter() hoạt động đúng.
#
# Được dùng bởi:
#   - Chạy thủ công: python pipeline/etl.py
#   - monitoring/freshness_check.py  (phát hiện data cũ → trigger rebuild)
# =============================================================================
