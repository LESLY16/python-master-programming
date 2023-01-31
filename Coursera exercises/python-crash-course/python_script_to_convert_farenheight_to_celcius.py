def to_celcius(x):
    return (x-32)*5/9

for i in range(0, 101, 10):
    print(i, to_celcius(i))