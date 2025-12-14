def z_func(s):  
    n = len(s)                                       
    z = [0] * len(s)
    left = 0                                             
    right = 0
    for i in range(1, n):
        if i > right:                               
            z[i] = 0
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:                   
                left = i
                right = i + z[i] - 1
        elif i <= right:
            z[i] = min(right-i+1, z[i-left])              
            while i + z[i] < n and s[z[i]] == s[i + z[i]]: 
                z[i] += 1
            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1

    return z
    # Сложность O(n)


if __name__ == '__main__':
    pattern = input().strip()  # подстрока
    text = input().strip()     # строка
    s = pattern + '#' + text
    z = z_func(s)
    p_len = len(pattern)
    # ищем все вхождения
    for i in range(p_len + 1, len(s)):
        if z[i] == p_len:
            print(i - p_len - 1)
