from cmdb import models
import pprint
from aip import AipNlp


def judgeEmotion(message):
    emotion = ""
    APP_ID = '16811849'
    API_KEY = 'N1hOXPpQlzjyABnwANlq1zeV'
    SECRET_KEY = 'Z76lPMetpBZUqqzWfL1FoNSYELUwFa8X'

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    """ 调用情感倾向分析 """
    text = message
    options = {}
    options["scene"] = "talk"
    reponse = client.emotion(text, options)['items'][0]
    pprint.pprint(reponse)
    '''
    response:
        {'label': 'optimistic',
        'prob': 0.976717,
        'replies': ['以后还会更优秀哦'],
        'subitems': [{'label': 'like', 'prob': 0.976717}]}
    '''
    emotion = reponse['label']
    reply = reponse['replies']
    return emotion,reply

emotion,reply = judgeEmotion("难受")
print(emotion)
print(reply)