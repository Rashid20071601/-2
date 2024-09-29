def get_password(n):
    if n < 3 or n > 20:
        return "Число должно быть от 3 до 20."
    result = ""
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += f"{i}{j} "
    return result

print(get_password(3))