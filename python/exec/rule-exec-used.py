#!/usr/bin/env python
# License: MIT (c) GitLab Inc.

from flask import Flask, request

app = Flask(__name__)
# Literal strings are ok
com = '''
import os
os.system('ls -l')
'''


@app.route('/exec', methods=['POST'])
def exec_route():
    user_input = request.form['input']

    # ruleid: python_exec_rule-exec-used
    exec(f"{user_input}")

    # ruleid: python_exec_rule-exec-used
    exec("Hello {0}!" % user_input)

    # ruleid: python_exec_rule-exec-used
    exec(user_input)


@app.route('/safe', methods=['GET'])
def exec_safe_route():
    text = 'exec is evil'
    com = f"print('{text}')"

    # rule ok:
    exec(com)

    # rule ok:
    exec(com)

    # rule ok:
    exec("2 + 3")

    # rule ok:
    exec("print('hello world!')")

    return "no response"


if __name__ == '__main__':
    app.run(debug=True)
