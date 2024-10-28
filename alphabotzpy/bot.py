import telebot
import requests

class AlphaBotzPy(telebot.TeleBot):
    def __init__(self, token, *args, **kwargs):
        super().__init__(token, *args, **kwargs)
        self.token = token

    def send_large_document(self, chat_id, file_path, caption=None):
        url = f"https://api.telegram.org/bot{self.token}/sendDocument"
        
        with open(file_path, 'rb') as file:
            response = requests.post(url, data={'chat_id': chat_id, 'caption': caption}, files={'document': file})
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
