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
    "topic_selection": {
        "description": "The choice of topic for the project work and the approach to be adopted needs to be based on the field of specialization. It is important to distinguish between 'project work topic' and 'project work title'. The topic is the specific area that you wish to investigate. The title may not be decided until the project work has been written so as to reflect its content properly.",
        "criteria": [
            "Relevant to business or technology, defined broadly",
            "Related to one or more of the subjects or areas of study within the core program and specialization",
            "Clearly focused so as to facilitate in-depth study, subject to the availability of adequate sources of information and to your own knowledge",
            "Of value and interest to you and your personal and professional development"
        ]
    },
    "planning": [
        "Selecting an original and relevant topic for investigation",
        "Establishing the precise focus of your study by deciding on the aims and objectives of the project work, formulating questions to be investigated, deciding the sampling techniques and statistical techniques to sum up the findings of the study. Consider very carefully what is worth investigating and its feasibility",
        "Drawing up initial project work outlines considering the aims and objectives of the project work. Workout various stages of project work"
    ],
    "submission_instructions": {
        "title_max_words": 12,
        "report_min_words": 15000,
        "report_max_words": 30000,
        "abstract_min_words": 3000,
        "abstract_max_words": 5000,
        "plagiarism_min_percent": 85,
        "guide_requirements": "Post Graduate with a minimum of 10 years of work experience",
        "certificates": [
            "From Project Guide: Certifying bonafides of project work carried out under his/her supervision",
            "From a student: Certifying that submitted project work is an original piece of work and has not been submitted earlier"
        ],
        "file_size_limit": "2MB",
        "formats": ["Portable document format (.pdf)", "Microsoft Word (.doc, .docx)"],
        "style_guide": "American Psychological Association (APA) Style guide, 6th edition",
        "formatting": {
            "font": "Times New Roman",
            "font_size": 12,
            "spacing": "Double-spaced",
            "margin": "1-inch (2.5cm) margin all around",
            "running_head": "Include a page header known as 'running head' at the top of every page",
            "spellings": "Use American spellings ('program' not 'programme'; 'center' and not 'centre'); Use 'z' spellings instead of 's' spellings (recognize, organize, summarize)"
        },
        "stages": [
            "Extended Abstract along with Guide Resume",
            "Project Report Submission along with Plagiarism Report",
            "Answer Viva Questions"
        ],
        "viva": "Viva Questions will include 5 descriptive questions related to your specific project. Viva questions are mandatory for the final project submission.",
        "evaluation_time": "Generally, it takes four to six weeks to complete the process of evaluation of project work."
    },
    "writing": {
        "extended_abstract": {
            "word_count": "3000-5000 words",
            "components": [
                "The abstract for 500-1000 words: An abstract is an overview or a brief summary of project work, which helps the reader to ascertain the purpose of carrying the project work. It acts as a stand-alone entity for the complete project work.",
                "The study hypotheses (null or alternative hypotheses, if applicable)",
                "Literature Review: Literature review (secondary sources) is the evaluation of substantive findings and theoretical and methodological contribution to a particular topic. It is a critical analysis of the previous research conducted in a particular area.",
                "Research methodology adopted: Research methodology is the implementation of methods or techniques to efficiently solve a research problem, which helps the reader to assess the validity and reliability of the study. Research methodology constitutes of: Research Design (Descriptive, Conclusive, Causal or Exploratory), Sampling Technique (Probability or Non-Probability), Data Collection (Tools used for data collection, e.g., questionnaire, survey, etc.), Data Preparation (Classification and Tabulation of data), Data Analysis (Hypotheses Testing)",
                "Results (theoretical or empirical): The findings of the study are to be summarized as: Data interpretation (Interpret and elaborate findings of the research), Recommendation (Suggestions based on critical analysis of the results)",
                "Implications of theory and practice"
            ]
        },
        "additional_notes": [
            "Mention the sources of any images, tables, figures cited or presented",
            "Figures, graphs, Tables, Appendices and References should follow the American Psychological Association (APA) Style guide, 6th edition"
        ]
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

## 2. Extended Abstract (3000-5000 words)
### 2.1 Abstract (500-1000 words)
- Overview or brief summary of the project work
- Purpose of the project work

### 2.2 Study Hypotheses
- Null or alternative hypotheses (if applicable)

### 2.3 Literature Review
- Evaluation of substantive findings and theoretical contributions
- Critical analysis of previous research

### 2.4 Research Methodology
- Research Design (Descriptive, Conclusive, Causal, or Exploratory)
- Sampling Technique (Probability or Non-Probability)
- Data Collection Tools (e.g., questionnaire, survey)
- Data Preparation (Classification and Tabulation)
- Data Analysis (Hypotheses Testing)

### 2.5 Results (Theoretical or Empirical)
- Data Interpretation
- Recommendations based on analysis

### 2.6 Implications of Theory and Practice
- Theoretical implications
- Practical implications

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
- Source list in proper citation format (APA 6th edition)

## 9. Annexures
- Plagiarism report (minimum 85% originality)
- Project guide certificate
- Student declaration
- Supporting figures and tables (with sources cited)
- Appendices
"""


class ProjectWork:
    def __init__(self, topic: str, title: str, specialization: str, estimated_words: int, estimated_abstract_words: int = 0):
        self.topic = topic.strip()
        self.title = title.strip()
        self.specialization = specialization.strip()
        self.estimated_words = estimated_words
        self.estimated_abstract_words = estimated_abstract_words

    def validate_title_length(self) -> bool:
        return len(self.title.split()) <= GUIDELINES["submission_instructions"]["title_max_words"]

    def validate_word_count(self) -> bool:
        min_words = GUIDELINES["submission_instructions"]["report_min_words"]
        max_words = GUIDELINES["submission_instructions"]["report_max_words"]
        return min_words <= self.estimated_words <= max_words

    def validate_abstract_word_count(self) -> bool:
        min_words = GUIDELINES["submission_instructions"]["abstract_min_words"]
        max_words = GUIDELINES["submission_instructions"]["abstract_max_words"]
        return min_words <= self.estimated_abstract_words <= max_words

    def build_summary(self) -> str:
        status = [
            f"Topic: {self.topic}",
            f"Title: {self.title}",
            f"Specialization: {self.specialization}",
            f"Estimated report word count: {self.estimated_words}",
            f"Estimated abstract word count: {self.estimated_abstract_words}",
            "Title length valid: " + ("Yes" if self.validate_title_length() else "No"),
            "Report word count valid: " + ("Yes" if self.validate_word_count() else "No"),
            "Abstract word count valid: " + ("Yes" if self.validate_abstract_word_count() else "No")
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
    lines.append("Selection of Project Work Topic:")
    lines.append(GUIDELINES["topic_selection"]["description"])
    lines.append("")
    lines.append("Project Topic Criteria:")
    for idx, criterion in enumerate(GUIDELINES["topic_selection"]["criteria"], 1):
        lines.append(f"  {idx}. {criterion}")
    lines.append("")
    lines.append("Planning the Project Work:")
    for idx, step in enumerate(GUIDELINES["planning"], 1):
        lines.append(f"  {idx}. {step}")
    lines.append("")
    lines.append("Writing the Project Work:")
    lines.append(f"  - Extended Abstract: {GUIDELINES['writing']['extended_abstract']['word_count']}")
    lines.append("  - Components:")
    for component in GUIDELINES["writing"]["extended_abstract"]["components"]:
        lines.append(f"    - {component}")
    for note in GUIDELINES["writing"]["additional_notes"]:
        lines.append(f"  - {note}")
    lines.append("")
    lines.append("Submission Requirements:")
    submission = GUIDELINES["submission_instructions"]
    lines.append(f"  - Max title length: {submission['title_max_words']} words")
    lines.append(f"  - Report length: {submission['report_min_words']} to {submission['report_max_words']} words")
    lines.append(f"  - Extended abstract length: {submission['abstract_min_words']} to {submission['abstract_max_words']} words")
    lines.append(f"  - Minimum originality: {submission['plagiarism_min_percent']}%")
    lines.append(f"  - Project guide requirements: {submission['guide_requirements']}")
    lines.append(f"  - File size limit: {submission['file_size_limit']}")
    lines.append(f"  - Accepted formats: {', '.join(submission['formats'])}")
    lines.append(f"  - Style guide: {submission['style_guide']}")
    lines.append(f"  - Formatting: Font {submission['formatting']['font']}, size {submission['formatting']['font_size']}, {submission['formatting']['spacing']}, {submission['formatting']['margin']}")
    lines.append(f"  - {submission['formatting']['running_head']}")
    lines.append(f"  - {submission['formatting']['spellings']}")
    lines.append("  - Essential certificates:")
    for cert in submission["certificates"]:
        lines.append(f"    - {cert}")
    lines.append("  - Submission stages:")
    for idx, stage in enumerate(submission["stages"], 1):
        lines.append(f"    {idx}. {stage}")
    lines.append(f"  - Viva: {submission['viva']}")
    lines.append(f"  - Evaluation time: {submission['evaluation_time']}")
    lines.append("  - Upload project file and answer viva questions for submission acceptance")
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
    estimated_abstract_words_input = input("Estimated extended abstract word count: ").strip()
    try:
        estimated_abstract_words = int(estimated_abstract_words_input or 0)
    except ValueError:
        estimated_abstract_words = 0

    project = ProjectWork(topic=topic, title=title, specialization=specialization, estimated_words=estimated_words, estimated_abstract_words=estimated_abstract_words)
    print("\n--- Project Validation Summary ---")
    print(project.build_summary())

    if not project.validate_title_length():
        print("\n⚠️  The title is longer than 12 words. Please shorten it.")
    if not project.validate_word_count():
        print("\n⚠️  The report word count must be between 15000 and 30000.")
    if not project.validate_abstract_word_count():
        print("\n⚠️  The abstract word count must be between 3000 and 5000.")

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
        self.abstract_words_var = tk.StringVar()

        self._add_labeled_entry(frame, "Project topic:", self.topic_var)
        self._add_labeled_entry(frame, "Field of specialization:", self.specialization_var)
        self._add_labeled_entry(frame, "Project title (≤ 12 words):", self.title_var)
        self._add_labeled_entry(frame, "Estimated report words:", self.words_var)
        self._add_labeled_entry(frame, "Estimated abstract words:", self.abstract_words_var)

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
        estimated_abstract_words = 0
        try:
            estimated_abstract_words = int(self.abstract_words_var.get().strip() or 0)
        except ValueError:
            pass

        project = ProjectWork(topic=topic, title=title, specialization=specialization, estimated_words=estimated_words, estimated_abstract_words=estimated_abstract_words)
        summary = project.build_summary()

        if not project.validate_title_length() or not project.validate_word_count() or not project.validate_abstract_word_count():
            problems = []
            if not project.validate_title_length():
                problems.append("Project title must be 12 words or fewer.")
            if not project.validate_word_count():
                problems.append("Estimated report length must be between 15000 and 30000 words.")
            if not project.validate_abstract_word_count():
                problems.append("Estimated abstract length must be between 3000 and 5000 words.")
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
