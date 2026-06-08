def get_review_prompt(code_snippet):

    return f"""
You are a professional code reviewer.

Analyze the following code snippet.

Rules:
- Do NOT execute code.
- Identify syntax issues.
- Identify readability issues.
- Identify poor naming practices.
- Suggest improvements.

Return ONLY valid JSON.

{{
    "identified_issues": [],
    "improvement_suggestions": [],
    "code_quality_level": "",
    "review_summary": ""
}}

Code:

{code_snippet}
"""