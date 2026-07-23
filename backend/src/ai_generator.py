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



    """

    try:
        response=client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":f"Generate a {difficulty} difficulty coding challenge."}

            ],
            response_format={"type":"json_object"},

            temperature=0.5
        )

        content=response.choices[0].message.content
        challenge_data=json.loads(content)

        required_fields=["title","options","correct_answer_id","explanation"]

        for field in required_fields:


            if field not in challenge_data:

                raise ValueError(f"Missing required field : {field}")

            

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

            "correct_answer_id":0,

            "explanation":"In Python, append() is the correct method to add an element to the end of the list."



        }