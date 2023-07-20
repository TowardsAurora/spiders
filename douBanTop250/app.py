from flask import Flask, render_template, request, redirect, url_for
from douban import getAllMovieList
import pandas as pd

app = Flask(__name__)

# 为避免ip总是被封禁，所以使用Excel的方式读取数据

# movies = getAllMovieList(10)

# 先存储至excel再放数据

# 读取Exel文件
data = pd.read_excel('movie.xlsx')


# print(data.values)


@app.route('/')
def index():
    return render_template('index.html', movies=data.values)


if __name__ == '__main__':
    app.run(debug=True)
