import ast
import openai
import os
from models import fetch_answers, fetch_questions, insert_questions
from controllers.utils import is_good_anagram

"""
Unfortunately, this code is not used in the final version. Our goal was to dynamically generate new questions by
feeding answers from our database to an OpenAI model and have it find matching anagrams. However, we had to find
that the model did not return enough usable results no matter what prompt was used or how often it was corrected.
Most suggestions were not anagrams at all, others merely switched the order of *words* in the input without changing
the order of *letters* within or between words; the overall success rate was below 10%. We therefore decided to drop
the idea for the time being and build our own database of questions. With more time, we would have liked to look into
training our own model specifically for the purpose of generating anagrams.

We decided to leave the code in this repo for illustrative purposes and in case we get to keep working on this project
in the future.
"""


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
