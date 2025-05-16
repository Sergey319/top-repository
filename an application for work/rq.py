#import vk_api
#from vk_api.upload import VkUpload
#from vk_api.utils import get_random_id
#
#session = vk_api.VkApi(token="vk1.a.g8zNLtdez7ts40ll2IuPCdIyjxsqoKFbhtvfDOmp7V_q4W8sNmAEPZQMisk3rWgP47m1I6Ac2MV7fV_9v-eWlyo8Vek8X0xcXoMO75A3RZ9dqIYg39LjhZGELU4PQQbxJMg_PxgMic7ItOjsSFQFHYDFg7TwJ1NC0p3g5dXr8g2WF8SXPWfIgpsGDEd_nfOMWm83ovSW2TxcadBzCjxsmg")
#vk = session.get_api()
#upload = VkUpload(vk)
#
#photo = upload.photo_messages(photos=r"F:\Python415\top-repository\an application for work\Сводка25.04.jpg")[0]
#id = photo['id']
#
#vk.wall.post(
#        owner_id=-219852965,  # id пользователя / сообщества
#        message="hello world",
#        random_id=get_random_id(),
#        photo=photo['id']
#    )
import vk_api
import json
import requests
session = vk_api.VkApi(token='vk1.a.g8zNLtdez7ts40ll2IuPCdIyjxsqoKFbhtvfDOmp7V_q4W8sNmAEPZQMisk3rWgP47m1I6Ac2MV7fV_9v-eWlyo8Vek8X0xcXoMO75A3RZ9dqIYg39LjhZGELU4PQQbxJMg_PxgMic7ItOjsSFQFHYDFg7TwJ1NC0p3g5dXr8g2WF8SXPWfIgpsGDEd_nfOMWm83ovSW2TxcadBzCjxsmg')
api = session.get_api()
result = api.photos.getWallUploadServer(group_id=219852965)
img = {'photo': ('Сводка25.04.jpg', open(r"F:\Python415\top-repository\an application for work\Сводка25.04.jpg", 'rb'))}# ПУТЬ ДО ФОТОГРАФИИ НА ДИСКЕ
response = requests.post(result['upload_url'], files=img)
resultjs = json.loads(response.text)
result2=api.photos.saveWallPhoto(group_id=219852965,photo=resultjs['photo'],hash=resultjs['hash'], server=resultjs['server'])
api.wall.post(owner_id=-219852965,from_group=1,attachments=result2[0]['id'])