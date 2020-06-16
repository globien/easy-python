def cbrt(a):
    s = -1 if a < 0 else 1
    return s * (a*s) ** (1/3)

print(cbrt(-8))     # -2.0
print(cbrt(8))      # 2.0
print(cbrt(0))      # 0.0