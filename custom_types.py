# custom_types.py

class MyInt:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.value + other.value)
        elif isinstance(other, MyFloat):
            return MyFloat(self.value + other.value)
        elif isinstance(other, MyComplex):
            return MyComplex(self.value + other.value)
        else:
            raise TypeError("不支持的加法操作")

    def __lt__(self, other):
        if isinstance(other, (MyInt, MyFloat)):
            return self.value < other.value
        else:
            raise TypeError("不支持的比较操作")

    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value == other.value
        elif isinstance(other, MyFloat):
            return self.value == other.value
        else:
            raise TypeError("不支持的比较操作")

    def __str__(self):
        return str(self.value)

class MyFloat:
    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyFloat(self.value + other.value)
        elif isinstance(other, MyFloat):
            return MyFloat(self.value + other.value)
        elif isinstance(other, MyComplex):
            return MyComplex(self.value + other.value)
        else:
            raise TypeError("不支持的加法操作")

    def __lt__(self, other):
        if isinstance(other, (MyInt, MyFloat)):
            return self.value < other.value
        else:
            raise TypeError("不支持的比较操作")

    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value == other.value
        elif isinstance(other, MyFloat):
            return self.value == other.value
        else:
            raise TypeError("不支持的比较操作")

    def __str__(self):
        return str(self.value)

class MyComplex:
    def __init__(self, value):
        self.value = complex(value)

    def __add__(self, other):
        if isinstance(other, (MyInt, MyFloat, MyComplex)):
            return MyComplex(self.value + other.value)
        else:
            raise TypeError("不支持的加法操作")

    def __str__(self):
        return str(self.value)

class MyList:
    def __init__(self, *args):
        self.data = list(args)

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)

class MyDict:
    def __init__(self, **kwargs):
        self.data = dict(kwargs)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def __str__(self):
        return str(self.data)
