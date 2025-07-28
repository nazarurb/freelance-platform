def generate_report_prompt_from_template(input):
    chat_prompt_template = f"""<|start_of_role|>system<|end_of_role|>
Generate a concise structured report on job requests data.
Provide key statistics, trends, and insights, including:
- Total requests and category distribution.
- Average budgets and budget ranges.
- Most popular and highest-paying requests.
- Demand trends and notable shifts.
- Recommendations based on data patterns.
Ensure clarity, avoid redundant details, and keep the report well-organized.<|end_of_text|>
<|start_of_role|>user<|end_of_role|>
Job Requests Data:\n{input}<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>"""
    return chat_prompt_template


def generate_statistics_prompt_from_template(input):
    chat_prompt_template = f"""<|start_of_role|>system<|end_of_role|>
Analyze the provided job requests and generate **concise numerical statistics**
in a structured format.
Ensure the report is clear and presents key insights effectively.

Focus on:
- **Number of Requests** (total and trend: increasing/stable/decreasing).
- **Budget Distribution** (min, max, median).
- **Category Distribution** (top-requested categories, % share).
- **Keyword Frequency** (most common keywords and count).
- **Average Competition** (applications per request).

Once statistics are generated, provide a **brief summary** with key findings.
The summary should highlight notable trends in **2-3 sentences**.
<|end_of_text|>
<|start_of_role|>user<|end_of_role|>
Requests Data:\n{input}
<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>"""
    return chat_prompt_template


def generate_budget_prompt_from_template(new_request, input):
    chat_prompt_template = f"""<|start_of_role|>system<|end_of_role|>
Estimate an appropriate budget for the new job request based on past examples.
Provide the result as a JSON with a "budget" key and a numeric value.<|end_of_text|>
<|start_of_role|>user<|end_of_role|>
New Request:\n{new_request}\n\nPast Examples:\n{input}<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>"""
    return chat_prompt_template
