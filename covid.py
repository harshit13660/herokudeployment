from pushbullet import Pushbullet
import time


API= 'o.WfYU9eM5o7fXoBq5PxburlwjXEpfCw0Q'
pb=Pushbullet(API)
while True:

    pb.push_note("Hurry up dude","working succesfully")

    time.sleep(5)