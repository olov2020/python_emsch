# №1
# n = 3
# a = int(input())
# b = int(input())
# c = int(input())
# max_num = max(a, max(b, c))
# min_num = min(a, min(b, c))
# mediana = a + b + c - min_num - max_num
# ans1 = '{:.6}'.format((a + b + c) / n)
# ans2 = '{:.6}'.format(n / (1 / a + 1 / b + 1 / c))
# ans4 = '{:.6}'.format(max_num ** min_num / mediana)
# print(ans1, ans2, mediana, ans4, sep='; ')


# №3
# n = int(input())
# hours = n // 60 % 24
# minutes = n % 60 % 60
# print(hours, minutes)


# №4
# a = int(input())
# b = int(input())
# c = int(input())
# print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)


# №5
# a, b, c = map(int, input().split())
# p2 = (a + b + c) / 2
# square = (p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5
# print('{:.3}'.format(square))


# №6
# a, b, c = map(int, input().split())
# d = b * b - 4 * a * c
# x1 = (-b - d ** 0.5) / (2 * a)
# x2 = (-b + d ** 0.5) / (2 * a)
# print(x1, x2)
