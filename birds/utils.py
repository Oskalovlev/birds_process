class hashMap:
    d = {}

    def put(key, val):
        hashMap.d[key] = val

    def get(key):
        return hashMap.d.get(key)

    def remove(key):
        if key in hashMap.d:
            hashMap.d.pop(key)

    def containsKey(key):
        return key in hashMap.d

    def export():
        ex_hashMap = []
        for key in hashMap.d.keys():
            ex_hashMap.append({"key": key, "value": hashMap.d[key]})
        return ex_hashMap
