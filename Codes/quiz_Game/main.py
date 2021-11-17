from data import question_data
class Question:
    def __init__(self , text , ans) -> None:
        self.text = text
        self.ans =ans
        
# new_q = Question(question_data[0]['text'] , question_data[0]['answer']) 
# print(new_q.text)
# print(new_q.ans)

question_bank= []
for question  in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_q = Question(question_text , question_answer)
    question_bank.append(new_q)

