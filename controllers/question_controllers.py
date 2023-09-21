from models.question_models import fetch_questions

def get_questions():
    def build_obj(question, answer, category):
        return {'question': question,
                'answer': answer,
                'category': category}
    questions = list(map(lambda item: build_obj(*item), fetch_questions()))
    return questions
