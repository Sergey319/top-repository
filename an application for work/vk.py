from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

TOKEN = "vk1.a.g8zNLtdez7ts40ll2IuPCdIyjxsqoKFbhtvfDOmp7V_q4W8sNmAEPZQMisk3rWgP47m1I6Ac2MV7fV_9v-eWlyo8Vek8X0xcXoMO75A3RZ9dqIYg39LjhZGELU4PQQbxJMg_PxgMic7ItOjsSFQFHYDFg7TwJ1NC0p3g5dXr8g2WF8SXPWfIgpsGDEd_nfOMWm83ovSW2TxcadBzCjxsmg"
#PEER_ID = 280301240
PEER_ID = 480583232

def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key

def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )

def main():
    vk_session = VkApi(token=TOKEN)
    vk = vk_session.get_api()
    upload =VkUpload(vk)

    send_photo(vk, PEER_ID, *upload_photo(upload, r"F:\Python415\top-repository\an application for work\Сводка25.04.jpg"))

if __name__ == '__main__':
    main()