# 1: 大吉、2: 吉、3: 中吉、4: 小吉、5: 凶、6:大凶
import random
from flask import Flask, render_template, request

app = Flask(__name__)

GOOD_FILE = 'input/fortune_good.txt'
BAD_FILE = 'input/fortune_bad.txt'


@app.route("/")
def index():
    fortune = {}
    if request.args.get('fortune',''):
        fortune['no']= random.randint(1,6)
        #吉凶によって利用するファイルを変更
        if fortune['no'] >=5:
            #凶と大凶の場合
            fortune_file=BAD_FILE
        else:
            fortune_file = GOOD_FILE
        with open(fortune_file,'r',encoding='utf-8')as f:
            messages =f.readlines()
        msg = random.choice(messages)
        fortune['message'] = msg.strip()

    return render_template('index.html', fortune=fortune)
