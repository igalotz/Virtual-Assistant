import wolframalpha

input = input("Question: ")

app_id = "3K7YJQ-VWA72Q6QWR"
client = wolframalpha.Client(app_id)

result = client.query(input)
answer = next(result.results).text

print(answer)