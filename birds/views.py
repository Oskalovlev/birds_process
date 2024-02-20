import json

from flask import request

from birds import app
from birds.utils import hashMap


@app.route("/set_input_direct/<method>", methods=["POST"])
def set_input(method):
    func = method
    jdata = json.loads(request.data.decode("utf-8"))
    f = globals()[func]
    hashMap.d = jdata["hashmap"]
    f()
    jdata["hashmap"] = hashMap.export()
    jdata["stop"] = False
    jdata["ErrorMessage"] = ""
    jdata["Rows"] = []

    return json.dumps(jdata)


@app.route("/post_screenshot", methods=["POST"])
def post_screenshot():
    d = request.data  # noqa
    return "1"
