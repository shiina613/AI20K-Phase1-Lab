# =============================================================================
# monitoring/logging_config.py  —  Day 13
# =============================================================================
# Vai trò: Cấu hình structured logging cho toàn bộ product.
#
# Mọi request đều được log dưới dạng JSON với correlation_id để có thể
# trace một session học sinh từ đầu đến cuối.
#
# Cấu hình:
#   - structlog với JSON format
#   - Correlation ID middleware (mỗi request có x-request-id riêng)
#   - PII scrubbing (tự động ẩn tên, email nếu học sinh vô tình gửi)
#   - Log levels: DEBUG (dev) / INFO (prod)
#
# Các field chuẩn trong mỗi log entry:
#   { timestamp, request_id, session_id, grade, event, latency_ms, ... }
#
# Được dùng bởi:
#   - Tất cả các module khác đều import logger từ đây
#   - monitoring/tracing.py  (kết hợp log với Langfuse trace)
# =============================================================================
