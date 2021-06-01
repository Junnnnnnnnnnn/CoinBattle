from flask import Flask, Blueprint, request
from coinBattle import socket
bp = Blueprint("HomeSocketController", __name__);

users = []
@socket.on("connect")
def connect():
    print("CONNECT !!")
    socket.emit("connect", request.sid, to=request.sid)

@socket.on("disconnect")
def disconnect():
    if len(users):
        for i in range(0, len(users)):
            if users[i].get("id") == request.sid:
                users.pop(i)
    print("\n\n\nUSERS ::: ", users)
    socket.emit("disconnect", request.sid)
@socket.on("setting")
def setting(sid, data, index):
    print("SID ::: ", sid)
    print("color ::: ", data)
    info = {
        "id": sid,
        "color": data,
        "index": index,
    }
    users.append(info)

    print("list ::: ", users)
    socket.emit("setting", info)
    if len(users) == 2:
        socket.emit("ready", 1)


@socket.on("initColor")
def initColor():
    socket.emit("initColor", users)

@socket.on("changeCoin")
def changeCoin(index, color, className):
    print("INDEX ::: ", index)
    print("COLOR ::: ", className)
    socket.emit("changeCoin", {"index": index, "color": color, "className": className})


