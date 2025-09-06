import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message, UserProfile

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Update user status
        await self.update_user_status(True)

        # Notify group about new user
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_join',
                'username': self.user.username,
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Update user status
        await self.update_user_status(False)

        # Notify group about user leaving
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_leave',
                'username': self.user.username,
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save message to database
        await self.save_message(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'username': username,
        }))

    async def user_join(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_join',
            'username': event['username'],
        }))

    async def user_leave(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_leave',
            'username': event['username'],
        }))

    @database_sync_to_async
    def save_message(self, message):
        room = Room.objects.get(name=self.room_name)
        Message.objects.create(
            room=room,
            user=self.user,
            content=message
        )

    @database_sync_to_async
    def update_user_status(self, online):
        profile, created = UserProfile.objects.get_or_create(user=self.user)
        profile.online = online
        profile.save()
