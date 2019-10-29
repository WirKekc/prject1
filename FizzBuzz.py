a, b = map(int, (input().split()))
for i in range(a, b+1):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)
 # Короткое решение
# start, end = map(int, input().split())
# for i in range(start, end + 1):
#     print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)