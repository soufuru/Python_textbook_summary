# chapter2-4 ~

#############################
####---ユーザーからの入力---####
#############################

# 時給計算プログラム

# 時給の入力
usr = input("時給はいくらですか")
jikyu = int(usr)

# 時間の入力
usr = input("何時間働きましたか")
jikan = int(usr)

#計算
kyuryo = jikyu * jikan

#結果を表示
fmt = """
時給{0}円で{1}時間働いたので
給料は、{2}円です。
"""

desc = fmt.format(jikyu,jikan,kyuryo)
print(desc)
<<<<<<< HEAD

# 時給はいくらですか1000
# 何時間働きましたか3
#
# 時給1000円で3時間働いたので
# 給料は、3000円です。
=======
>>>>>>> parent of ee5d3b0... apdate
