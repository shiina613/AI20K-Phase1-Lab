# =============================================================================
# eval/regression_gate.py  —  Day 14
# =============================================================================
# Vai trò: Tự động quyết định "Release" hay "Rollback" dựa trên benchmark.
#
# So sánh kết quả benchmark của phiên bản mới với phiên bản cũ (baseline).
# Nếu bất kỳ chỉ số nào tệ hơn ngưỡng → tự động block release.
#
# Ngưỡng (lấy từ monitoring/slo.yaml):
#   - hint_quality giảm > 10%  → ROLLBACK
#   - answer_leak_rate > 0%    → ROLLBACK (zero tolerance)
#   - latency_p95 tăng > 20%   → WARNING
#   - rag_hit_rate giảm > 5%   → ROLLBACK
#
# Output: { decision: "RELEASE" | "ROLLBACK", delta_report: {...} }
#
# Được dùng bởi:
#   - CI/CD pipeline  (chạy tự động trước khi deploy lên production)
#   - Chạy thủ công: python eval/regression_gate.py
# =============================================================================
