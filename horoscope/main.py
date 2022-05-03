import random, requests, zodiac
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/gethoroscope", methods=["POST"])
def get_horoscope():
    name = request.form["query_name"]
    if not zodiac.check_name(name):
        return 'Name must contains only letters. Please try again!'
    else:
        name = zodiac.check_name(name)

    date = request.form["query_date"]

    api_day_list = ['today', 'yesterday', 'tomorrow']
    api_day_list = random.choice(api_day_list)

    formatted_date = zodiac.format_date(date)
    if not zodiac.check_date(formatted_date):
        return 'You cannot select future dates. Please try again!'

    zodiac_sign = zodiac.zodiac(formatted_date)

    querystring = {"sign": zodiac_sign, "day": api_day_list}

    display_name = name

    response = requests.request("POST", url, headers=headers, params=querystring)

    response_dict = response.json()

    display_description = response_dict['description']
    display_lucky_number = response_dict['lucky_number']

    zodiac_img = zodiac.zodiac_dict[zodiac_sign]

    with open('file.txt', 'a', encoding='UTF-8') as f:
        f.write(f'\n'
                f'User: {display_name}\n'
                f'Your zodiac sign is: {zodiac_sign}\n'
                f'Your lucky number is: {display_lucky_number}\n'
                f'Your magic prophecy: {display_description}\n'
                '-------------------------------------------------'
                )

    return render_template('result.html', display_name=display_name, display_description=display_description, display_lucky_number=display_lucky_number, zodiac_sign=zodiac_sign, zodiac_img=zodiac_img)


url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
headers = {
    'X-RapidAPI-Host': "sameer-kumar-aztro-v1.p.rapidapi.com",
    'X-RapidAPI-Key': "1d29be574fmsh640449ef3f06ab9p142201jsn740815e95d10"
}

if __name__ == '__main__':
    app.run(debug=True)
