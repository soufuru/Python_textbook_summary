# chapter3-1

########################
###---リストについて---###
########################

#あるクラスの平均点を求めるプログラム
points = [88, 76, 52, 90, 62]

sum_v = 0
for i in points:
    sum_v += i #

print("平均点は", sum_v / len(points) )

#リストの値を一気に合計するsum()関数
sum_v = sum(points)
print("合計点は", sum_v)

#リストに入るのは数値だけではない
fruits = ["Apple","Banana","Mango","Orange"]
for i in fruits:
    print("I like", i ,"!")
    # print("「" + i + "」が好き")

# for文でインデックス番号付きの繰り返し enumerate()関数
for i,v in enumerate(fruits):
    print(i,v)
    # 0 Apple
    # 1 Banana
    # 2 Mango
    # 3 Orange


######################
###---リストの操作---###
######################

# 要素の追加
num = [1,2,3]
num.append(4)

# リストの結合
n1 = [1,2]
n2 = [3,4]
n3 = n1 + n2 # n3 = [1,2,3,4]
n1 += n2 # n1 = [1,2,3,4]
n = [11,22]
n.extend([33,44]) # n = [11, 22, 33, 44]

# スライス
a = [10, 555, 30, 45]
print(a[1:3]) #[555,30]
##### 終了の位置はインデックス番号の+1を指定する必要がある

print(a[:3]) #[10, 555, 30]
print(a[-1]) #45 後ろから
print(a[0:3:2]) #[10,30] 0から2番目まで2個おき

# 要素の削除
del a[0]
print(a) #[555, 30, 45]


#################
###---タプル---###
#################

t = (1,2,3)
#要素を変更できない配列
