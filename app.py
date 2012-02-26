#!/usr/bin/python

import serial
import ConfigParser
from bottle import route, static_file, template, run, debug, request


config = ConfigParser.ConfigParser()
config.read(['config.conf'])

pollSpeed = config.get('gui', 'poll_speed')

try:
    ser = serial.Serial(config.get('serial', 'serial'), config.get('serial', 'baud'))
except serial.SerialException:
    ser = None


@route('/static/<file:re:.*>')
def static(file):
    return static_file(file, root="static")


@route('/')
def index():
    return template('templates/index.tpl', init=(ser is not None), pollSpeed=pollSpeed)


@route('/serial', method='GET')
def get_serial():
    resp = ""
    while ser and ser.inWaiting():
        resp += ser.readline()[0:-2]

    return resp

@route('/serial', method='POST')
def send_serial():
    if not ser:
        return 'false'

    try:
        ser.write(request.POST.get('serial'))
        return "true"
    except serial.SerialException:
        return "false"


if __name__ == "__main__":
    debug()
    run(host=config.get('server', 'host'), port=config.get('server', 'port'))