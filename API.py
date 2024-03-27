from telethon.sync import TelegramClient,connection
from jdatetime import GregorianToJalali
from datetime import timezone
import logging
# from s import down
from table import session,P_name,posts
from random import randrange

names = session.query(P_name).all()
person = names[randrange(len(names))]

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def get_IRN_time(time):
    date = GregorianToJalali(time.year,time.month,time.day).getJalaliList()
    time = utc_to_local(time).time()
    return str(date[0])+":"+str(date[1])+":"+str(date[2]),time.__str__()

def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

api_id  = 8888659
api_hash = "75fb85de4a0b0a4e00aeb72d8458de11"
name = []

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

async def get_chat():
    names = await client.get_dialogs()
    for name in names:
        print(str(name.id) + "  "+name.name)

async def talk(whom):
    massage = "خلاصه بگم اینه که کونمون گذاشتن "
    await client.send_message(whom,massage)

async def get_msg(whom):
    massages = await client.get_messages(whom,limit=10)
    for x in massages:
        if x.media:
            await client.download_media(x,progress_callback=callback)
        else:
            print(x.message)


with TelegramClient('anon', api_id, api_hash,connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,proxy=("5.161.75.112",443,"ee002000003000000000000000000000406d61696c2e676f6f676c652e636f6d"))as client:
    client.loop.run_until_complete(get_chat())



# 2072980235سخته فهمیدنش فارسی تایپ کن وویسآره م
# نظر تو چیه؟
# میرزایی با سروش بحث اندازه لباس شد من میگم ضایع میشیم ما اندازشو نداریم سروش میگه بدره بزرگ تر شه اشکالی ندارد کوچک نشه فقط
# میگه یه سایت پیدا کرده دویست تومان با هزینه ارسال تقریبی دویست و چهل
