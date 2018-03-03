from .user import User
import requests
from .exceptions import APIExceptions

class Bot(User):
    def __init__(self, token):
        self.__token = token

    @property
    def token(self):
        return self.__token

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, id):
        self.__id = id

    def endpoint(self, entry=''):
        return 'https://api.telegram.org/bot{token}/{query}'.format(token=self.token, entry=entry)

    def get(self, endpoint, keys=[], **kwargs):
        if len(kwargs) > 0:
            query = '?'
            valid_kwargs = [key for key in keys and key in kwargs]
            for index, key in valid_kwargs:
                query += '{key}={value}'.format(key=key, value=kwargs[key])
                if index < len(valid_kwargs) - 1:
                    query += '&'
        r = requests.get(self.endpoint(endpoint) + query)
        if r['ok']:
            return r
        else:
            raise APIExceptions(r)

    def post(self, endpoint, attributes=[], **kwargs):
        json = {attr: kwargs.pop(attr, None) for attr in attributes}
        r = requests.post(self.endpoint(endpoint), json=json)
        if r['ok']:
            return r
        else:
            raise APIExceptions(r)
    
    def getMe(self):
        r = self.get('getMe')
        self.json_init(r['result'])
        return r['result']
        
    def sendMessage(self, chat_id, text, **kwargs):
        return self.post('sendMessage', ['chat_id', 'text', 'parse_mode', 'disable_web_page_preview', 'disable_notification', 'reply_to_message_id', 'reply_markup'], 
                             chat_id=chat_id, text=text, **kwargs)

    def forwardMessage(self, chat_id, from_chat_id, message_id, **kwargs):
        return self.post('forwardMessage', ['chat_id', 'from_chat_id', 'message_id', 'disable_notification'], 
                             chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id, **kwargs)

    def sendPhoto(self, chat_id, photo, **kwargs):
        return self.post('sendPhoto', ['chat_id', 'photo', 'caption', 'parse_mode', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                             chat_id=chat_id, photo=photo, **kwargs)
        
    def sendAudio(self, chat_id, audio, **kwargs):
        return self.post('sendAudio', ['chat_id', 'audio', 'caption', 'parse_mode', 'performer', 'title', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                             chat_id=chat_id, audio=audio, **kwargs)

    def sendDocument(self, chat_id, document, **kwargs):
        return self.post('sendAudio', ['chat_id', 'audio', 'caption', 'parse_mode', 'disable_notification', 'reply_to_message_id', 'reply_markup'], 
                             chat_id=chat_id, document=document, **kwargs)

    def sendVideo(self, chat_id, video, **kwargs):
        return self.post('sendVideo', ['chat_id', 'video', 'duration', 'width', 'height', 'caption', 'supports_streaming', 'parse_mode', 'disable_web_page_preview', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                             chat_id=chat_id, video=video, **kwargs)
        
    def sendVoice(self, chat_id, voice, **kwargs):
        return self.post('sendVoice', ['chat_id', 'audio', 'caption', 'parse_mode', 'duration', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                             chat_id=chat_id, voice=voice, **kwargs)

    def sendVideoNote(self, chat_id, video_note, **kwargs):
        return self.post('sendVideoNote', ['chat_id', 'video_note', 'length', 'parse_mode', 'duration', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                             chat_id=chat_id, video_note=video_note, **kwargs)

    def sendMediaGroup(self, chat_id, media, **kwargs):
        return self.post('sendMediaGroup', ['chat_id', 'media', 'disable_notification', 'reply_to_message_id'],
                             chat_id=chat_id, media=media, **kwargs)

    def sendLocation(self, chat_id, latitude, longitude, **kwargs):
        return self.post('sendLocation', ['chat_id', 'latitude', 'longitude', 'live_period', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                             chat_id=chat_id, latitude=latitude, longitude=longitude, **kwargs)

    def editMessageLiveLocation(self, latitude, longitude, **kwargs):
        return self.post('editMessageLiveLocation', ['chat_id', 'message_id', 'inline_message_id', 'latitude', 'longitude', 'reply_markup'],
                         latitude=latitude, longitude=longitude, **kwargs)

    def stopMessageLiveLocation(self, **kwargs):
        return self.post('stopMessageLiveLocation', ['chat_id', 'message_id', 'inline_message_id', 'reply_markup'], **kwargs)

    def sendVenue(self, chat_id, latitude, longitude, title, address, **kwargs):
        return self.post('sendVenue', ['chat_id', 'latitude', 'longitude', 'title', 'address', 'foursquare_id', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                         chat_id=chat_id, latitude=latitude, longitude=longitude, title=title, address=address, **kwargs)

    def sendContact(self, chat_id, phone_number, first_name, **kwargs):
        return self.post('sendContact', ['chat_id', 'phone_number', 'first_name', 'last_name', 'disable_notification', 'reply_to_message_id', 'reply_markup'],
                         chat_id=chat_id, phone_number=phone_number, first_name=first_name, **kwargs)

    def sendChatAction(self, chat_id, action):
        return self.post('sendChatAction', ['chat_id', 'action'], chat_id=chat_id, action=action)

    def getUserProfilePhotos(self, user_id, **kwargs):
        return self.get('getUserProfilePhotos', ['user_id', 'offset', 'limit'], user_id=user_id, **kwargs)

    def getFile(self, file_id):
        return self.get('getFile', ['file_id'], file_id=file_id)

    def kickChatMember(self, chat_id, user_id, until_date=None):
        return self.post('kickChatMember', ['chat_id', 'user_id'], chat_id=chat_id, user_id=user_id, until_date=until_date)

    def unbanChatMember(self, chat_id, user_id):
        return self.post('unbanChatMember', ['chat_id', 'user_id'], chat_id=chat_id, user_id=user_id)

    def restrictChatMember(self, chat_id, user_id, **kwargs):
        return self.post('restrictChatMember', ['chat_id', 'user_id', 'can_send_messages', 'can_send_media_messages', 'can_send_other_messages', 'can_add_web_page_previews'], chat_id=chat_id, user_id=user_id, **kwargs)

    def promoteChatMember(self, chat_id, user_id, **kwargs):
        return self.post('promoteChatMember', ['chat_id', 'user_id', 'can_change_info', 'can_post_messages', 'can_edit_messages', 'can_delete_messages', 'can_invite_users', 'can_restrict_members', 'can_pin_messages', 'can_promote_members'], chat_id=chat_id, user_id=user_id, **kwargs)

    def exportChatInviteLink(self, chat_id):
        return self.get('exportChatInviteLink', ['chat_id'], chat_id=chat_id)

    def setChatPhoto(self, chat_id, photo):
        return self.post('setChatPhoto', ['chat_id', 'photo'], chat_id=chat_id, photo=photo)

    def deleteChatPhoto(self, chat_id):
        return self.post('deleteChatPhoto', ['chat_id'], chat_id=chat_id)

    def setChatTitle(self, chat_id, title):
        return self.post('setChatTitle', ['chat_id', 'title'], chat_id=chat_id, title=title)

    def setChatDescription(self, chat_id, description):
        return self.post('setChatDescription', ['chat_id', 'description'], chat_id=chat_id, description=description)
        
    def pinChatMessage(self, chat_id, message_id, disable_notification=None):
        return self.post('pinChatMessage', ['chat_id', 'message_id', 'disable_notification'], chat_id=chat_id, message_id=message_id, disable_notification=disable_notification)

    def unpinChatMessage(self, chat_id):
        return self.get('unpinChatMessage', ['chat_id'], chat_id=chat_id)

    def leaveChat(self, chat_id):
        return self.get('leaveChat', ['chat_id'], chat_id=chat_id)
    
    def getChat(self, chat_id):
        return self.get('getChat', ['chat_id'], chat_id=chat_id)

    def getChatAdministrators(self, chat_id):
        return self.get('getChatAdministrators', ['chat_id'], chat_id=chat_id)

    def getChatMembersCount(self, chat_id):
        return self.get('getChatMembersCount', ['chat_id'], chat_id=chat_id)
     
    def getChatMember(self, chat_id, user_id):
        return self.get('getChatMember', ['chat_id', 'user_id'], chat_id=chat_id, user_id=user_id)

    def setChatStickerSet(self, chat_id, sticker_set_name):
        return self.post('setChatStickerSet', ['chat_id', 'sticker_set_name'], chat_id=chat_id, sticker_set_name=sticker_set_name)

    def deleteChatStickerSet(self, chat_id):
        return self.get('deleteChatStickerSet', ['chat_id'], chat_id=chat_id)

    def answerCallbackQuery(self, callback_query_id, **kwargs):
        return self.post('answerCallbackQuery', ['callback_query_id', 'text', 'show_alert', 'url', 'cache_time'], callback_query_id=callback_query_id, **kwargs)

    def editMessageText(self, text, **kwargs):
        return self.post('editMessageText', ['chat_id', 'message_id', 'inline_message_id', 'text', 'parse_mode', 'disable_web_page_preview', 'reply_markup'],
                         text=text, **kwargs)

    def editMessageCaption(self, **kwargs):
        return self.post('editMessageCaption', ['chat_id', 'message_id', 'inline_message_id', 'caption', 'parse_mode', 'reply_markup'], **kwargs)

    def editMessageReplyMarkup(self, **kwargs):
        return self.post('editMessageReplyMarkup', ['chat_id', 'message_id', 'inline_message_id', 'reply_markup'], **kwargs)

    def deleteMessage(self, chat_id, message_id):
        return self.post('deleteMessage', ['chat_id', 'message_id'], chat_id=chat_id, message_id=message_id)