# =============================================================================
# monitoring/tracing.py  —  Day 13
# =============================================================================
# Vai trò: Langfuse tracing — ghi lại toàn bộ "hành trình" của mỗi câu hỏi.
#
# Trong khi logging ghi sự kiện rời rạc, tracing ghi toàn bộ cây thực thi:
# câu hỏi → supervisor route → worker nào → LLM call nào → output gì.
#
# Mỗi session học sinh = 1 trace trong Langfuse dashboard.
# Mỗi bước trong ReAct loop = 1 span trong trace đó.
#
# Ghi lại:
#   - Input / output của từng LLM call
#   - Latency từng bước
#   - Chunks nào được retrieve
#   - Guardrail nào được trigger
#   - HITL decision
#
# Được dùng bởi:
#   - agent/tutor_agent.py   (wrap toàn bộ flow trong 1 trace)
#   - agent/workers/         (mỗi worker tạo 1 span)
#   - core/rag_pipeline.py   (trace retrieval step)
# =============================================================================
