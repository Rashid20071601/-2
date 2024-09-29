n = int(input('Введите целое число от 3 до 20: '))
def get_password(password):
    if password < 3 or password > 20:
        return "Число должно быть от 3 до 20."
    result = ""
    for i in range(1, password + 1):
        for j in range(i + 1, password + 1):
            if password % (i + j) == 0:
                result += f"{i}{j} "
    return result

print('Пароль:', get_password(n))
