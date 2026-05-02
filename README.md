# Project Work Utility

This Python utility helps students plan and validate a project work proposal based on comprehensive academic submission guidelines.

## Features

- Built-in project guidelines including writing instructions, formatting, and submission stages
- Validates title length (maximum 12 words)
- Validates estimated report length (15,000 to 30,000 words)
- Validates estimated abstract length (3,000 to 5,000 words)
- Generates a detailed markdown project report skeleton with extended abstract structure
- Supports GUI, CLI, and Web interfaces

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Desktop GUI (recommended)
```powershell
python project_ready.py
```

### Command Line Interface
```powershell
python project_ready.py --cli
```

### Web Application (Local)
```powershell
python app.py
```
Then open http://127.0.0.1:5000 in your browser.

## 🚀 Deploy to Live Server

### Option 1: Heroku (Recommended - Free)

1. **Install Heroku CLI**:
   - Download from: https://devcenter.heroku.com/articles/heroku-cli
   - Or use npm: `npm install -g heroku`

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create Heroku App**:
   ```bash
   cd "C:\Users\Mr.Harry\Desktop\PROJECT WORK"
   heroku create your-app-name
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

5. **Open your live app**:
   ```bash
   heroku open
   ```

### Option 2: PythonAnywhere (Free)

1. Go to https://www.pythonanywhere.com/
2. Create account and upload your files
3. Set up web app with Flask
4. Configure WSGI file pointing to your `app` object

### Option 3: Vercel (Free)

1. Install Vercel CLI: `npm install -g vercel`
2. Login: `vercel login`
3. Deploy: `vercel`
4. Follow prompts

## Web App Features

- **Home Page**: Overview and navigation
- **Guidelines**: Complete project work guidelines
- **Project Planner**: Form-based project validation and skeleton generation
- **Download**: Generated report skeleton download

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