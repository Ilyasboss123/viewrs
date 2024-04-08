from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 20088743

api_hash = "17b46840f613ae250f5ac409549fbcd0"
phone = "+994707909394"

# List of source channels that you want to get messages from
source_channel_names = ['🚀CM#Analytics', '🥷CM#Shelby', '💯 CM #ADMIN']

# The channel/Group that you want to send messages to
destination_channel_link = -1001917948220

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code:'))

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title in source_channel_names:
            message = event.message

            # Forward the message to the destination channel
            await client.forward_messages(entity=destination_channel_link, messages=message)
    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit

client.start()
client.run_until_disconnected()