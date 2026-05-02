from flask import Flask, render_template, request, flash, send_file
from pathlib import Path
import os
import textwrap

# Import the existing guidelines and classes
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
            "Related to one or more subjects or areas of study within the core program and specialization",
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


app = Flask(__name__)
app.secret_key = 'project_work_secret_key_2024'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guidelines')
def guidelines():
    guidelines_text = get_guidelines_text()
    return render_template('guidelines.html', guidelines=guidelines_text)

@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        specialization = request.form.get('specialization', '').strip()
        title = request.form.get('title', '').strip()
        estimated_words = int(request.form.get('estimated_words', 0) or 0)
        estimated_abstract_words = int(request.form.get('estimated_abstract_words', 0) or 0)

        project = ProjectWork(topic, title, specialization, estimated_words, estimated_abstract_words)
        summary = project.build_summary()

        # Check validations
        title_valid = project.validate_title_length()
        report_valid = project.validate_word_count()
        abstract_valid = project.validate_abstract_word_count()

        if not (title_valid and report_valid and abstract_valid):
            flash("Some validations failed. Please check the summary below.", "warning")

        # Generate skeleton
        skeleton_path = Path(app.root_path) / 'static' / 'project_report_skeleton.md'
        project.save_skeleton(skeleton_path)

        return render_template('result.html',
                             summary=summary,
                             title_valid=title_valid,
                             report_valid=report_valid,
                             abstract_valid=abstract_valid,
                             skeleton_available=True)

    return render_template('planner.html')

@app.route('/download')
def download():
    skeleton_path = Path(app.root_path) / 'static' / 'project_report_skeleton.md'
    if skeleton_path.exists():
        return send_file(skeleton_path, as_attachment=True, download_name='project_report_skeleton.md')
    else:
        flash("Skeleton file not found. Please generate it first.", "error")
        return redirect(url_for('planner'))

if __name__ == '__main__':
    app.run(debug=True)