from app.dependencies.conversation_summary_dependencies import (
    conversation_summary_service
)

from app.dependencies.long_term_memory_dependencies import (
    long_term_memory_service
)


class MemoryTool:

    def execute(
        self,
        session_id: str = "agent-session"
    ) -> str:

        summary = (
            conversation_summary_service
            .get_summary(session_id)
        )

        memories = (
            long_term_memory_service
            .get_memories(session_id)
        )

        memory_text = "\n".join(
            memories
        )

        return f"""
Conversation Summary:
{summary}

Long Term Memories:
{memory_text}
"""