#chapter4-2

#########################
###---ファイル読み込み---###
#########################

# (1)テキストファイルを開く
a_file = open("mt7_7.txt",encoding="utf-8")

# (2)テキストを読む
s = a_file.read()

# (3)ファイルを閉じる
a_file.close()

# 結果を表示する
print(s)

#########################
###---ファイル書き込み---###
#########################

# modeについて
# w : ファイルを書き込みモードで開く
# r : ファイルを読み込みモードで開く(デフォルト)
# a : 書き込み用に開き、ファイルが存在すれば末尾に追記する
# b : バイナリモード
# t : テキストモード(デフォルト)

# (1)テキストファイルを開く
a_file = open("test.txt",mode="w", encoding="utf-8")

# (2)ファイルに書き込む
a_file.write("私は失敗したことがない\n")
a_file.write("ただ、一万通りの方法を\n見つけただけだ\n")
a_file.write("ートーマス・エジソン\n")

# (3)ファイルを閉じる
a_file.close()

# with公文を使って楽をする
with open("test.txt",mode="w") as f:
    f.write("私は失敗したことがない\n")
    f.write("ただ、一万通りの方法を\n見つけただけだ\n")
# 自動的にclose()してくれる。
