import json 
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class AppConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type_front']
        
        if message_type == 'DELETE':
            message_id = text_data_json['id_front']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':message_type,
                    'id':message_id
                }
            )

        elif message_type == 'PUT':
            message_id = text_data_json['id_front']
            message_content = text_data_json['message_front']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':message_type,
                    'id':message_id,
                    'message':message_content
                }
            )

        elif message_type == 'POST':
            message_content = text_data_json['message_front']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':message_type,
                    'message':message_content
                }
            )

    def DELETE(self, event):
        msg_type = event['type']
        msg_id = event['id']
        self.send(text_data=json.dumps({
            'type':msg_type,
            'id':msg_id
        }))
    def PUT(self, event):
        msg_type = event['type']
        msg_id = event['id']
        msg_content = event['message']
        self.send(text_data=json.dumps({
            'type':msg_type,
            'id':msg_id,
            'content':msg_content
        }))
    def POST(self, event):
        msg_type = event['type']
        msg_content = event['message']
        self.send(text_data=json.dumps({
            'type':msg_type,
            'content':msg_content
        }))