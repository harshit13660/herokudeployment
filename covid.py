import requests
from datetime import datetime
from pushbullet import PushBullet

count=0
API= 'o.WfYU9eM5o7fXoBq5PxburlwjXEpfCw0Q'
pb=PushBullet(API)
#SHAHDARA
b=datetime.today()
headers = {"User-Agent":"BF-DirectLine/3.0 (Microsoft-BotFramework/3.0 +https://botframework.com/ua)"}
url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?'
para={"district_id": 148, "date": b.strftime("%d-%m-%Y")}
a=requests.get(url,params=para,headers=headers)
file=a.json()



for i in range(0,len(file['centers'])):
    if(file['centers'][i]['sessions'][0]['min_age_limit']==45 and (file['centers'][i]['sessions'][0]['available_capacity']>=1)):
        count=count+1

if count>=1:
    pb.push_note("Vaccine Slots Available", "Slots Available for 18+ Hurry up")

