import argparse
import textwrap
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

GUIDELINES = {
    "overview": "Project Based Learning is the application of a comprehensive methodology to inculcate the spirit of strategizing industry operations in a real-time environment.",
    "objectives": [
        "Develop conceptual skills",
        "Develop analytical skills",
        "Develop communication skills",
        "Develop interpersonal skills"
    ],
    "topic_criteria": [
        "Relevant to business or technology, defined broadly",
        "Related to one or more subjects or areas of study within the core program and specialization",
        "Clearly focused for in-depth study",
        "Supported by adequate sources of information and your own knowledge",
        "Of value and interest to you and your personal and professional development"
    ],
    "submission": {
        "title_max_words": 12,
        "report_min_words": 15000,
        "report_max_words": 30000,
        "plagiarism_min_percent": 85,
        "guide_requirements": "Post Graduate with a minimum of 10 years of work experience"
    }
}

PROJECT_SKELETON = """
# Project Report Template

## 1. Title Page
- Project Title
- Student Name
- Institution
- Project Guide Name
- Submission Date

## 2. Extended Abstract
- Brief summary of the project
- Objectives and scope
- Key findings and recommendations

## 3. Introduction
- Background of the topic
- Problem statement
- Purpose of the study
- Scope and limitations

## 4. Literature Review
- Related theories and models
- Prior research and industry references
- Relevance to specialization

## 5. Research Methodology
- Aims and objectives
- Research questions
- Sampling techniques
- Data collection methods
- Statistical techniques used

## 6. Analysis and Findings
- Data analysis
- Results and discussion
- Interpretation of findings

## 7. Conclusion and Recommendations
- Summary of findings
- Practical implications
- Recommendations for stakeholders

## 8. References
- Source list in proper citation format

## 9. Annexures
- Plagiarism report
- Project guide certificate
- Student declaration
- Supporting figures and tables
"""


class ProjectWork:
    def __init__(self, topic: str, title: str, specialization: str, estimated_words: int):
        self.topic = topic.strip()
        self.title = title.strip()
        self.specialization = specialization.strip()
        self.estimated_words = estimated_words

    def validate_title_length(self) -> bool:
        return len(self.title.split()) <= GUIDELINES["submission"]["title_max_words"]

    def validate_word_count(self) -> bool:
        min_words = GUIDELINES["submission"]["report_min_words"]
        max_words = GUIDELINES["submission"]["report_max_words"]
        return min_words <= self.estimated_words <= max_words

    def build_summary(self) -> str:
        status = [
            f"Topic: {self.topic}",
            f"Title: {self.title}",
            f"Specialization: {self.specialization}",
            f"Estimated word count: {self.estimated_words}",
            "Title length valid: " + ("Yes" if self.validate_title_length() else "No"),
            "Word count valid: " + ("Yes" if self.validate_word_count() else "No")
        ]
        return "\n".join(status)

    def save_skeleton(self, output_path: Path) -> Path:
        output_path.write_text(PROJECT_SKELETON.strip() + "\n", encoding="utf-8")
        return output_path


def get_guidelines_text() -> str:
    lines = ["PROJECT BASED LEARNING GUIDELINES", ""]
    lines.append(GUIDELINES["overview"])
    lines.append("")
    lines.append("Objectives:")
    for idx, objective in enumerate(GUIDELINES["objectives"], 1):
        lines.append(f"  {idx}. {objective}")
    lines.append("")
    lines.append("Project Topic Criteria:")
    for idx, criterion in enumerate(GUIDELINES["topic_criteria"], 1):
        lines.append(f"  {idx}. {criterion}")
    lines.append("")
    lines.append("Submission Requirements:")
    submission = GUIDELINES["submission"]
    lines.append(f"  - Max title length: {submission['title_max_words']} words")
    lines.append(f"  - Report length: {submission['report_min_words']} to {submission['report_max_words']} words")
    lines.append(f"  - Minimum originality: {submission['plagiarism_min_percent']}%")
    lines.append(f"  - Project guide requirements: {submission['guide_requirements']}")
    lines.append("  - Upload project file and answer viva questions for submission acceptance")
    lines.append("  - Evaluation typically takes 4-6 weeks")
    return "\n".join(lines)


