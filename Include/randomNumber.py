import random

#生成随机参数
def random_parameter( maxNum ):

    #随机生成整数或者分数的标志
    tag = random.randint(0, 1)
    maxNum=int(maxNum)
    num = ''
    # tag == 0 时生成整数
    if tag == 0:
        num = str(random.randint( 0, maxNum ))

    # tag == 1 时生成分数
    elif tag == 1:
        num = random_fraction( maxNum )

    return num

#随机生成分数
def random_fraction( maxNum ):

    #分母
    maxNum=int(maxNum)
    denominator = random.randint( 1, maxNum )

    #分子
    molecule = random.randint( 0, maxNum * denominator )

    if molecule == 0:
        return 0

    if molecule > denominator:
        m = int(molecule / denominator)
        molecule -= m * denominator
        if molecule != 0:
            return str(m) + "'" + str(molecule) + '/' + str(denominator)
        else:
            return str(m)

    return str(molecule) + '/' + str(denominator)
