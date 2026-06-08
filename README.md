# Code-Review-Generator
# Code Review Feedback Generator

An AI-powered Code Review Feedback Generator built using **Google Gemini**, **Streamlit**, and **Langfuse**. This application analyzes code snippets and provides structured feedback on code quality, readability, syntax issues, and improvement suggestions without executing the code.

## Features

* Analyze code snippets using Google Gemini
* Detect potential syntax and formatting issues
* Suggest code quality improvements
* Provide structured JSON feedback
* Interactive Streamlit web interface
* Langfuse integration for observability and tracing
* Safe analysis without code execution

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* Langfuse
* Python Dotenv

## Project Structure

```text
Code Review Generator/
│
├── app.py
├── reviewer.py
├── prompt.py
├── langfuse_config.py
├── requirements.txt
├── .env
└── README.md
```

## Output Format

```json
{
  "identified_issues": [
    "string"
  ],
  "improvement_suggestions": [
    "string"
  ],
  "code_quality_level": "High | Medium | Low",
  "review_summary": "string"
}
```

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/code-review-feedback-generator.git
cd code-review-feedback-generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

##  Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

##  Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Example Input

```python
for i in range(5):
print(i)
```

## Example Output

```json
{
  "identified_issues": [
    "The print statement is not properly indented inside the loop."
  ],
  "improvement_suggestions": [
    "Indent the print statement so it becomes part of the loop body."
  ],
  "code_quality_level": "Low",
  "review_summary": "The snippet contains an indentation issue that will cause a syntax error."
}
```

## Langfuse Integration

This project uses Langfuse for:

* Tracing AI requests
* Monitoring model interactions
* Observability
* Performance tracking
* Debugging LLM responses

## Safety

* The application does not execute user code.
* Analysis is performed only on the provided code snippet.
* Prevents execution-related security risks.

## Future Enhancements

* Support for multiple programming languages
* Code quality scoring system
* Downloadable review reports
* User feedback collection
* Syntax highlighting
* Batch code review support

## Author

Praveen Reddy

##  License

This project is licensed under the MIT License.
