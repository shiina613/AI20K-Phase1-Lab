# =============================================================================
# agent/tools.py  —  Day 4
# =============================================================================
# Vai trò: Định nghĩa các tool mà agent có thể gọi (function calling).
#
# Tools:
#   - hint_tool(question, step)       : tạo gợi ý cho bước cụ thể
#   - check_understanding_tool(answer): kiểm tra học sinh hiểu đúng chưa
#   - explain_concept_tool(concept)   : giải thích khái niệm toán học
#   - retrieve_tool(query, grade)     : tìm tài liệu liên quan từ knowledge base
#
# Mỗi tool được định nghĩa theo chuẩn OpenAI function calling schema
# (name, description, parameters) để LLM biết khi nào nên gọi tool nào.
#
# Được dùng bởi:
#   - agent/tutor_agent.py   (đăng ký tools vào agent loop)
#   - agent/supervisor.py    (route dựa trên tool được gọi)
# =============================================================================
