import gradio as gr
import asyncio

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from teams.travel_team import team


# =========================
# ✅ FORMAT SEARCH RESULTS
# =========================
def format_search_result(data):
    if not isinstance(data, dict):
        return str(data)

    output = []

    # Query
    if "query" in data:
        output.append(f"🔍 **Search Query:** {data['query']}")

    # Answer
    if "answer" in data:
        output.append(f"\n📌 **Summary:**\n{data['answer']}")

    # Results
    if "results" in data and data["results"]:
        output.append("\n🌟 **Top Recommendations:**\n")

        for i, r in enumerate(data["results"][:5], 1):
            title = r.get("title", "No Title")
            content = r.get("content", "")
            url = r.get("url", "")

            if len(content) > 200:
                content = content[:200] + "..."

            output.append(
f"""**{i}. {title}**
{content}
🔗 {url}
"""
            )

    return "\n".join(output)


# =========================
# ✅ MASTER FORMATTER
# =========================
def format_travel_content(content):

    try:

        # ignore function lists
        if isinstance(content, list):
            return ""

        # IMPORTANT: handle dict output properly
        if isinstance(content, dict):
            return format_search_result(content)

        # string handling
        if isinstance(content, str):

            # sometimes dict comes as string
            if content.strip().startswith("{") and "query" in content:
                try:
                    return format_search_result(eval(content))
                except:
                    pass

            return content

        return str(content)

    except Exception as e:
        return f"Formatting error: {e}"


# =========================
# ✅ MAIN STREAMING FUNCTION
# =========================
async def generate_trip(destination, days, budget, interests):

    task = TextMessage(
        content=(
            f"Plan a trip to {destination} for {days} days "
            f"with a budget of {budget}. "
            f"Interests: {interests}"
        ),
        source="User",
    )

    final_output = ""

    async for message in team.run_stream(task=task):

        # Task completed
        if isinstance(message, TaskResult):

            final_output += f"\n\n✅ **Task Completed:** {message.stop_reason}"
            yield final_output
            return

        # Agent message
        formatted = format_travel_content(message.content)

        if formatted.strip():

            final_output += (
                f"\n\n---\n"
                f"## 🤖 {message.source}\n"
                f"{formatted}\n"
            )

            yield final_output


# =========================
# ✅ GRADIO UI
# =========================
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 🌍 AI Travel Planner (Multi-Agent System)

        Plan trips with AI agents (Planner + Researcher + Optimizer)
        """
    )

    with gr.Row():
        destination = gr.Textbox(label="📍 Destination", placeholder="Chennai")
        days = gr.Number(label="📅 Days", value=2)

    with gr.Row():
        budget = gr.Textbox(label="💰 Budget", placeholder="5000 INR")
        interests = gr.Textbox(label="🎯 Interests", placeholder="Beach, food, culture")

    btn = gr.Button("🚀 Generate Plan")

    output = gr.Markdown()

    btn.click(
        fn=generate_trip,
        inputs=[destination, days, budget, interests],
        outputs=output
    )


# =========================
# ✅ RUN APP
# =========================
demo.launch(
    theme=gr.themes.Soft()
)