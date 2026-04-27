# =============================================================================
# core/rag_pipeline.py  —  Day 8
# =============================================================================
# Vai trò: Retrieval pipeline — nhận câu hỏi, trả về context liên quan.
#
# Nâng cấp từ knowledge_base.py với các kỹ thuật retrieval nâng cao:
# hybrid search (dense + sparse), query transformation, reranking.
#
# Cung cấp:
#   - retrieve(query, grade)  : trả về list[Chunk] đã rerank
#   - evaluate()              : đo faithfulness + relevance, ghi vào rag_scorecard.csv
#
# Pipeline nội bộ:
#   câu hỏi → query transformation → hybrid search → rerank → top-k chunks
#
# Được dùng bởi:
#   - agent/workers/retrieval_worker.py  (lấy context cho từng câu hỏi)
#   - eval/benchmark.py                  (đánh giá chất lượng retrieval)
# =============================================================================
