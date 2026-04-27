# =============================================================================
# core/knowledge_base.py  —  Day 7
# =============================================================================
# Vai trò: Vector store — nơi lưu trữ toàn bộ tài liệu toán đã được embed.
#
# Load tài liệu từ data_for_rag/ (toan10, toan11, toan12),
# chunk thành đoạn nhỏ, embed và lưu vào vector store (ChromaDB / FAISS).
#
# Cung cấp:
#   - build()         : đọc data_for_rag/, chunk, embed, lưu vào store
#   - search(query)   : tìm top-k chunks liên quan nhất với câu hỏi
#   - search_with_filter(query, grade): lọc theo lớp (10/11/12)
#   - delete(doc_id)  : xóa tài liệu khỏi store
#
# Được dùng bởi:
#   - core/rag_pipeline.py   (gọi search() để lấy context)
#   - pipeline/etl.py        (gọi build() sau khi ingest data mới)
# =============================================================================
