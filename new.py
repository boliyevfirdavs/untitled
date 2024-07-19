from ai import get_response
from comments import categorised_comments
import json

response = get_response("thread_u6HkV2cdciQp193lumNEtzor")
print(response)
for i in range(len(response)):
    categorised_comment = json.loads(response[i][0].text.value)
    for j in range(len(categorised_comment)):
        categorised_comments[j]["number"] += categorised_comment[j]["number"]
        for f in range(len(categorised_comment[j]["comments"])):
            categorised_comments[j]["comments"].append(categorised_comment[j]["comments"][f])


with open('categorised_comments.json', 'w', encoding='utf-8') as f:
    json.dump(categorised_comments, f, ensure_ascii=False, indent=4)