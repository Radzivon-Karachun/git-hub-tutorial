secIn = int(input())
minute = secIn // 60
hour = minute // 60
sut = hour // 24
secOut = secIn - minute * 60
minOut = minute - hour * 60
hourOut = hour - sut * 24
print('%01d:%02d:%02d' % (hourOut, minOut, secOut))
