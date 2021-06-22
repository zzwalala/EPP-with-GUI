# 估价函数1：深度+错放棋子个数
# 估价函数2：深度+错放棋子与目标位置的距离之和
import numpy as np
import copy
import time


def standardEight():
    '''标准的八数码'''
    data = [[3, 0, 6], [1, 8, 5], [4, 7, 2]]
    return data


def creatEight():
    ''''构建并返回八数码'''
    data = [[], [], [], 0, 0]  # 存八数码,第一个0表示深度，第二个0表示当前状态（0：初始状态；1：0上移得来；2：0下移得来；3：0左移得来；4：0右移得来）
    i = 0
    while (i < 9):
        j = eval(input('输入第' + str(i + 1) + '个数据：'))
        if 0 <= j <= 8:
            data[int(i / 3)].append(j)
            i = i + 1
        else:
            print('输入数据错误!\n')
    return data


def findLocation(data, findNum):
    data_array = np.array(data[:3])
    return np.argwhere(data_array == findNum)[0]


def errorNum(data_1, data_2):
    errorNum = 0
    loc_1 = findLocation(data_1, 0)
    loc_2 = findLocation(data_2, 0)
    for i in range(3):
        for j in range(3):
            if data_1[i][j] != data_2[i][j]:
                errorNum = errorNum + 1
    if loc_1[0] == loc_2[0 and loc_1[1] == loc_2[1]]:
        return errorNum
    else:
        return errorNum - 1


def getReverseOrderNumber(list):
    '''获得逆序数'''
    num = 0
    for i in range(1, len(list)):
        for j in range(i):
            if list[j] > list[i]:
                num = num + 1
    return num


def judge(data_1, data_2):
    '''判断两个八数码是否可互相到达（逆序奇偶性）'''
    temp1 = copy.deepcopy(data_1[0:3])
    temp2 = copy.deepcopy(data_2[0:3])

    list1 = sum(temp1, [])
    list2 = sum(temp2, [])
    list1.remove(0)
    list2.remove(0)
    if getReverseOrderNumber(list1) % 2 == getReverseOrderNumber(list2) % 2:
        return True
    else:
        print("无解！")
        return False


'''构建估价函数'''


def aStarOne(data_1, data_2):
    '''八数码错放棋子个数的估价函数'''
    '''data_1:标准八数码;data_2:构造的八数码'''
    return errorNum(data_1, data_2) + data_2[3]


def first_method(data_1, data_2):
    return errorNum(data_1, data_2)


def second_method(data_1, data_2):
    errorDistance = 0
    for i in range(1, 9):
        loc_1 = findLocation(data_1, i)
        loc_2 = findLocation(data_2, i)
        errorDistance = abs(loc_1[0] + loc_1[1] - loc_2[0] - loc_2[1]) + errorDistance  # 求曼哈顿距离
    return errorDistance


def third_method(data_1, data_2):
    data = []
    error = 0
    for i in range(3):
        for j in range(3):
            data.append(data_1[i][j])
    for i in range(7):
        if data[i] > data[i + 1]:
            error += 1
    return error


def fourth_method(data_1, data_2):
    data = []
    error = 0
    for i in range(3):
        for j in range(3):
            data.append(data_1[i][j])
    for i in range(7):
        if data[i] > data[i + 1]:
            error += 1
    return error * 3 + errorNum(data_1, data_2)


def fifth_method(data_1, data_2):
    errorNum(data_1, data_2) + data_2[3]


def aStarTwo(data_1, data_2):
    '''错放棋子与目标位置距离之和构成的估价函数'''
    errorDistance = 0
    for i in range(1, 9):
        loc_1 = findLocation(data_1, i)
        loc_2 = findLocation(data_2, i)
        errorDistance = abs(loc_1[0] + loc_1[1] - loc_2[0] - loc_2[1]) + errorDistance  # 求曼哈顿距离
    return errorDistance + data_2[3]


'''构建移动函数'''


