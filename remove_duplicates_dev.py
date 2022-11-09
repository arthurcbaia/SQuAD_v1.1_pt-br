import json
with open("dev-v1.1.json", encoding="utf-8") as f:
    data = json.load(f)['data']


# remove duplicates from dev set using the question id 
# (the same question can appear in multiple contexts)

questions = set()
new_data = []
for article in data:
    new_paragraphs = []
    for paragraph in article['paragraphs']:
        new_qas = []
        for qa in paragraph['qas']:
            if qa['id'] not in questions:
                questions.add(qa['id'])
                new_qas.append(qa)
        if new_qas:
            paragraph['qas'] = new_qas
            new_paragraphs.append(paragraph)
    if new_paragraphs:
        article['paragraphs'] = new_paragraphs
        new_data.append(article)

with open("dev-v1.1.json", "w", encoding="utf-8") as f:
    json.dump({'data': new_data}, f)
