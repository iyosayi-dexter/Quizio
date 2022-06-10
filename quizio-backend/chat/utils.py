from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError


def decode_token(token):
    try:
        decoded_token = AccessToken(token=token, verify=True)
        return decoded_token
    except TokenError:
        return


def get_chat_name(user):
    return f'chat_{user.id}_{user.username}'


def load_message(user, id, text_data_json):
    message = {
        'id':id,
        'sender': {
            'username':user.username,
            "id":user.id
        },
        'receiver':{
            'username': text_data_json['receiver']['username'],
            'id':text_data_json['receiver']['id']
        },
        'seen':text_data_json['seen'],
        'text':  text_data_json['text'],
        'attachments': text_data_json['attachments'],
        'date_sent': text_data_json['date_sent']
    }
    return message