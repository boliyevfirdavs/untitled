import time
from comments import categorised_comments
from ai import create_thread, create_message, run_thread, get_response, retrieve_run
import json

with open('comments.json', 'r', encoding='utf-8') as file:
    comments = json.load(file)


for i in range(0, len(comments), 20):
    try:
        thread = create_thread()
        batch = comments[i:i + 20]
        create_message(thread.id, f"{batch}")
        run = run_thread(thread.id)
        run_id = run.id
        status = retrieve_run(thread.id, run_id).status
        while not status == "completed":
            time.sleep(3)
            status = retrieve_run(thread.id, run_id).status
        string_comment = get_response(thread.id)[0][0].text.value
        categorised_comment = json.loads(string_comment)
        for j in range(len(categorised_comment)):
            categorised_comments[j]["number"] += categorised_comment[j]["number"]
            for f in range(len(categorised_comment[j]["comments"])):
                categorised_comments[j]["comments"].append(categorised_comment[j]["comments"][f])
    except:
        pass

with open('categorised_comments.json', 'w', encoding='utf-8') as f:
    json.dump(categorised_comments, f, ensure_ascii=False, indent=4)

print(categorised_comments)
