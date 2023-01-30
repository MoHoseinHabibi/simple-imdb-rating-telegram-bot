# simple imdb rating telegram bot
simple bot that return imdb rating of given movie/series name
this bot uses RapidApi api to get imdb rating therefor you need to get api key from rapidapi
feel free to use this bot for you university porject

این یه ربات ساده تلگرامه که اسم فیلم یا سریال میگیره و امتیاز اونو تو imdb برمیگردونه.  
میتونید از این ربات برای پروژه دانشگاتون استفاده کنید.

![bot chat sample](/preview.png)
# how to run
1. install requirements by `pip install -r requirements.txt` command
2. rename config.py.sample to config.py
3. in config.py replace TOKEN with telegram bot token which you should obtained from [botfather](https://t.me/BotFather) bot in telegram 
4. login to https://rapidapi.com and subscribe to Online Movie Database api and get your api key from dashboard and replace it with APIKEY in config.py
5. run bot by `python bot.py` command

# نحوه راه اندازی
1. اول از همه انتظار میره که پایتون رو نصب داشته باشید اگه ندارید میرید تو سایت python.org و پایتون رو دانلود و نصب میکنید
2. وارد پوشه ای که فایل های پروژه هست وارد میشید و با دستور `pip install -r requirements.txt` کتابخونه های مورد نیاز رو نصب میکنید
3. نام فایل config.py.sample رو به config.py تغییر میدید
4. توکنی که از ربات [botfather](https://t.me/BotFather) تو تلگرام گرفتید رو تو فایل config.py جای کلمه TOKEN پیست میکنید
5. تو سایت https://rapidapi.com ثبت نام کنید و به `Online Movie Database` سابیکرایب کنید و بعد از بخش داشبورد api_key رو کپی کنید و تو فایل config.py جای کلمه APIKEY پیست کنید
6. ربات رو با دستور `python bot.py` اجرا کنید