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
