# =============================================================================
# core/llm_client.py  —  Day 1
# =============================================================================
# Vai trò: Wrapper duy nhất để gọi LLM (OpenAI GPT-4o / GPT-4o-mini).
#
# Tất cả các file khác trong product/ đều import từ đây để gọi LLM,
# không ai gọi openai trực tiếp. Điều này giúp dễ đổi model sau này.
#
# Cung cấp:
#   - call()          : gọi LLM, trả về (text, latency)
#   - stream()        : gọi LLM với streaming, yield từng token
#   - compare_models(): so sánh GPT-4o vs GPT-4o-mini (cost + latency)
#
# Được dùng bởi:
#   - agent/tutor_agent.py   (gọi LLM để tạo gợi ý)
#   - agent/workers/         (mỗi worker gọi LLM cho task riêng)
#   - guardrails/output.py   (LLM-as-Judge kiểm tra output)
#   - eval/benchmark.py      (gọi LLM để chấm điểm)
# =============================================================================
