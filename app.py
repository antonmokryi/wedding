from flask import Flask, render_template, url_for, request, redirect, make_response
from flask_scss import Scss
import sqlite3
# from telegram import Bot
import time
import requests




app = Flask(__name__)
scss = Scss(app, static_dir='static/css', asset_dir='css')
# bot = Bot('7035391219:AAH_S8I9XDvPpulXuwlVaxCSninkkFOFcjY')


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/search_num', methods=['POST'])
def search_num():
    inp_num = request.form['number'].strip()  # Видаляємо зайві пробіли з введеного рядка
    if not inp_num or not inp_num.isdigit():  # Перевіряємо, чи введено не пустий рядок та чи складається він лише з цифр
        print("Введено неправильні дані")
        return render_template('index.html')  # Повертаємо користувача на сторінку index.html

    inp_num = int(inp_num)
    inp_num = int(request.form['number'])

    con = sqlite3.connect(
        "guests.db"
    )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM guests")
    for num in cursor.fetchall():
        if inp_num == num[1]:
            response = make_response(redirect(url_for('invitation')))
            response.set_cookie('user_id', str(inp_num))
            print(response)
            return response
 
    print(f"Немає номера в  базі {inp_num}")
    return render_template('index.html')

@app.route('/invitation')
def invitation():
    user_num = int(request.cookies.get('user_id'))
    print(user_num)
    con = sqlite3.connect(
        "guests.db"
    )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM guests")
    for num in cursor.fetchall():
        if user_num == num[1]:
            names = num[2]
            compliment = num[3]
            return render_template('invitation.html', names=names, compliment=compliment)



@app.route('/send_bot', methods=['POST'])
def send_bot():
    user_num = int(request.cookies.get('user_id'))
    print(user_num)
    con = sqlite3.connect(
        "guests.db"
    )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM guests")
    for num in cursor.fetchall():
        if user_num == num[1]:
            bot_token = '7035391219:AAH_S8I9XDvPpulXuwlVaxCSninkkFOFcjY'
            message = request.form['message']
            chat_id = 440380344
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            params = {'chat_id': chat_id, 'text': f"телефон: {num[1]}, від кого:{num[2]} повідомлення:{message}"}
            response = requests.post(url, data=params)
            if response.status_code == 200:
                print('Повідомлення відправлене успішно!')
            else:
                print(f'Сталася помилка при відправленні повідомлення: {response.status_code}')
                print(response.text)

            return  redirect(url_for('finish'))
    




@app.route('/finish')
def finish():
    resp = make_response(render_template('finish.html'))

    resp.set_cookie('user_id', '', expires=0)

    return resp

if __name__ == "__main__":
    app.run()

