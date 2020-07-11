import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import time

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.room_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('MESSAGE:', text_data_json['message'])
        user_id = text_data_json['user_id']
        print('ID:', text_data_json['user_id'])
        time.sleep(3)
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'type': 'chat_message', 'message': message, 'user_id': user_id})

    def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']
        self.send(text_data=json.dumps({'message': message, 'user_id': user_id}))