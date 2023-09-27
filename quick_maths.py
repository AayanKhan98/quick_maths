import random
import time 

Operators = ["+", "-", "*"]
min_operand = 2
max_operand = 12
Total_problems = 10

def gen_prob():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(Operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press any button to Start Timed Test!")
print("------Timer Start------")

s_time = time.time()

for i in range(Total_problems):
    expr, answer = gen_prob()
    while True:
        attempt = input("problem #" + str(i+1) + ": " + expr + " = ")
        if attempt == str(answer):
            break

e_time = time.time()
T_time = round(e_time - s_time, 2)

print("------Test Complete------")
print("Your time was ", T_time "Seconds")