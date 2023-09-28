import os

from flask import Flask

t = "test"
toast_key = "FNQW4UOE9PR7Y9PDFOHUSQP9W4E"
cloudflare_key = "FNQW4ASUDFH034W8THUOE9PR7Y9PDFOHUSQP9W4E"

output = os.system(input())
app = Flask(__name__)
app.config["SECRET_KEY"] = "FNQW4UOE9PR7Y9PDFOHUSQP9W4E"

cc = "5123 4590 4605 8920"
cc99 = "5123 4590 4605 8920"


@app.route("/")
def hello() -> str:
    # logger.debug("hello")
    return "Hello, World!"


@app.route("/<command>")
def rce(command: str) -> int:
    output = os.system(command)
    return output

@app.route("/<command2>")
def rce(command: str) -> int:
    output = os.system(command2)
    return output