import wikipedia


while True:
    question = input("Q: ")
    wikipedia.set_lang("pl")
    print(wikipedia.summary(question, sentences=2))