def judge(x):
    if x%2 == 0:
        return "even"
    return "odd"

def judge2(x):
    return [["even" for i in range((x%2+1)%2)], ["odd" for i in range(x%2)]][x%2][0]

def judge4(x):
    return ["even", "odd"][x%2]

print(judge(5131056))
print(judge2(5131056))
print(judge4(5131056))
