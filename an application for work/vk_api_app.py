import vk_api
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token="vk1.a.g8zNLtdez7ts40ll2IuPCdIyjxsqoKFbhtvfDOmp7V_q4W8sNmAEPZQMisk3rWgP47m1I6Ac2MV7fV_9v-eWlyo8Vek8X0xcXoMO75A3RZ9dqIYg39LjhZGELU4PQQbxJMg_PxgMic7ItOjsSFQFHYDFg7TwJ1NC0p3g5dXr8g2WF8SXPWfIgpsGDEd_nfOMWm83ovSW2TxcadBzCjxsmg")
vk = vk_session.get_api()
upload = VkUpload(vk)

#event = VkLongPoll(vk_session).listen()
#for event in VkLongPoll(vk_session).listen():
#    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#        if event.text == "картинка":
photo = upload.photo_messages(photos=r"F:\Python415\top-repository\an application for work\Сводка25.04.jpg")[0]
vk.messages.send(
    user_id=480583232,
    #peer_id=280301240,
    random_id=get_random_id(),
    #message="Ваша картинка:",
    attachment='photo{}_{}'.format(photo['owner_id'], photo['id'])
)