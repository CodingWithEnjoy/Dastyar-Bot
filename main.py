import requests
import time

TOKEN = '1617359307:PiNPnSiQ4g1h4CaQFPmyau5pI4glnNxYu3bneXet'
BASE_URL = f'https://tapi.bale.ai/bot{TOKEN}/'

WEATHER_API_KEY = '3045dd712ffe6e702e3245525ac7fa38'
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/weather?q=Tehran,IR&units=metric&appid={WEATHER_API_KEY}'

BAD_WORDS = [
        "شت",
        "چس",
        "گوز",
        "ان",
        "لجن",
        "کثافت",
        "بی شرف",
        "بیشعور",
        "گوه",
        "کون",
        "کیری",
        "کسکش",
        "بی ناموس",
        "سگ پدر",
        "پدرسگ",
        "شاش",
        "ریدن",
        "ریدی",
        "کونی",
        "دیوس",
        "انی",
        "گهی",
        "بی پدر",
        "مادرسگ",
        "بی ناموس",
        "جنده",
        "گایدی",
        "گایدن",
        "کیر",
        "کیروکس",
        "عمتو",
        "خفه شو",
        "خفه",
        "خفه خون",
        "مرض داری",
        "مرضداری",
        "گردن دراز",
        "خری",
        "گاوی",
        "اسبی",
        "سگی",
        "حیوانی",
        "دهنتوببند",
        "انگل",
        "آشغال",
        "خرفت",
        "پپه",
        "خنگ",
        "دکل",
        "دله",
        "قرتی",
        "گوزو",
        "کونده",
        "کون ده",
        "گاگول",
        "ابله",
        "گنده گوز",
        "کس",
        "کله کیری",
        "گشاد",
        "دخترقرتی",
        "خواهرجنده",
        "خواهر جنده",
        "مادرجنده",
        "مادر جنده",
        "لخت",
        "بخورش",
        "بپرسرش",
        "بپرروش",
        "بیابخورش",
        "میخوریش",
        "بمال",
        "دیوس خان",
        "زرنزن",
        "زنشو",
        "زنتو",
        "زن جنده",
        "بکنمت",
        "بکن",
        "بکن توش",
        "بکنش",
        "لز",
        "سکس",
        "سکسی",
        "ساک",
        "ساک بزن",
        "پورن",
        "سکسیی",
        "کونن",
        "کیرر",
        "جاکش",
        "انی",
        "بدبخت",
        "خایه",
        "خایه مال",
        "خایه خور",
        "ممه",
        "ممه خور",
        "دخترجنده",
        "خارکسده",
        "کس ننت",
        "کیردوس",
        "مادرکونی",
        "خارکسده",
        "خارکس ده",
        "کیروکس",
        "کس و کیر",
        "زنا",
        "زنازاده",
        "ولدزنا",
        "ملنگ",
        "سادیسمی",
        "فاحشه",
        "خانم جنده",
        "فاحشه خانم",
        "سیکتیر",
        "سسکی",
        "کس خیس",
        "حشری",
        "گاییدن",
        "بکارت",
        "داف",
        "بچه کونی",
        "کسشعر",
        "سرکیر",
        "سوراخ کون",
        "حشری شدن",
        "کس کردن",
        "کس دادن",
        "بکن بکن",
        "شق کردن",
        "کس لیسیدن",
        "آب کیر",
        "جاکش",
        "جلق زدن",
        "جنده خانه",
        "شهوتی",
        "عن",
        "قس",
        "کردن",
        "کردنی",
        "کس لیس",
        "کس کش",
        "کوس",
        "کیرمکیدن",
        "لاکونی",
        "پستان",
        "آلت",
        "آلت تناسلی",
        "نرکده",
        "مالوندن",
        "سولاخ",
        "جنسی",
        "دوجنسه",
        "سگ تو روحت",
        "بی غیرت",
        "نعشه",
        "بی عفت",
        "مادرقهوه",
        "پلشت",
        "پریود",
        "کله کیری",
        "کیرناز",
        "پشمام",
        "لختی",
        "کسکیر",
        "دوست دختر",
        "دوست پسر",
        "کونشو",
        "دول",
        "شنگول",
        "کیردراز",
        "داف ناز",
        "سکسیم",
        "کوص",
        "ساکونی",
        "کون گنده",
        "سکسی باش",
        "کسخل",
        "صیغه ای",
        "گوش دراز",
        "درازگوش",
        "توله سگ",
        "خز",
        "ماچ",
        "ماچ کردنی",
        "اسکل",
        "هیز",
        "بیناموس",
        "اوسکل",
        "بی آبرو",
        "لاشی",
        "لاش گوشت",
        "باسن",
        "جکس",
        "سگ صفت",
        "کصکش",
        "مشروب",
        "عرق خور",
        "سکس چت",
        "جوون",
        "سرخور",
        "کلفت",
        "حشر",
        "لاس",
        "زارت",
        "رشتیf",
        "ترک",
        "فارس",
        "لر",
        "عرب",
        "خر",
        "گاو",
        "اسب",
        "گوسفند",
        "کرم",
        "الاق",
        "الاغ",
        "احمق",
        "بی شعور",
        "حرومزاده",
        "کونی",
        "گه",
        "مادر جنده",
        "کث",
        "کص",
        "پسون",
        "خارکسّه",
        "دهن گاییده",
        "دهن سرویس",
        "دهن سرویسا",
        "پدر سگ",
        "پدر سوخته",
        "پدر صلواتی",
        "لامصب",
        "زنیکه",
        "مرتیکه",
        "مردیکه",
        "بی خایه",
        "عوضی",
        "اسگل",
        "اوسکل",
        "اوسگل",
        "اوصگل",
        "اوصکل",
        "دیوث",
        "دیوص",
        "قرمصاق",
        "قرمساق",
        "غرمساق",
        "غرمصاق",
        "فیلم سوپر",
        "چاقال",
        "چاغال",
        "چس خور",
        "کس خور",
        "کس خل",
        "کوس خور",
        "کوس خل",
        "کص لیس",
        "کث لیس",
        "کس لیس",
        "کوص لیس",
        "کوث لیس",
        "کوس لیس"
]

