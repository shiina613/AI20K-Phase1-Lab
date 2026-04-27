# =============================================================================
# eval/benchmark.py  —  Day 14
# =============================================================================
# Vai trò: Chạy toàn bộ golden_set qua agent và đo chất lượng.
#
# Đây là "bài kiểm tra" định kỳ cho agent — chạy trước mỗi lần release
# để đảm bảo agent không bị tệ hơn so với phiên bản trước.
#
# Pipeline:
#   1. Load golden_set.jsonl (câu hỏi + expected hints)
#   2. Chạy từng câu qua tutor_agent (async để nhanh)
#   3. Đánh giá bằng multi-judge (GPT-4o + GPT-4o-mini):
#      - Hint có hữu ích không? (0-5)
#      - Có leak đáp án không? (boolean)
#      - Có dựa trên context không? (faithfulness)
#   4. Tính Hit Rate + MRR cho retrieval stage
#   5. Ghi kết quả vào reports/benchmark_results.json
#
# Được dùng bởi:
#   - eval/regression_gate.py  (đọc kết quả để quyết định release/rollback)
#   - Chạy thủ công: python eval/benchmark.py
# =============================================================================
