questions = open('questions.txt', 'r')
question_list = [line.strip() for line in questions.readlines()]
questions.close()

score = 0;
total = len(question_list)

for line in question_list:
    q, a = line.split('=')
    ans = input(f'{q}=')
    if a == ans:
        score += 1

results = open('results.txt', 'w')
results.write(f'Your final score is {score}/{total}')
results.close()
