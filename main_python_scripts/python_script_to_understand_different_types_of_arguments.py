def add_tax_many(hra, lta, pt=0, abc=0, bcd=10):
    print("hra", hra, "lta", lta, "pt", pt, "abc", abc, "bcd", bcd)
    return hra + lta + pt + abc + bcd

print(add_tax_many(100, 50, 0, 0, 10))
print(add_tax_many(100, 150, 0, 0, 10))
print(add_tax_many(20, 50, 0, 0, 10))

print(add_tax_many(100, 50))
print(add_tax_many(100, 150))
print(add_tax_many(20, 50))

# Named arguments
print(add_tax_many(20, 50, abc=5))
print(add_tax_many(20, 30, 11, bcd=33))

# Positional arguments
print(add_tax_many(20, 50, 8))
print(add_tax_many(20, 30, 11, 22, 33))