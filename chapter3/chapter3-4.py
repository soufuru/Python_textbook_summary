# chapter3-4

################
###---関数---###
################

def mul(a,b):
    '''掛け算を行う関数''' # docstring(関数の説明)を指定
    return a*b

print(mul(3,4))
# print(help(mul)) # docstringを表示

# 引数にデフォルト値をつける
def convert_jou(jou, unit="江戸間"):
    if unit == "江戸間":
        base = 0.88 * 1.76
    elif unit == "京間":
        base = 0.955 * 1.91
    elif unit == "中京間":
        base = 0.91 * 1.82
    m2 = jou * base
    s = "{0}で{1}畳は{2}m^2".format(unit,jou,m2)
    print(s)


# 関数を実行
convert_jou(6, "江戸間")
convert_jou(6)

# 可変長引数の指定
def sumArgs(*args):
    v = 0
    for n in args:
        v += n
    return v

print(sumArgs(1,2,3))
print(sumArgs(1,2,3,4,5,6))
