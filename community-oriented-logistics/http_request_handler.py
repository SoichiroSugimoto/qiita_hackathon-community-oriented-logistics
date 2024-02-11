import json
import rds_connect
import adobe_sign
import os
from line import LineBotApi
from line.exceptions import LineBotApiError
from line.models import MessageEvent, TextMessage, TextSendMessage

# 環境変数からアクセストークンとシークレットを取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ['YOUR_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET = os.environ['YOUR_CHANNEL_SECRET']

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def lambda_handler(event, context):
    # LINEからのWebhookイベントを解析
    body = json.loads(event['body'])
    events = body['events']
    
    for event in events:
        # メッセージイベントの場合
        if event['type'] == 'message':
            reply_token = event['replyToken']
            message_type = event['message']['type']
            
            # テキストメッセージの場合
            if message_type == 'text':
                user_message = event['message']['text']
                
                # ユーザーからのメッセージに基づいて応答を変更することも可能
                reply_message = TextSendMessage(text=f"You said: {user_message}")
                rds_connect.create_item("John Doe", 30)
                rds_connect.read_item("John Doe")
                rds_connect.update_item("John Doe", 31)
                rds_connect.delete_item("John Doe")
                adobe_sign.sign(event, context)
                
                try:
                    line_bot_api.reply_message(reply_token, reply_message)
                except LineBotApiError as e:
                    print(f"Error: {e}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Webhook processed successfully')
    }