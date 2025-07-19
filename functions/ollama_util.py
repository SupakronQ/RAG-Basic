import ollama

class OllamaChatClient:
    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name
        self.messages = []

    def set_system_prompt(self, prompt):
        self.messages.append({"role": "system", "content": prompt})

    def send_user_prompt(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=self.messages
            )
            # เพิ่มข้อความของ assistant เข้าไปใน history
            self.messages.append({"role": "assistant", "content": response['message']['content']})
            return response['message']['content']
        except Exception as e:
            return f"Error: {e}"

    def reset_chat(self):
        self.messages = []
