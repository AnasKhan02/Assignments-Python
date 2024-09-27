def fibbo(n):
    series = []
    series.append(0)
    series.append(1)
    for i in range(2,n+1):
        series.append(series[i-1] + series[i-2])
    print(series)

print(fibbo(int(input())))