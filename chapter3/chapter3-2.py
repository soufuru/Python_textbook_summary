# chapter3-2

########################
###---辞書型について---###
########################

age = {"鈴木": 30, "井上":20, "伊藤": 22}
print(age["鈴木"]) # 30
print(age.keys() ) # dict_keys(['鈴木', '井上', '伊藤'])

fruits =  {
    "バナナ"   :300,
    "オレンジ" :240,
    "いちご"   :350,
    "マンゴー" :400
}

for name in fruits.keys():
    price = fruits[name]
    print("{0}は、{1}円です。".format(name, price) )

for name in fruits:
    price = fruits[name]
    print(price) 
