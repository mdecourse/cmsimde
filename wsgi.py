#!/usr/bin/python

"""Flask startup script
"""

# import flaskapp at the same directory
import flaskapp
import ssl

# even on localhost still use https to access
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('localhost.crt', 'localhost.key')

# get uwsgi variable value of flaskapp.py
uwsgi = flaskapp.uwsgi
ip = flaskapp.ip
port = flaskapp.port

if uwsgi:
    # run on remote site
    application = flaskapp.app
else:
    # on localhost, on Linux or Mac need to use python3 wsgi.py to execute
    flaskapp.app.run(host=ip, port=port, debug=True, ssl_context=context)
