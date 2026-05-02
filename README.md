# Project Work Utility

This Python utility helps students plan and validate a project work proposal based on typical academic submission guidelines.

## Features

- Built-in project guidelines
- Validates title length (maximum 12 words)
- Validates estimated report length (15,000 to 30,000 words)
- Generates a markdown project report skeleton
- Supports both GUI and CLI interaction

## Usage

### GUI mode (recommended)

```powershell
python project_ready.py
```

A window will open where you can enter project details, view guidelines, validate input, and save the report skeleton.

### CLI mode

```powershell
python project_ready.py --cli
```

Follow the prompts in the terminal.

## Output

- `project_report_skeleton.md` is generated in the project folder
