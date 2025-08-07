import random

print("\t\t\t-----Добро пожаловать в игру Pong-----")
height = 25
width = 80
paddleHeight = 3
isEnd = "w"


def drawField(leftPaddleY, rightPaddleY, leftPaddleX, rightPaddleX, ballX, ballY, firstUserPoints,secondUserPoints):     #Отрисовка поля
    field = []

    topBorder = '+' + '-' * (width - 2) + '+'
    field.append(topBorder)

    for y in range(1, height -1):
        rowChars = []
        for x in range(width):
            if x == 0:
                rowChars.append('|')
            elif x == width -1:
                rowChars.append('|')
            elif x == leftPaddleX and leftPaddleY <= y < leftPaddleY + paddleHeight:
                rowChars.append('|')
            elif x == rightPaddleX and rightPaddleY <= y < rightPaddleY + paddleHeight:
                rowChars.append('|')
            elif x == ballX and y == ballY:
                rowChars.append('o')
            else:
                rowChars.append(' ')
        field.append(''.join(rowChars))

    bottomBorder = '+' + '-' * (width - 2) + '+'
    field.append(bottomBorder)
    usersScore = ' ' * (width//2-3) + str(firstUserPoints) + ' : ' + str(secondUserPoints)
    field.append(usersScore)

    for line in field:
        print(line)


def ballDirectionControl(ballY, paddleY, ballX, paddleX):
    ballDirection = 2

    if ballY == paddleY:
        ballDirection = 1
    elif ballY == paddleY + 1:
        ballDirection = 2
    elif ballY == paddleY + 2:
        ballDirection = 3
    return ballDirection
    

def printCup():
    cup = """
           ___________
          /           \\
         /             \\
        /    ЗОЛОТАЯ    \\
       |                 |
       |     WINNER!     |
       |                 |
       |     РАКЕТКА     |
       |                 |
       |                 |
        \\               /
         \\             /
          \\___________/
            |     |
            |     |
            |     |
            |_____|
    """

    print(cup)
    
    
while isEnd != 'q':
    roundsAmount = int(input('Количество раундов: '))
    firstUserPoints = 0
    secondUserPoints = 0
    leftPaddleY = (height - paddleHeight) // 2
    rightPaddleY = (height - paddleHeight) // 2
    leftPaddleX = 1
    rightPaddleX = width - 2

    ballX = width // 2
    ballY = height // 2
    isFirstUserTurn = random.randint(0,1)
    ballDirection = 2 
    
    while firstUserPoints + secondUserPoints != roundsAmount:
        drawField(leftPaddleY,rightPaddleY,leftPaddleX,rightPaddleX,ballX,ballY,firstUserPoints,secondUserPoints)
        
        if ballX == leftPaddleX:
            ballX = width // 2
            ballY = height // 2
            isFirstUserTurn = 0
            secondUserPoints += 1
            
        elif ballX == rightPaddleX:
            ballX = width // 2
            ballY = height // 2
            isFirstUserTurn = 1
            firstUserPoints += 1
            
        userTurn = input('Твой ход: ')

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

        if ballY == 1:
            ballDirection = 3
        elif abs(ballY - height+1) == 1:
            ballDirection = 1


        if ballY <= leftPaddleY +2 and ballY >= leftPaddleY and abs(ballX - leftPaddleX) == 1:
            isFirstUserTurn = 0
            ballDirection = ballDirectionControl(ballY, leftPaddleY, ballX, leftPaddleX)

        elif ballY <= rightPaddleY +2 and ballY >= rightPaddleY and abs(ballX - rightPaddleX) == 1:
            isFirstUserTurn = 1
            ballDirection = ballDirectionControl(ballY, rightPaddleY, ballX, rightPaddleX)

        
        if isFirstUserTurn == 0:
            ballX += 1
        else:
            ballX -= 1
            
        if ballDirection == 1:
            ballY -= 1
        elif ballDirection == 3:
            ballY += 1

        if firstUserPoints == secondUserPoints and firstUserPoints + secondUserPoints == roundsAmount:
            print('Ничья! ' + str(firstUserPoints)+ ' : ' +  str(secondUserPoints))
            userAns = input('Хотите сыграть бонусный раунд? Y - Да | Остальное - Нет: ')
            if userAns == 'Y' or userAns == 'y':
                roundsAmount += 1
                continue
    
    drawField(leftPaddleY,rightPaddleY,leftPaddleX,rightPaddleX,ballX,ballY,firstUserPoints,secondUserPoints)
    printCup()
    if firstUserPoints > secondUserPoints:
        print('Игрок P1 выиграл набрав', firstUserPoints, 'очков')
    elif firstUserPoints < secondUserPoints:
        print('Игрок P2 выиграл набрав', secondUserPoints, 'очков')
    


    isEnd = input('Хочешь ли ты начать заново? q = нет, остальное = да: ')
    
