# simple_calculator.py
# 簡単な計算機プログラム（初心者向け）

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0で割ることはできません"
    return a / b

def main():
    print("簡単な計算機へようこそ！")
    x = float(input("1つ目の数字を入力してください: "))
    y = float(input("2つ目の数字を入力してください: "))

    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")

if __name__ == "__main__":
    main()

