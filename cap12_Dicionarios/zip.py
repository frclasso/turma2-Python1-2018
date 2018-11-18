questions = ['name', 'questions', 'favorite color']
answers = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(questions,answers):
    print("What's yours {}? It's {}".format(q,a))