def run_cli() -> None:
    print(textwrap.fill(get_guidelines_text(), width=80))
    print("\nEnter your project details below:\n")
    topic = input("Project topic: ").strip()
    specialization = input("Field of specialization: ").strip()
    title = input("Proposed project title (<= 12 words): ").strip()
    estimated_words_input = input("Estimated project report word count: ").strip()
    try:
        estimated_words = int(estimated_words_input or 0)
    except ValueError:
        estimated_words = 0

    project = ProjectWork(topic=topic, title=title, specialization=specialization, estimated_words=estimated_words)
    print("\n--- Project Validation Summary ---")
    print(project.build_summary())

    if not project.validate_title_length():
        print("\n⚠️  The title is longer than 12 words. Please shorten it.")
    if not project.validate_word_count():
        print("\n⚠️  The word count must be between 15000 and 30000.")

    output_file = Path.cwd() / "project_report_skeleton.md"
    project.save_skeleton(output_file)
    print(f"\n✅ Project skeleton saved to: {output_file}")
    print("You can use this template to start writing your 15,000–30,000 word report.")


class ProjectWorkApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Project Work Planner")
        root.geometry("640x520")
        root.resizable(False, False)

        self._build_widgets()

    def _build_widgets(self) -> None:
        heading = tk.Label(self.root, text="Project Work Planner", font=("Segoe UI", 16, "bold"))
        heading.pack(pady=(16, 8))

        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=20)

        self.topic_var = tk.StringVar()
        self.specialization_var = tk.StringVar()
        self.title_var = tk.StringVar()
        self.words_var = tk.StringVar()

        self._add_labeled_entry(frame, "Project topic:", self.topic_var)
        self._add_labeled_entry(frame, "Field of specialization:", self.specialization_var)
        self._add_labeled_entry(frame, "Project title (≤ 12 words):", self.title_var)
        self._add_labeled_entry(frame, "Estimated report words:", self.words_var)

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=20, pady=(12, 8))

        validate_button = tk.Button(button_frame, text="Validate & Save", command=self._validate_and_save)
        validate_button.pack(side="left", padx=(0, 8), ipadx=8)

        guidelines_button = tk.Button(button_frame, text="Show Guidelines", command=self._show_guidelines)
        guidelines_button.pack(side="left", ipadx=8)

        self.summary_text = tk.Text(self.root, height=11, wrap="word", state="disabled", padx=10, pady=10)
        self.summary_text.pack(fill="both", padx=20, pady=(8, 16), expand=True)

        notice = tk.Label(self.root, text="Saved skeleton file: project_report_skeleton.md", fg="#2563EB")
        notice.pack(pady=(0, 8))

    def _add_labeled_entry(self, parent: tk.Widget, label_text: str, text_var: tk.StringVar) -> None:
        row = tk.Frame(parent)
        row.pack(fill="x", pady=6)
        label = tk.Label(row, text=label_text, width=24, anchor="w")
        label.pack(side="left")
        entry = tk.Entry(row, textvariable=text_var)
        entry.pack(side="left", fill="x", expand=True)

    def _show_guidelines(self) -> None:
        dialog = tk.Toplevel(self.root)
        dialog.title("Guidelines")
        dialog.geometry("680x520")
        dialog.resizable(False, False)

        text_area = tk.Text(dialog, wrap="word", padx=10, pady=10)
        text_area.insert("1.0", get_guidelines_text())
        text_area.config(state="disabled")
        text_area.pack(fill="both", expand=True)

    def _validate_and_save(self) -> None:
        topic = self.topic_var.get().strip()
        specialization = self.specialization_var.get().strip()
        title = self.title_var.get().strip()
        estimated_words = 0
        try:
            estimated_words = int(self.words_var.get().strip() or 0)
        except ValueError:
            pass

        project = ProjectWork(topic=topic, title=title, specialization=specialization, estimated_words=estimated_words)
        summary = project.build_summary()

        if not project.validate_title_length() or not project.validate_word_count():
            problems = []
            if not project.validate_title_length():
                problems.append("Project title must be 12 words or fewer.")
            if not project.validate_word_count():
                problems.append("Estimated report length must be between 15000 and 30000 words.")
            messagebox.showwarning("Validation issue", "\n".join(problems))

        output_file = Path.cwd() / "project_report_skeleton.md"
        project.save_skeleton(output_file)
        messagebox.showinfo("Saved", f"Project skeleton saved to:\n{output_file}")
        self._update_summary(summary)

    def _update_summary(self, summary: str) -> None:
        self.summary_text.config(state="normal")
        self.summary_text.delete("1.0", "end")
        self.summary_text.insert("1.0", summary)
        self.summary_text.config(state="disabled")


def main() -> None:
    parser = argparse.ArgumentParser(description="Project Work Planner")
    parser.add_argument("--cli", action="store_true", help="Run the command-line interaction")
    args = parser.parse_args()

    if args.cli:
        run_cli()
    else:
        try:
            root = tk.Tk()
            ProjectWorkApp(root)
            root.mainloop()
        except tk.TclError:
            print("GUI is not available. Falling back to CLI mode.")
            run_cli()


if __name__ == "__main__":
    main()
