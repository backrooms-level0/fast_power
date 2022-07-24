

def power(x: int, y: int) -> int:
    """
    中文:参数x为底数,y为指数。
    English:The parameters x are base and y is exponential.
    """
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return power(x, y // 2) * power(x, y - (y // 2))

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = power(x, y)
    print(z)
