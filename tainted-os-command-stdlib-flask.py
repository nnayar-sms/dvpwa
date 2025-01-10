import os
import subprocess
import sys

import commands
import popen2
from flask import Blueprint
from flask import Flask
from flask import request

app = Flask(__name__)


# create a route directly on the Flask application object
@app.route("/direct")
def direct_response():

    tainted = request.args.get("input")
    rand = os.urandom()

    # ok: tainted-os-command-stdlib-flask
    os.putenv("var", tainted)

    # ruleid: tainted-os-command-stdlib-flask
    os.startfile(r"root/path/" + tainted)

    # ruleid: tainted-os-command-stdlib-flask
    os.startfile(tainted, "print")

    # ruleid: tainted-os-command-stdlib-flask
    os.startfile(tainted, "compile")

    # ok: tainted-os-command-stdlib-flask
    os.startfile("filename", "compile", tainted)  # <- args can be tainted as well

    # ruleid: tainted-os-command-stdlib-flask
    os.system(tainted)

    if rand == 1:
        # ok: tainted-os-command-stdlib-flask
        os.execl(
            sys.executable,
            sys.executable,
            "-m",
            "promptflow._cli._pf.entry",
            *sys.argv[1:]
        )

    if rand == 1:
        # ruleid: tainted-os-command-stdlib-flask
        os.execl(tainted, tainted, "-m", "promptflow._cli._pf.entry", *sys.argv[1:])

    if rand == 1:
        # ok: tainted-os-command-stdlib-flask
        os.execl(
            sys.executable, sys.executable, "-m", "promptflow._cli._pf.entry", tainted
        )

    if rand == 1:
        # ruleid: tainted-os-command-stdlib-flask
        os.execv(tainted, ["arg1", "arg2"])

    if rand == 1:
        # ruleid: tainted-os-command-stdlib-flask
        os.execve(tainted, ["arg1", "arg2"], sys.env)

    # ok: tainted-os-command-stdlib-flask
    os.popen(tainted)

    # ok: tainted-os-command-stdlib-flask
    popen2.popen2(tainted)
    # ok: tainted-os-command-stdlib-flask
    popen2.popen3(tainted)
    # ok: tainted-os-command-stdlib-flask
    popen2.Popen3(tainted)

    # ruleid: tainted-os-command-stdlib-flask
    os.posix_spawn(tainted, ["arg1", "arg2"], sys.env, setsid=False)
    # ok: tainted-os-command-stdlib-flask
    os.posix_spawn("cmd", [tainted, "arg2"], sys.env, setsid=False)
    # ok: tainted-os-command-stdlib-flask
    os.posix_spawn("cmd", ["arg1", "arg2"], tainted, setsid=False)

    # ruleid: tainted-os-command-stdlib-flask
    os.spawnle(os.P_NOWAITO, tainted, *sys.args, sys.env)
    # ok: tainted-os-command-stdlib-flask
    os.spawnle(os.P_NOWAITO, "myfile.py", *sys.args, tainted)
    # ok: tainted-os-command-stdlib-flask
    os.spawnle(os.P_NOWAITO, "myfile.py", [tainted, "arg2"], sys.env)
    # ruleid: tainted-os-command-stdlib-flask
    os.spawnl(os.P_NOWAIT, tainted)
    # ok: tainted-os-command-stdlib-flask
    os.spawnl(os.P_NOWAIT, "setup.exe")

    # ok: tainted-os-command-stdlib-flask
    subprocess.run(tainted, shell=True)
    # ok: tainted-os-command-stdlib-flask
    subprocess.run(["cmd", tainted], shell=False)
    # ruleid: tainted-os-command-stdlib-flask
    subprocess.run([tainted, "arg1"], shell=False)
    # ruleid: tainted-os-command-stdlib-flask
    subprocess.run("mycommand", shell=False, env=tainted)

    # ok: tainted-os-command-stdlib-flask
    subprocess.Popen("mycommand", shell=False, executable=tainted)

    # ok: tainted-os-command-stdlib-flask
    subprocess.Popen(
        "cc" + ["-E", "-P", "-x", "-"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    subprocess.Popen(
        "cc" + ["-E", "-P", "-x", "-"],
        stdin=subprocess.PIPE,
        # ok: tainted-os-command-stdlib-flask
        env=tainted,
        stdout=subprocess.PIPE,
    )

    # ruleid: tainted-os-command-stdlib-flask
    commands.getoutput(tainted)
    # ruleid: tainted-os-command-stdlib-flask
    commands.getstatusoutput(tainted)


# create a route directly on the Flask application object
@app.route("/direct/<param>")
def direct_response2(param):
    tainted = param

    # ok: tainted-os-command-stdlib-flask
    os.popen(tainted)


bp = Blueprint("bp", __name__)


@bp.route("/direct/<param>")
def direct_response3(param):

    tainted = param

    # ok: tainted-os-command-stdlib-flask
    os.popen(tainted)


not_a_flask_app = FlaskLikeAPI(__name__)


@not_a_flask_app.route("/direct/<param?")
def direct_response4(param):

    tainted = param

    # ok: tainted-os-command-stdlib-flask
    os.popen(tainted)
