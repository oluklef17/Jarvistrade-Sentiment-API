from getdata import getdata
from flask import Flask, render_template, request, flash
import os
from write_data import write

app = Flask(__name__)



data = ""


@app.route('/<int:Date>', methods=['POST', 'GET'])
def home(Date):
    write()
    if(os.path.exists(f'Sentiment_{Date}.csv')):
        with open(f'Sentiment_{Date}.csv', 'r') as f:
            data = f.read()
            return data.replace("'","")
    else:
        return 'No data found for the date specified. Please try some other date'



if __name__ == "__main__":
 app.secret_key = "170194"
 app.run(debug=False, host='0.0.0.0')