import datetime  as dt
now=dt.datetime.utcnow()
period=dt.timedelta(hours=3)
msk_time=now+period
month=msk_time.strftime("%B")
week=msk_time.strftime("%A")
h=int(msk_time.strftime("%H"))
if month=="January":
    month="Января"
elif month=="February":
    month="февраля"
elif month=="March":
    month="Марта"
elif month=="April":
    month="Апреля"
elif month=="May":
    month="Марта"
elif month=="June":
    month="Июля"
elif month=="July":
    month="Июня"
elif month=="August":
    month="Августа"
elif month=="September":
    month="Сентября"
elif month=="October":
    month="Октября"
elif month=="November":
    month="Ноября"
elif month=="December":
    month="Декабря"
if week=="Monday":
    week="Понедельник"
elif week=="Tuesday":
    week="Вторник"
elif week=="Wednesday":
    week="Среда"
elif week=="Thursday":
    week="Четверг"
elif week=="Friday":
    week="Пятница"
elif week=="Saturday":
    week="Суббота"
elif week=="Sunday":
    week="Воскресенье"
if h<6:
    temp="Доброй ночи"
if h<12:
    temp="Доброе утро"
if h<17:
    temp="Добрый день"
if h<22:
    temp="Добрый вечер"

print(h)
print('Сегодня',week,msk_time.strftime('%d'),month ,msk_time.strftime('%Y'),'года')
print('Время',msk_time.strftime('%H:%M'))
