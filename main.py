from flask import Flask
from flask import render_template


i = 0
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    user = "Ученик Яндекс.Лицея!"
    return render_template("index.html", title="Домашняя страница", username=user)


@app.route("/bootstrap_sample")
def bootstrap():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>"""


def main():
    app.run(port=8000, host="192.168.0.152")


if __name__ == "__main__":
    main()
