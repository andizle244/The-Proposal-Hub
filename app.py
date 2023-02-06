from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import *
from pywebio.pin import *
import openai


def App():
    put_html("<center><h2>The Proposal Hub</h2></center>").style("color:black;")
    put_html(
        "<center><p>Paste the job description, or job proposal (Optional: Add what tone you would like your proposal to be written in and add any other nuances you would like included</p></center>").style("color:gray;")
    put_html("<center><p><a/></p></center>").style("color:black;")
    openai.api_key = "generate one"
    while True:
        def is_valid(ask):
            if ask == " " or ask == "":
                return 'Enter a valid prompt!'
        ask = input("Paste your proposal here!", type="text", validate=is_valid)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=0.9,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        text = response['choices'][0]['text']
        put_text('The Proposal Hub is complete: ', text).style(
            "background:#212529; color:white; border-radius:5px")

pyth
app = Flask(__name__)

# app.run()


app.add_url_rule('/tool', 'webio_view', webio_view(App),
                 methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    start_server(App, port=8080)