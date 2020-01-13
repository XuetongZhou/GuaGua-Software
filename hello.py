from win10toast import ToastNotifier
from datetime import date
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from sys import exit

t_together = date(2018, 3, 22)
today = date.today()
together_days = (today-t_together).days

hello_meg = "我们已经在一起" + str(together_days) + "天了哦\n"

hour_now = datetime.now().hour

if hour_now < 6 or hour_now >= 18:
    hello_head = "豆豆晚安安安安安安安安~"
    if hour_now < 2:
        hello_meg = hello_meg + "快准备睡觉觉！ 爱你呀！"
    else:
        hello_meg = hello_meg + "晚上也要加油哦~  爱你哦~"
elif hour_now >= 6 and hour_now < 11:
    hello_head = "豆豆早安安安安安！"
    hello_meg = hello_meg + "又是元气满满的一早哦~  爱你~"
elif hour_now >= 11 and hour_now < 1:
    hello_head = "豆豆午安安安安安安！"
    hello_meg = hello_meg + "中午有没有吃饱哦"
else:
    hello_head = "豆豆下午安安安安安！"
    hello_meg = hello_meg + "下午也要元气满满哦~  爱你！！"

hello_toaster = ToastNotifier()
hello_toaster.show_toast(hello_head, hello_meg, "logo.ico", 10);

sleep(300)

try:
    html = get("http://www.weather.com.cn/weather/101210101.shtml").text.encode('iso-8859-1')
except:
    sleep(300)
    try:
        html = get("http://www.weather.com.cn/weather/101210101.shtml").text.encode('iso-8859-1')
    except:
        exit()

soup = BeautifulSoup(html, 'html.parser')
con = soup.find(id='7d')
weather_list = con.find_all('li')

wea_today = weather_list[0].find('p', class_='wea').string
tem_today = weather_list[0].find('p', class_='tem').find('i').string
wind_today = weather_list[0].find('p', class_='win').find('i').string
wea_tomorrow = weather_list[1].find('p', class_='wea').string
tem_tomorrow = weather_list[1].find('p', class_='tem').find('i').string
wind_tomorrow = weather_list[1].find('p', class_='win').find('i').string

weather_head = "瓜瓜天气预报"
weather_meg = "今天：" + wea_today + " " + tem_today + " " + wind_today
if int(tem_today[:-1]) < 5:
    weather_meg = weather_meg + " 注意保暖哦~\n"
else:
    weather_meg = weather_meg + "\n"
weather_meg = weather_meg + "明天：" + wea_tomorrow + " " + tem_tomorrow + " " + wind_tomorrow + "\n"

weather_toaster = ToastNotifier()
weather_toaster.show_toast(weather_head, weather_meg, "logo.ico", 10)

exit()