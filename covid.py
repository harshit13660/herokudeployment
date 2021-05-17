import requests
from datetime import datetime
from pushbullet import PushBullet
import json

count=0
API= 'o.WfYU9eM5o7fXoBq5PxburlwjXEpfCw0Q'
pb=PushBullet(API)
#SHAHDARA
b=datetime.today()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?'
para={"district_id": 148, "date": b.strftime("%d-%m-%Y")}
a=requests.get(url,params=para,headers=headers)
fi=a.text


try:
    with open("file1.json",'w') as f:
        f.write(fi)

    with open("file1.json",'r') as f:
        file= json.load(f)

    for i in range(0, len(file['centers'])):
        if (file['centers'][i]['sessions'][0]['min_age_limit'] == 45 and (
                file['centers'][i]['sessions'][0]['available_capacity'] >= 1)):
            count = count + 1

    if count >= 1:
        pb.push_note("Vaccine Slots Available", "Slots Available for 18+ Hurry up")
except Exception as e:
    print("No json Data")





