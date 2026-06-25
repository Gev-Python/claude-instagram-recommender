from agent import run_claude_agent


def main():
    print("=" * 60)
    print("DATE SERIES FINDER")
    print("Claude AI Recommendation CLI")
    print("=" * 60)
    print("Available demo profiles:")
    print("- anna")
    print("- maria")
    print("- kate")
    print()

    username = input("Enter Instagram username: ").strip()

    if not username:
        print("Error: Instagram username is required.")
        return

    print("\nStep 1: Analyzing Instagram profile...")
    print("Step 2: Detecting interests...")
    print("Step 3: Building Claude prompt...")
    print("Step 4: Generating Claude recommendation...")
    print("Step 5: Checking streaming availability...")

    result = run_claude_agent(username)

    print("\n" + "=" * 60)
    print("FINAL RECOMMENDATION")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()