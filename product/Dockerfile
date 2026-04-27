# =============================================================================
# Dockerfile  —  Day 12
# =============================================================================
# Vai trò: Đóng gói toàn bộ product thành Docker image để deploy.
#
# Dùng multi-stage build để image production nhỏ gọn:
#   Stage 1 (builder): cài dependencies, build assets
#   Stage 2 (runtime): chỉ copy những gì cần thiết để chạy
#
# Image này chứa:
#   - Python runtime + tất cả dependencies từ requirements.txt
#   - Source code trong product/
#   - KHÔNG chứa data_for_rag/ (mount vào lúc chạy qua volume)
#   - KHÔNG chứa .env (inject qua environment variables lúc deploy)
#
# Build: docker build -t tutor-ai .
# Run:   docker run -p 8000:8000 --env-file .env tutor-ai
# =============================================================================
