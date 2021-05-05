'''
Напишете функција која ќе ги содржи функционалностите на едноставен аритметички калкулатор. Интеракција со калкулаторот треба да се врши преку читање на параметри од стандардниот влез со наредбата input(), т.е. се внесуваат двата операнди и операторот во командна линија. По процесирање на барањето од страна на функцијата се обработува и печати се печати резултатот на екран. Командите кои ги испраќаме на калкулаторот се читаат од стандарден влез и треба да го имаат следниот формат:

операнд1

оператор

операнд2

Доколку настанала грешка при внес соодветно да се извести корисникот. Калкулаторот треба да ги подржува следните операции:

Собирање (+) Одземање (-) Множење (*) Целобројно делење (//) Делење (/) Модуло (остаток) (%) Степенување (**)
'''


# __operators = ('+','-', '/' , '//', '*', '**', '%')


def calculator():          # we define function that handles the input two numbers and one operator(string) and prints the calculated result
    x = eval(input())
    operator = input()
    y = eval(input())

    result = 0

    if operator == "+":       # check which string is stored in the operator variable and based on that make the arithmetic calculation
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "/":
        result = x / y
    elif operator == "//":
        result = x // y
    elif operator == "*":
        result = x * y
    elif operator == "**":
        result = x ** y
    elif operator == "%":
        result = x % y
    else:
        print("greshka vo vlez")

    print(result)       # just print out the calculated result on stdout


if __name__ == "__main__":
    calculator()               # do the function call.