WEATHER_DESCRIPTIONS = {
    "clear sky": "آسمان صاف",
    "few clouds": "کمی ابری",
    "scattered clouds": "ابرهای پراکنده",
    "broken clouds": "ابرهای شکسته",
    "shower rain": "باران رگباری",
    "rain": "باران",
    "thunderstorm": "رعد و برق",
    "snow": "برف",
    "mist": "مه"
}

def get_updates(offset=None):
    url = BASE_URL + 'getUpdates'
    params = {'offset': offset, 'timeout': 100} if offset else {'timeout': 100}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text, reply_to_message_id=None):
    url = BASE_URL + 'sendMessage'
    payload = {'chat_id': chat_id, 'text': text, 'reply_to_message_id': reply_to_message_id}
    requests.post(url, json=payload)

def check_message_for_bad_words(message):
    text = message.get('text', '').lower()
    if any(bad_word in text for bad_word in BAD_WORDS):
        return True
    return False

def translate_weather_description(description):
    return WEATHER_DESCRIPTIONS.get(description, description)

def get_weather():
    response = requests.get(WEATHER_URL)
    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        translated_description = translate_weather_description(weather_description)
        weather_message = f"دمای تهران: *{temp}°C*\nوضعیت هوا: *{translated_description}*"
    else:
        weather_message = "مشکلی در دریافت وضعیت آب و هوا به وجود آمد."
    return weather_message

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates.get('result', []):
            message = update.get('message')
            if message:
                chat_id = message['chat']['id']
                user_name = message['from']['first_name']
                message_id = message['message_id']
                text = message.get('text', '').lower()
                if check_message_for_bad_words(message):
                    warning_message = f"{user_name} فحش نده کصکش 🗿"
                    send_message(chat_id, warning_message, reply_to_message_id=message_id)
                elif text == "هواشناسی":
                    weather_message = get_weather()
                    send_message(chat_id, weather_message, reply_to_message_id=message_id)
                elif "😂" in text:
                    emoji_response = "خوب میخندی 🗿"
                    send_message(chat_id, emoji_response, reply_to_message_id=message_id)
            offset = update['update_id'] + 1
        time.sleep(1)

if __name__ == '__main__':
    main()