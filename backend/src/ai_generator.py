import os
import json

from openai import OpenAI

from typing import Dict, Any

from dotenv import load_dotenv

load_dotenv()

client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://ai.hackclub.com/proxy/v1",
    

)

def generate_challenge_with_ai(difficulty:str) -> Dict[str,Any]:

    system_prompt="""
   You are an expert coding challenge creator and senior programming instructor. 
Your task is to generate a unique, highly diverse coding multiple-choice question based on the requested difficulty level.

### Difficulty Guidelines:
- **Easy**: Focus on basic syntax, string manipulation, simple arithmetic, basic conditional statements, or basic lists/arrays.
- **Medium**: Cover intermediate concepts like loops, dictionaries/hash maps, functions, basic algorithms, or standard library features.
- **Hard**: Include advanced topics, recursion, time complexity optimization, design patterns, or complex data structures.

### Critical Rules for Variety & Randomization:
1. **High Diversity**: Never repeat the same concept or code snippet. Each generated question must test a completely different angle or sub-topic, even if the difficulty level is the same.
2. **Random Answer Placement**: Randomly distribute the `correct_answer` index (0, 1, 2, or 3) across generations. Do not keep the correct answer in a fixed or predictable position.
3. **Plausible Distractors**: Make the wrong options (distractors) realistic common mistakes that developers or students actually make.

### Formatting Instructions for "title":
- Structure the `title` cleanly by separating the question description from the code snippet using standard Markdown.
- Example format for title: "What will be the output of the following Python code?\n\n```python\n# code here\n```"

### Required JSON Output Structure:
{
    "title": "Clear description followed by a formatted Markdown code block",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer": 1, // Must be a random integer between 0 and 3
    "explanation": "Detailed, step-by-step technical explanation of why the correct answer is right and why others are wrong."
}

    """

    try:
        response=client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":f"Generate a {difficulty} difficulty coding challenge."}

            ],
            response_format={"type":"json_object"},

            temperature=0.8
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        if "correct_answer" not in challenge_data:
            for alt_key in ["correct_answer", "correct", "answer_index", "correct_index", "answer"]:
                if alt_key in challenge_data:
                    challenge_data["correct_answer"] = challenge_data[alt_key]
                    break

        required_fields = ["title", "options", "correct_answer", "explanation"]

        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field : {field}")

        challenge_data["correct_answer"] = int(challenge_data["correct_answer"])

        return challenge_data
    
    except Exception as e:
        print(e)

        return {

            "title":"Basic Python List Operation",
            "options":[
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)"
            ],

            "correct_answer":0,

            "explanation":"In Python, append() is the correct method to add an element to the end of the list."



        }