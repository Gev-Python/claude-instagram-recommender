from mock_data import MOCK_INSTAGRAM_PROFILES, STREAMING_CATALOG


def scan_instagram_profile(username: str) -> dict:
    profile = MOCK_INSTAGRAM_PROFILES.get(username.lower())

    if not profile:
        return {
            "success": False,
            "message": "Profile not found. Try username: anna"
        }

    return {
        "success": True,
        "username": username,
        "bio": profile["bio"],
        "posts": profile["posts"],
        "interests": profile["interests"]
    }


def find_streaming_service(series_name: str) -> dict:
    for service, titles in STREAMING_CATALOG.items():
        for title in titles:
            if title.lower() == series_name.lower():
                return {
                    "available": True,
                    "series": title,
                    "service": service
                }

    return {
        "available": False,
        "series": series_name,
        "service": "Not found in Netflix, HBO or Prime mock catalog"
    }


CLAUDE_TOOLS = [
    {
        "name": "scan_instagram_profile",
        "description": "Scans an Instagram-like mock profile and returns bio, recent posts and detected interests.",
        "input_schema": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "Instagram username to analyze"
                }
            },
            "required": ["username"]
        }
    },
    {
        "name": "find_streaming_service",
        "description": "Finds which streaming service has the recommended series in the mock catalog.",
        "input_schema": {
            "type": "object",
            "properties": {
                "series_name": {
                    "type": "string",
                    "description": "Name of the TV series"
                }
            },
            "required": ["series_name"]
        }
    }
]


def execute_tool(tool_name: str, tool_input: dict) -> dict:
    if tool_name == "scan_instagram_profile":
        return scan_instagram_profile(tool_input["username"])

    if tool_name == "find_streaming_service":
        return find_streaming_service(tool_input["series_name"])

    return {"error": f"Unknown tool: {tool_name}"}