import os
from line import LineBotApi
from line.models import TextSendMessage

# LINE Messaging APIのアクセストークンと送信先ユーザーIDを設定
CHANNEL_ACCESS_TOKEN = os.environ['YOUR_CHANNEL_ACCESS_TOKEN']
USER_ID = os.environ['RECIPIENT_USER_ID']

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# メッセージを送信
try:
    line_bot_api.push_message(USER_ID, TextSendMessage(text='Hello, this is a message from my LINE bot!'))
    print("Message sent successfully.")
except Exception as e:
    print(f"Error sending message: {e}")
