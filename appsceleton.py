import wikipedia
import wolframalpha
# from espeak import espeak
import os

# espeak.synth("Welcome")
os.system("espeak 'Welcome'")


while True:
    question = input("Q: ")

    try:
        #wolframalpha
        app_id = "3K7YJQ-VWA72Q6QWR"
        client = wolframalpha.Client(app_id)

        result = client.query(question)
        answer = next(result.results).text

        print(answer)
        os.system("espeak 'The answer is '" + answer)
        # espeak.synth("The answer is " + answer)

    except:
        #wikipedia
        question = question.split(' ')
        question = " ".join(question[2:])
        os.system("espeak 'Searched for '" + question)
        print(wikipedia.summary(question))