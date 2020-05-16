import requests
import vk_api
import json

vk_session = vk_api.VkApi(token='193a60b8dcf34283ced57558a3f9ef4407112b85f6a47c8f8dcfed98fa8a4e7c1725349874d9d6c44473a')

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
		
        if event.text:
        	try:
	        	response = json.loads(requests.get('https://videocdn.tv/api/short?api_token=vqKsPAxSoFk9uQZnB31AmuGyOfnIdSQn&title=' + event.text).content)['data']
	        	res = ''
	        	for item in response:
	        		mes = item['title']

	        		if item['year']:
	        			mes += ' (' + item['year'][:4] + ')\n'

	        		else:
	        			mes += '\n'

	        		mes += 'https:' + item['iframe_src']

	        		res += mes + '\n\n'

	        	vk.messages.send(user_id = event.user_id, message = res, random_id = vk_api.utils.get_random_id())
	        except:
	        	pass