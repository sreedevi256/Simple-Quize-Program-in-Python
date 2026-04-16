
questions = [
    "1. What is the capital of India?\n a) Delhi\n b) Mumbai\n c) Chennai\n",
    "2. Which language is used for web development?\n a) Python\n b) HTML\n c) C\n",
    "3. What is 5 + 3?\n a) 6\n b) 8\n c) 9\n"
    "4. Which data type is used to store true or false values?\n a) int\n b)char\n c)boolean\n",
    "5. What will be output of:print(5+3*2)?\n a)16\n b)13\n c)11\n",
    "6. In java,which keyword is used to create an object?\n a)object\n b)new\n c)create\n",
    "7. What does CPU stand for?\n a)Central Process Unit\n b)Central Processing Unit\n c)Computer Process Unit\n",
    "8. Which Operator is Used for logical AND?\n a)&\n b)&&\n c)||\n",
    "9. Which data structurs follows FIFO?\n a)Queue\n b)Stack\n c)Tree\n",
    "10. Which of the following is not a loop?\n a)for\n b)while\n c)if\n",
    
]

answers = ['a', 'b', 'b', 'c', 'c', 'b', 'b', 'b', 'a', 'c']
score = 0
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Enter your answer (a/b/c): ").lower()
    
    if user_answer == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("Quiz Finished!")
print("Your Score:", score, "/", len(questions))
