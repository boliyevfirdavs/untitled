from openai import OpenAI

client = OpenAI(api_key="sk-proj-rQ9p7ISGZu5Q0NLokIkMT3BlbkFJaT20MPAIYyjDHp4FNIlZ")


def create_thread():
    new_thread = client.beta.threads.create()
    return new_thread


def create_message(thread_id: str, message: str):
    thread_message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message,
    )
    return thread_message


def run_thread(thread_id: str):
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id="asst_rDnK8ZCEkeX2z4K4f8RHHeJK"
    )
    return run


def get_response(thread_id: str):
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    assistant_responses = [msg.content for msg in messages.data if msg.role == 'assistant']
    return assistant_responses


def retrieve_run(thread_id: str, run_id: str):
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )
    return run

# print(run_thread("thread_H0EnpVWkXYYAfoGCnHS4RlAi").status)

# responses = get_assistant_response("thread_H0EnpVWkXYYAfoGCnHS4RlAi")
# print(responses[0])
