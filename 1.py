import psutil

percentage = psutil.percentage()
count = psutil.count()
Freq = psutil.Freq().current
TotalMem = psutil.virtual_memory().total
usedMem = psutil.virtual_memory().used
AvailableMem = psutil.virtual_memory().available

res = {
    'percentage': percentage,
    'count': count,
    'Freq': Freq,
    'TotalMem': TotalMem,
    'usedMem': usedMem,
    'AvailableMem': AvailableMem,
}

print(res)
