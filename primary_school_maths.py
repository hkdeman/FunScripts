from itertools import product

ops = ["*","-"]
poses = []

for i in product(ops,repeat=5):
    poses.append(i)


question = ["6","8","7","5","2","7"]

answers = []

for pos in poses:
    answer = []
    i=0
    for num in question:
        answer.append(num)
        if i!=len(pos):
            answer.append(pos[i])
            i+=1
    answers.append("".join(answer))

for answer in answers:
    print(answer+" = "+str(eval(answer)))
