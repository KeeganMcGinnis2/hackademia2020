import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import time

# DELAYS = {'MERCURY': 190, 'VENUS': 360, 'EARTH': 496, 'MARS': 756, 'JUPITER':, 'SATURN':, 'URANUS':, 'NEPTUNE':, 'PLUTO': }

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
        user_id = text_data_json['user_id']
        planet = text_data_json['planet']
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'type': 'chat_message', 'message': message, 'user_id': user_id, 'planet': planet})

    def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']
        planet = event['planet']
        self.send(text_data=json.dumps({'message': message, 'user_id': user_id, 'planet': planet}))