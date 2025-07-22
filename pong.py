#Выбор количества раундов
roundsAmount = int(input('Количество раундов'))
height = 25
width = 80
paddleHeight = 3
isEnd = "w"


def drawField(left_paddle_y, right_paddle_y, left_paddle_x, right_paddle_x, ball_x, ball_y):     #Отрисовка поля
    field = []

    top_border = '+' + '-' * (width - 2) + '+'
    field.append(top_border)

    for y in range(1, height -1):
        row_chars = []
        for x in range(width):
            if x == 0:
                row_chars.append('|')
            elif x == width -1:
                row_chars.append('|')
            elif x == left_paddle_x and left_paddle_y <= y < left_paddle_y + paddleHeight:
                row_chars.append('|')
            elif x == right_paddle_x and right_paddle_y <= y < right_paddle_y + paddleHeight:
                row_chars.append('|')
            elif x == ball_x and y == ball_y:
                row_chars.append('o')
            else:
                row_chars.append(' ')
        field.append(''.join(row_chars))

    bottom_border = '+' + '-' * (width - 2) + '+'
    field.append(bottom_border)

    for line in field:
        print(line)




while isEnd != 'q':
    firstUserPoints = 0
    secondUserPoints = 0
    leftPaddleY = (height - paddleHeight) // 2
    rightPaddleY = (height - paddleHeight) // 2
    leftPaddleX = 1
    rightPaddleX = width - 2

    ballX = width // 2
    ballY = height // 2

    while firstUserPoints + secondUserPoints != roundsAmount:
        drawField(leftPaddleY,rightPaddleY,leftPaddleX,rightPaddleX,ballX,ballY)
        userTurn = input('Твой ход')
        print(leftPaddleY)

        if userTurn == 'a':
            if leftPaddleY > 1:
                leftPaddleY -= 1
            else:
                print('Левая ракетка уже в верхней границе.')
        elif userTurn == 'z':
            if leftPaddleY < 21:
                leftPaddleY += 1
            else:
                print('Левая ракетка уже в нижней границе.')
        elif userTurn == 'k':
            if rightPaddleY > 1:
                rightPaddleY -= 1
            else:
                print('Правая ракетка уже в верхней границе.')
        elif userTurn == 'm':
            if rightPaddleY < 21:
                rightPaddleY += 1
            else:
                print('Правая ракетка уже в нижней границе.')
        else:
            print('Такой команды не существует')
            
            
    
    #Движение ракеток
    isEnd = input('Хочешь ли ты начать заново? q = нет, остальное = да: ')

    

    



        


















    
    
