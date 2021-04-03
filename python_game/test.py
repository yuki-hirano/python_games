import random
pl_pos = 1
com_pos = 1
def banmen():
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos)+"Goal")
    print("・"*(com_pos-1) + "C" + "・"*(30-pl_pos)+"Goal")

banmen()
print("すごろくスタート")
while True:
    
    input("Enterを押すとあなたのコマが進む")
    pl_pos = pl_pos + random.randint(1,6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("あなたの勝ちです")
        break
    input("Enterを押すとCPUのコマが進む")
    com_pos = com_pos + random.randint(1,6)
    if com_pos > 30:
        com_pos > 30
    banmen()
    if com_pos == 30:
        print("CPUの勝ちです！")
        break
    
