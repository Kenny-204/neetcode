temperatures = [30, 38, 30, 36, 35, 40, 28]


def dailyTemperatures(temperatures):
    res = []
    for i in range(len(temperatures)):
        count = 1
        found = False
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                # res.append(temperatures[j])
                found = True
                break
            count += 1
        if found == True:
            res.append(count)
        else: res.append(0)
    return res
        
    


print(dailyTemperatures(temperatures))
