minutIn = int(input())
hour = minutIn // 60
minutOut = minutIn - hour * 60
sut = hour // 24
hourOut = hour - sut * 24
print(hourOut, minutOut)
