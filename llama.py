import ollama

# setting up the role and comntent of ollama:
messages = [
    {
        'role': 'system',
        'content': 'You are a guest, and the user will tell you a topic to debate on. You can debate on that topic with the user.'
    }
    
]

def truncate_response(response_text, max_words=50):
    words = response_text.split()
    if len(words) > max_words:
        return ' '.join(words[:max_words]) + '...'
    return response_text
while True:
   
    user_input = input("You: ")

    messages.append({'role': 'user', 'content': user_input})

    response = ollama.chat(model='llama3.1', messages=messages)
    
    ai_response = response['message']['content']
    truncated_response = truncate_response(ai_response, max_words=50)
    print(f"AI: {truncated_response}")
    
    messages.append({'role': 'assistant', 'content': truncated_response})