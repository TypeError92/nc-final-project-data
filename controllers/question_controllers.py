import ast
import openai
import os
from models import fetch_answers, fetch_questions, insert_questions
from controllers.utils import is_good_anagram


def get_questions():
    def build_obj(question, answer, category):
        return {'question': question,
                'answer': answer,
                'category': category}
    questions = list(map(lambda item: build_obj(*item), fetch_questions()))
    return questions


def get_new_questions():
    answers = [answer for (answer,) in fetch_answers()]
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user",
             "content":
                 """You will be provided with an array of movie titles.
                 Map over the array and return an anagram of each individual item in the array.
                 Each anagram must use all the letters in the individual item.
                 Do not repeat input words in the output.
                 Do not use any profanity.
                 All anagrams returned must be words listed in the Oxford English Dictionary"""},
            {"role": "user",
             "content": str(answers)}
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print('Response:', response['choices'][0]['message']['content'])
    anagrams = ast.literal_eval(response['choices'][0]['message']['content'])
    questions = list(zip(anagrams, answers))
    print('Questions received from AI:', questions)
    questions = list(filter(is_good_anagram, questions))
    print('Valid questions:', questions)
    inserted_questions = insert_questions(questions)
    print('Inserted questions:', inserted_questions)
    return inserted_questions