def up(data):
    '''上移'''
    zeroLoc = findLocation(data, 0)
    i = int(zeroLoc[0])
    j = int(zeroLoc[1])
    if i > 0:
        temp = data[i][j]
        data[i][j] = data[i - 1][j]
        data[i - 1][j] = temp
        data[3] = data[3] + 1
        data[4] = 1
        return data

    else:
        return


def down(data):
    '''下移'''
    zeroLoc = findLocation(data, 0)
    i = int(zeroLoc[0])
    j = int(zeroLoc[1])
    if i < 2:
        temp = data[i][j]
        data[i][j] = data[i + 1][j]
        data[i + 1][j] = temp
        data[3] = data[3] + 1
        data[4] = 2
        return data
    else:
        return


def left(data):
    '''左移'''
    zeroLoc = findLocation(data, 0)
    i = int(zeroLoc[0])
    j = int(zeroLoc[1])
    if j > 0:
        temp = data[i][j]
        data[i][j] = data[i][j - 1]
        data[i][j - 1] = temp
        data[3] = data[3] + 1
        data[4] = 3
        return data
    else:
        return


def right(data):
    '''右移'''
    zeroLoc = findLocation(data, 0)
    i = int(zeroLoc[0])
    j = int(zeroLoc[1])
    if j < 2:
        temp = data[i][j]
        data[i][j] = data[i][j + 1]
        data[i][j + 1] = temp
        data[3] = data[3] + 1
        data[4] = 4
        return data
    else:
        return


def overCondition(data, openTable):
    '''判断目标八数码是否在openTable中，
    返回 True or False
    并返回目标八数码在openTable的索引
    '''
    index = -1
    for item in openTable:
        index = index + 1
        j = 0
        for i in range(3):
            if item[i] == data[i]:
                j = j + 1
        if j == 3:
            print("搜索成功！")
            return True, index
    return False, -1


