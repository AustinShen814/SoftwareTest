rate_CNYtoJPY = 20.00
rate_CNYtoUSD = 0.14
rate_JPYtoCNY = 0.05
rate_USDtoCNY = 1/rate_CNYtoUSD

def cny_to_jpy(amount):
   jpy = amount * rate_CNYtoJPY
   print(f"{amount}人民币转换成日元为：{jpy:.1f}日元")
   return jpy

def cny_to_usd(amount):
    usd = amount * rate_CNYtoUSD
    print(f"{amount} 人民币转换成美元为：{usd:.1f} 美元")
    return usd

def jpy_to_cny(amount):
    cny = amount * rate_JPYtoCNY
    print(f"{amount} 日元转换成人民币为：{cny:.1f} 人民币")
    return cny

def usd_to_cny(amount):
    cny = amount * rate_USDtoCNY
    print(f"{amount} 美元转换成人民币为：{cny:.1f} 人民币")
    return cny


def Currency_Exchange(amount, method):
    if amount < 0:
        print("错误，金额不能为附属")
        return None;

    if method == "cny_to_jpy":
        result = amount * rate_CNYtoJPY
        target_currency = "日元"
        source_currency = "人民币"

    elif method == "cny_to_usd":
        result = amount * rate_CNYtoUSD
        target_currency = "美元"
        source_currency = "人民币"

    elif method == "jpy_to_cny":
        result = amount * rate_JPYtoCNY
        target_currency = "人民币"
        source_currency = "日元"

    elif method == "usd_to_cny":
        result = amount * rate_USDtoCNY
        target_currency = "人民币"
        source_currency = "美元"

    else:
        print(f"错误：不支持的兑换方法 '{method}'")
        return None

    print(f"{amount} {source_currency} 转换成 {target_currency} 为：{result:.1f} {target_currency}")
    return result

    #测试用例 1:100人民币兑换美元  预期结果 14美元
    #测试用例 2:100美元兑换人民币  预期结果 714.3人民币
    #测试用例 3:0美元兑换人民币    预期结果 0人民币
    #测试用例 4:100人民币兑换日元  预期结果 2000日元
    #测试用例 5:100日元兑换美元    预期结果 错误
    #测试用例 6:-100 日元兑换美元  预期结果 错误


def main():
    print("测试用例1:100人民币兑换美元")
    Currency_Exchange(100, "cny_to_usd")
    print()

    print("测试用例2:100美元兑换人民币")
    Currency_Exchange(100, "usd_to_cny")
    print("\n")

    print("测试用例3:0美元兑换人民币")
    Currency_Exchange(0,"usd_to_cny")
    print("\n")

    print("测试用例 4：100人民币兑换日元")
    Currency_Exchange(100, "cny_to_jpy")
    print("\n")

    print("测试用例 5:100日元兑换美元")
    Currency_Exchange(100, "jpy_to_usd")
    print("\n")

    print("测试用例 6:-100日元兑换美元")
    Currency_Exchange(-100, "jpy_to_usd")


if __name__ == "__main__":
    main()