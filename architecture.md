# Architecture

## Overview

Date Series Finder is a CLI-based Claude AI Agent demo.

The application recommends a TV series for a date night based on Instagram-like profile data and checks where the series is available.

                User

                  │

                  ▼

        main.py (CLI)

                  │

                  ▼

      scan_instagram_profile()

                  │

                  ▼

        Build Claude Prompt

                  │

                  ▼

           Claude API

                  │

                  ▼

      Recommended TV Series

                  │

                  ▼

      find_streaming_service()

                  │

                  ▼

        Final Console Output

## Components

### main.py

CLI entry point.  
Receives username and prints the final result.

### agent.py

Coordinates the application flow:
- scans profile data
- builds Claude prompt
- sends request to Claude
- receives recommended series
- checks streaming availability
- returns final recommendation

### tools.py

Contains application skills/tools:
- scan_instagram_profile
- find_streaming_service

### prompts.py

Contains Claude system prompt.

### claude_client.py

Handles Claude API communication.

### mock_data.py

Contains mock Instagram-like profiles and mock streaming catalog.

## Privacy Note

The application does not scrape real Instagram profiles.  
Mock data is used to avoid privacy and platform policy issues.

## Future Improvements

- Add real Instagram data source
- Add real streaming availability API
- Add structured JSON output
- Add tests
- Add Claude Tool Use implementation