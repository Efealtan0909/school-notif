import datetime
import pytz
import time
from plyer import notification

#10:00 S
#10:40 E
#10:50 S
#11:30 E
#11:40 S
#12:20 E
#12:30 S
#13:10 E
#13:20 S
#14:00 E

times = [
  ["10:00", "10:40", "09:55", "10:35"],
  ["10:50", "11:30", "10:45", "11:25"],
  ["11:40", "12:20", "11:35", "12:15"],
  ["12:30", "13:10", "12:25", "13:05"],
  ["13:20", "14:00", "13:15", "13:55"]
]

done = []

def notify(t, msg):
  notification.notify(
  title = t,
  message = msg,
  timeout = 60
  )

print('Started')

while True:
  t = datetime.datetime.now(pytz.timezone('Europe/Istanbul'))
  tf = t.strftime('%H:%M')
  tf2 = str(t.year)+'/'+str(t.month)+'/'+str(t.day)+' '+t.strftime('%H:%M')
  for t2 in times:
    ts = t2[0]
    te = t2[1]
    tsb = t2[2]
    teb = t2[3]
    if not tf2 in done:
      if tf == tsb:
        notify('Ders Başlangıç', 'Dersin başlamasına 5 dakika kaldı')
        done.append(tf2)
      elif tf == ts:
        notify('Ders Başlangıç', 'Ders Başladı')
        done.append(tf2)
      elif tf == teb:
        notify('Ders Bitiş', 'Dersin bitmesine 5 dakika kaldı')
        done.append(tf2)
      elif tf == te:
        notify('Ders Bitiş', 'Ders Bitti')
        done.append(tf2)
  time.sleep(15)

