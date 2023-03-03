from flask import Flask
from flask import render_template


i = 0
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    user = "Ученик Яндекс.Лицея!"
    return render_template("index.html", title="Домашняя страница", username=user)


def main():
    app.run(port=8000, host="192.168.0.152")


if __name__ == "__main__":
    main()
