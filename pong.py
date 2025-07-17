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
    leftPaddleY = (height - paddleHeight) // 2
    rightPaddleY = (height - paddleHeight) // 2
    leftPaddleX = 1
    rightPaddleX = width - 2

    ballX = width // 2
    ballY = height // 2
    drawField(leftPaddleY,rightPaddleY,leftPaddleX,rightPaddleX,ballX,ballY)
    #for i in range(roundsAmount):
        #логика игры
    #Движение ракеток
    isEnd = input('Хочешь ли ты начать заново? q = нет, остальное = да')

    

    



        


















    
    