def extend(data_1, data_2, openTable, valueTable, closeTable, mode, index2):
    '''扩展八数码,并将被扩展的八数码移除出openTable'''
    '''data_1:被扩展的八数码；data_2:标准八数码'''
    if data_1[4] == 0:
        data1 = up(copy.deepcopy(data_1))
        if data1:
            openTable.append(data1)
            if mode == "1":
                valueTable.append(first_method(data_2, data1))
            elif mode == '2':
                valueTable.append(second_method(data_2, data1))
            elif mode == '3':
                valueTable.append(third_method(data_2, data1))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data1))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data1))

        data2 = down(copy.deepcopy(data_1))
        if data2:
            openTable.append(data2)
            if mode == "1":
                valueTable.append(first_method(data_2, data2))
            elif mode == '2':
                valueTable.append(second_method(data_2, data2))
            elif mode == '3':
                valueTable.append(third_method(data_2, data2))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data2))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data2))

        data3 = left(copy.deepcopy(data_1))
        if data3:
            openTable.append(data3)
            if mode == "1":
                valueTable.append(first_method(data_2, data3))
            elif mode == '2':
                valueTable.append(second_method(data_2, data3))
            elif mode == '3':
                valueTable.append(third_method(data_2, data3))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data3))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data3))

        data4 = right(copy.deepcopy(data_1))
        if data4:
            openTable.append(data4)
            if mode == "1":
                valueTable.append(first_method(data_2, data4))
            elif mode == '2':
                valueTable.append(second_method(data_2, data4))
            elif mode == '3':
                valueTable.append(third_method(data_2, data4))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data4))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data4))

        del valueTable[index2]
        openTable.remove(data_1)
        closeTable.append(data_1)

    elif data_1[4] == 1:
        data1 = up(copy.deepcopy(data_1))
        if data1:
            openTable.append(data1)
            if mode == "1":
                valueTable.append(first_method(data_2, data1))
            elif mode == '2':
                valueTable.append(second_method(data_2, data1))
            elif mode == '3':
                valueTable.append(third_method(data_2, data1))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data1))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data1))

        data3 = left(copy.deepcopy(data_1))
        if data3:
            openTable.append(data3)
            if mode == "1":
                valueTable.append(first_method(data_2, data3))
            elif mode == '2':
                valueTable.append(second_method(data_2, data3))
            elif mode == '3':
                valueTable.append(third_method(data_2, data3))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data3))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data3))

        data4 = right(copy.deepcopy(data_1))
        if data4:
            openTable.append(data4)
            if mode == "1":
                valueTable.append(first_method(data_2, data4))
            elif mode == '2':
                valueTable.append(second_method(data_2, data4))
            elif mode == '3':
                valueTable.append(third_method(data_2, data4))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data4))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data4))

        del valueTable[index2]
        openTable.remove(data_1)
        closeTable.append(data_1)

    elif data_1[4] == 2:
        data2 = down(copy.deepcopy(data_1))
        if data2:
            openTable.append(data2)
            if mode == "1":
                valueTable.append(first_method(data_2, data2))
            elif mode == '2':
                valueTable.append(second_method(data_2, data2))
            elif mode == '3':
                valueTable.append(third_method(data_2, data2))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data2))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data2))

        data3 = left(copy.deepcopy(data_1))
        if data3:
            openTable.append(data3)
            if mode == "1":
                valueTable.append(first_method(data_2, data3))
            elif mode == '2':
                valueTable.append(second_method(data_2, data3))
            elif mode == '3':
                valueTable.append(third_method(data_2, data3))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data3))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data3))

        data4 = right(copy.deepcopy(data_1))
        if data4:
            openTable.append(data4)
            if mode == "1":
                valueTable.append(first_method(data_2, data4))
            elif mode == '2':
                valueTable.append(second_method(data_2, data4))
            elif mode == '3':
                valueTable.append(third_method(data_2, data4))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data4))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data4))

        del valueTable[index2]
        openTable.remove(data_1)
        closeTable.append(data_1)

    elif data_1[4] == 3:
        data1 = up(copy.deepcopy(data_1))
        if data1:
            openTable.append(data1)
            if mode == "1":
                valueTable.append(first_method(data_2, data1))
            elif mode == '2':
                valueTable.append(second_method(data_2, data1))
            elif mode == '3':
                valueTable.append(third_method(data_2, data1))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data1))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data1))

        data2 = down(copy.deepcopy(data_1))
        if data2:
            openTable.append(data2)
            if mode == "1":
                valueTable.append(first_method(data_2, data2))
            elif mode == '2':
                valueTable.append(second_method(data_2, data2))
            elif mode == '3':
                valueTable.append(third_method(data_2, data2))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data2))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data2))

        data3 = left(copy.deepcopy(data_1))
        if data3:
            openTable.append(data3)
            if mode == "1":
                valueTable.append(first_method(data_2, data3))
            elif mode == '2':
                valueTable.append(second_method(data_2, data3))
            elif mode == '3':
                valueTable.append(third_method(data_2, data3))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data3))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data3))

        del valueTable[index2]
        openTable.remove(data_1)
        closeTable.append(data_1)

    elif data_1[4] == 4:
        data1 = up(copy.deepcopy(data_1))
        if data1:
            openTable.append(data1)
            if mode == "1":
                valueTable.append(first_method(data_2, data1))
            elif mode == '2':
                valueTable.append(second_method(data_2, data1))
            elif mode == '3':
                valueTable.append(third_method(data_2, data1))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data1))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data1))

        data2 = down(copy.deepcopy(data_1))
        if data2:
            openTable.append(data2)
            if mode == "1":
                valueTable.append(first_method(data_2, data2))
            elif mode == '2':
                valueTable.append(second_method(data_2, data2))
            elif mode == '3':
                valueTable.append(third_method(data_2, data2))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data2))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data2))

        data4 = right(copy.deepcopy(data_1))
        if data4:
            openTable.append(data4)
            if mode == "1":
                valueTable.append(first_method(data_2, data4))
            elif mode == '2':
                valueTable.append(second_method(data_2, data4))
            elif mode == '3':
                valueTable.append(third_method(data_2, data4))
            elif mode == '4':
                valueTable.append(fourth_method(data_2, data4))
            elif mode == '5':
                valueTable.append(fifth_method(data_2, data4))

        del valueTable[index2]
        openTable.remove(data_1)
        closeTable.append(data_1)
