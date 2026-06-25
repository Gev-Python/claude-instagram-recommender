import json

from claude_client import ask_claude
from prompts import SYSTEM_PROMPT
from tools import scan_instagram_profile, find_streaming_service


def build_recommendation_prompt(profile: dict) -> str:
    return f"""
Instagram profile:

Username:
{profile["username"]}

Bio:
{profile["bio"]}

Recent posts:
{profile["posts"]}

Detected interests:
{", ".join(profile["interests"])}

Available series:

- Emily in Paris
- You
- The Queen's Gambit
- The White Lotus
- Euphoria
- Big Little Lies
- Fleabag
- The Summer I Turned Pretty
- Reacher
"""


def run_claude_agent(username: str) -> str:

    profile = scan_instagram_profile(username)

    if not profile["success"]:
        return profile["message"]

    prompt = build_recommendation_prompt(profile)

    claude_response = ask_claude(
        SYSTEM_PROMPT,
        prompt
    )

    # Claude sometimes returns ```json ... ```
    clean_response = claude_response.strip()

    if clean_response.startswith("```json"):
        clean_response = clean_response[7:]

    if clean_response.startswith("```"):
        clean_response = clean_response[3:]

    if clean_response.endswith("```"):
        clean_response = clean_response[:-3]

    clean_response = clean_response.strip()

    try:
        recommendation = json.loads(clean_response)

        series = recommendation.get("series", "Unknown")

        reason = recommendation.get(
            "reason",
            "No reason provided."
        )

        date_tip = recommendation.get(
            "date_tip",
            "No date tip provided."
        )

    except Exception:

        series = clean_response

        reason = "Claude selected this series based on the profile."

        date_tip = "Create a cozy evening atmosphere and enjoy the series together."

    streaming = find_streaming_service(series)

    interests = "\n".join(
        f"- {interest}"
        for interest in profile["interests"]
    )

    return f"""
Instagram profile summary

Username:
{profile["username"]}

Detected interests:

{interests}

Recommended series:

{series}

Streaming service:

{streaming["service"]}

Why this series fits:

{reason}

Date-night suggestion:

{date_tip}

Technical note:

Claude API generates the recommendation.

Python tools analyze the mock Instagram profile and determine streaming availability.
"""