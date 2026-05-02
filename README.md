# Project Work Utility

This Python utility helps students plan and validate a project work proposal based on comprehensive academic submission guidelines.

## Features

- Built-in project guidelines including writing instructions, formatting, and submission stages
- Validates title length (maximum 12 words)
- Validates estimated report length (15,000 to 30,000 words)
- Validates estimated abstract length (3,000 to 5,000 words)
- Generates a detailed markdown project report skeleton with extended abstract structure
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

- `project_report_skeleton.md` is generated in the project folder with a complete structure including:
  - Title page
  - Extended abstract (with subsections for abstract, hypotheses, literature review, methodology, results, implications)
  - Introduction, Literature Review, Methodology, Analysis, Conclusion, References, Annexures

## Guidelines Covered

- Project Based Learning objectives
- Topic selection and criteria
- Planning steps
- Writing requirements (extended abstract components)
- Submission instructions (stages, viva, certificates)
- Formatting (APA 6th edition, font, spacing, etc.)
- File size and format requirements