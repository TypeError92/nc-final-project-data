import ast
import openai
import os
from models import fetch_answers, fetch_questions
from controllers.utils import is_anagram, is_good_anagram


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
                 "You will be provided with an array of movie titles. Map over the array and return an anagram of each individual item in the array. \nEach anagram must use all the letters in the individual item.  \ndo not repeat input words in the output. Do not use any profanity. All anagrams returned must be words listed in the Oxford English Dictionary"},
            {"role": "user",
             "content": str(answers)}
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    anagrams = ast.literal_eval(response['choices'][0]['message']['content'])
    question_answer_pairs = zip(anagrams, answers)
    question_answer_pairs = filter(is_anagram, question_answer_pairs)
    question_answer_pairs = list(filter(is_good_anagram, question_answer_pairs))
    print(question_answer_pairs)