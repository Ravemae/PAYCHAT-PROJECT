import os
from dotenv import load_dotenv
import google.generativeai as genai
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

chat_session = model.start_chat(history=[])

class ChatApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, background_color='white', padding=10))

        self.chat_display = toga.Box(style=Pack(flex=1, direction=COLUMN, background_color='black'))
        
        self.input_box = toga.TextInput(style=Pack(flex=1, padding=10))
        self.send_button = toga.Button('Send', on_press=self.send_message, style=Pack(padding=10))

        input_box_container = toga.Box(style=Pack(direction=ROW, padding=10))
        input_box_container.add(self.input_box)
        input_box_container.add(self.send_button)

        main_box.add(self.chat_display)
        main_box.add(input_box_container)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(600, 400))
        self.main_window.content = main_box
        self.main_window.show()

    def send_message(self, widget):
        user_message = self.input_box.value
        if user_message:
            user_label = toga.Label(f"[User] {user_message}", style=Pack(color='red', padding=(5, 0))) 
            self.chat_display.add(user_label)
            self.input_box.value = ''

            response = chat_session.send_message(user_message)
            ai_message = response.text

            ai_label = toga.Label(f"[AI] {ai_message}", style=Pack(color='black', padding=(5, 0)))
            self.chat_display.add(ai_label)

def main():
    return ChatApp('Sephora', 'com.Sephora')

if __name__ == '__main__':
    main().main_loop()
