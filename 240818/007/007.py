code, place, time = input().split()


class zerozeroseven:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

answer = zerozeroseven(code, place, time)
print('secret code : ' + answer.code)
print('meeting point : ' + answer.place)
print('time : ' + answer.time)