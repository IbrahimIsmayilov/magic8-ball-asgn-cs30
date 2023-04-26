# Magic 8 Ball Asgn By Ibrahim Ismayilov

# Used to generate a random response from the magic 8 ball
import random

# Check user input for any set questions
def checkQuestion(question):
    if question == "":
        return "Please ask a question..."
    elif question == "Does a magic 8 ball actually work?":
        return "How dare you doubt me!"
    elif question == "Is Javascript awesome?":
        return "Of Course!"
    else:
        return ""

# Generating a random response
def randomResponse():
    # Randomizing the results
    num = random.randint(1, 10)
    if num > 8:
        return "Without a Doubt."
    elif num > 6:
        return "As I see it, yes."
    elif num > 4:
        return "Concentrate and ask again."
    elif num > 2:
        return "Don't count on it."
    else: 
        return "Outlook not so good."

# Main Program Loop
loop = True
while loop:
    # Print Main Menu
    # Get user input
    question = input("\nQuestion: ")
    # Check for any set question
    questionResponse = checkQuestion(question)
    if questionResponse == "":
        questionResponse = randomResponse()
       
    print(questionResponse)