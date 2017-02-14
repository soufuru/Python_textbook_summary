# chapter2-1~2-4

########################
####---基本的な演算---####
########################

# 四則演算
print(1 + 2 - 1) # 1
print(2 * 3 / 2) # 3.0

# べき乗
print(2 ** 500)  #3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127560071009217256545885393053328527589376
                    #めちゃくちゃでかい数字でも大丈夫

##################
####---変数---####
##################

# 東京-大阪、何時間かかる？
kyori = 507.5
jisoku = 100
jikan = kyori / jisoku
print(jikan) #5.075

# 数値に説明を加えて出力
nenrei = 18
print("年齢は", nenrei ,"才です。") #年齢は 18 才です。

##########################
####---文字列について---####
##########################

# シングルクォートの中でシングルクォートを表現
print('I can\'t play the guitar.') # バックスラッシュはエスケープシーケンスと呼ばれ奴で、文字列の中で特別な意味を持っている.

# ダブルクォートの中でダブルクォートを表現
print("I like \"Orange\".")

# 文字列の結合
s = "Hello," + "World!"
print(s)


##--- Tips
# print(.... , end="")で改行しない
print("剣で突き刺すかのように", end = "")
print("話す人がいる。", end="")
print("しかし賢い者たちの舌は", end="")
print("人をいやす。")

# 県で突き刺すかのように話す人がいる。しかし賢いものたちの舌は人をいやす。
