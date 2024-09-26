# 5-shot
standard_prompt = """Use numbers and basic arithmetic operations (+ - * /) to obtain 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24
Input: 1 4 8 8
Answer: (8 / 4 + 1) * 8 = 24
Input: 5 5 5 9
Answer: 5 + 5 + 5 + 9 = 24
Input: {input}
"""

# 5-shot
cot_prompt = """Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: {input}
"""

# 1-shot
propose_prompt = """We are playing a game. I will give you an input of 4 numbers and you will list combinations of those numbers joined by some arithmetic operator: +, -, /, *. For example:

Input: 2 8 8 14

You should output:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)

Now continue. Output a list of up to 10 possible combinations, and nothing else.

Input: {input}
"""

value_prompt = """I need your help to evaluate if given numbers can reach 24 through a combination of arithmetic operators (+, -, *, /). You need to classify each number list as sure/likely/impossible. I will give you a list of numbers, and you should output 5 lines of text. The first 4 lines are a few possibilities, and the last line is a judgement (sure/likely/impossible).

For example:

Input: 11 12

You should output:
11 + 12 = 23
12 - 11 = 1
11 * 12 = 132
impossible

Now continue.

Input: {input}
"""

value_last_step_prompt = """I need your help to mark some maths homework. Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. it uses each input exactly once and no other numbers, and reach 24.

Example 1
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24

You should output:
Judge: 
sure

Example 2
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24

You should output:
Judge: 
sure

Example 3
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24

You should output:
Judge: 
sure

Example 4
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) + 1 = 25

You should output:
Judge: 
impossible

Example 5
Input: 2 9 10 12
Answer: 2 * (12 - 10) = 24

You should output:
Judge: 
impossible

Example 6
Input: 4 9 10 13
Answer: (13 - 4) * (10 - 9) = 24

You should output:
Judge: 
impossible

Now continue. Only output the judgement, and nothing else.

Input: {input}
Answer: {answer}
"""
