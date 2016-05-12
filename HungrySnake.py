# -*- coding: utf-8 -*-

from graphics import *
from random import randint

moveX = {"Up":0, "Down":0, "Left":-1, "Right":1}
moveY = {"Up":-1, "Down":1, "Left":0, "Right":0}
directions = {"Up":-1, "Down":1, "Left":2, "Right":-2}

defaultSize = 8
space = defaultSize + 1

maxX = 24
maxY = 24

firstFood = (15, 15)
startPoint = (13, 5)
startDirection = "Up"

basePoint = (5, 5)

bricks = []

logicMap = [
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

class Snake:
    def __init__(self, headPoint, moveDirection, food, graphWindow):
        self.body = []
        self.logicBody = []
        self.moveDirection = moveDirection
        self.headPoint = headPoint
        self.graphWindow = graphWindow
        self.food = food
        
        self.snakeHead = SnakeHead(headPoint)
        
        self.logicBody.insert(0, headPoint)
        self.body.insert(0, SnakeBody(headPoint))
        newPoint = (headPoint[0] - moveX[moveDirection], headPoint[1] - moveY[moveDirection])
        self.logicBody.insert(0, newPoint)
        self.body.insert(0, SnakeBody(newPoint))
        newPoint = (newPoint[0] - moveX[moveDirection], newPoint[1] - moveY[moveDirection])
        self.logicBody.insert(0, newPoint)
        self.body.insert(0, SnakeBody(newPoint))
        newPoint = (newPoint[0] - moveX[moveDirection], newPoint[1] - moveY[moveDirection])
        self.logicBody.insert(0, newPoint)
        self.body.insert(0, SnakeBody(newPoint))
        
        for b in self.body:
            b.draw(self.graphWindow)
        self.food.draw(self.graphWindow)
        self.snakeHead.draw(self.graphWindow)
            
    def newFood(self):
        while True:
            x = randint(0, maxX - 1)
            y = randint(0, maxY - 1)
            if ((x, y) in self.logicBody) or ((x,y) in bricks):
                continue
            self.food = Bread((x, y))
            self.food.draw(self.graphWindow)
            break
    
    def updateSnakeHead(self):
        self.snakeHead.undraw()
        self.snakeHead = SnakeHead(self.headPoint)
        self.snakeHead.draw(self.graphWindow)

    def move(self, changeDirection=""):
        if changeDirection in moveX:
            if directions[changeDirection] + directions[self.moveDirection] != 0:
                # 调整方向
                self.moveDirection = changeDirection
            else:
                # 反向运动
                self.headPoint = self.body[0].getPoint()
                self.body.reverse()
                self.moveDirection = changeDirection
        
        newPoint = (self.headPoint[0] + moveX[self.moveDirection], self.headPoint[1] + moveY[self.moveDirection])
        if newPoint[0] >= maxX:
            newPoint = (0, newPoint[1])
        elif newPoint[0] < 0:
            newPoint = (maxX - 1, newPoint[1])
        if newPoint[1] >= maxY:
            newPoint = (newPoint[0], 0)
        elif newPoint[1] < 0:
            newPoint = (newPoint[0], maxY - 1)
        
        if newPoint in bricks:
            return
        
        if self.food != None:
            if newPoint == self.food.getPoint():
                self.food.undraw()
                self.food = None
                self.newFood()
                self.headPoint = newPoint
                newHead = SnakeBody(newPoint)
                newHead.draw(self.graphWindow)
                self.body.append(newHead)
                self.logicBody.append(newHead.getPoint())
                
                self.updateSnakeHead()
                return
                
        if newPoint in self.logicBody:
            if newPoint != self.logicBody[0]:
                return
        self.logicBody.pop(0)
        self.logicBody.append(newPoint)
        
        oldTail = self.body.pop(0)
        oldTail.undraw()
        
        self.headPoint = newPoint
        newHead = SnakeBody(newPoint)
        newHead.draw(self.graphWindow)
        self.body.append(newHead)
        
        self.updateSnakeHead()
        
class GameObject:
    def __init__(self, logicPoint, body):
        self.point = logicPoint
        self.body = body
    def getPoint(self):
        return self.point
    def getBody(self):
        return body
    def draw(self, graphWindow):
        self.body.draw(graphWindow)
    def undraw(self):
        self.body.undraw()
    def _draw(self, canvas, options):
        self.body._draw(canvas, options)
        
class SnakeHead(GameObject):
    def __init__(self, logicPoint):
        p = Point(basePoint[0] + logicPoint[0] * space + defaultSize / 2, basePoint[1] + logicPoint[1] * space + defaultSize / 2)
        body = Circle(p, 2)
        body.setOutline('red') #外围轮廓颜色
        body.setFill('red') #填充颜色
        GameObject.__init__(self, logicPoint, body)

class SnakeBody(GameObject):
    def __init__(self, logicPoint):
        p1 = Point(basePoint[0] + logicPoint[0] * space, basePoint[1] + logicPoint[1] * space)
        p2 = Point(basePoint[0] + logicPoint[0] * space + defaultSize, basePoint[1] + logicPoint[1] * space + defaultSize)
        body = Rectangle(p1, p2)
        body.setOutline('red') #外围轮廓颜色
        body.setFill('yellow') #填充颜色
        GameObject.__init__(self, logicPoint, body)

class Playground(GameObject):
    def __init__(self, point):
        p1 = Point(point[0], point[1])
        p2 = Point(point[0] + maxX * space - 1, point[1] + maxY * space - 1)
        body = Rectangle(p1, p2)
        body.setOutline('red') #外围轮廓颜色
        GameObject.__init__(self, point, body)

class Brick(GameObject):
    def __init__(self, logicPoint):
        p1 = Point(basePoint[0] + logicPoint[0] * space, basePoint[1] + logicPoint[1] * space)
        p2 = Point(basePoint[0] + logicPoint[0] * space + defaultSize, basePoint[1] + logicPoint[1] * space + defaultSize)
        
        p3 = Point(basePoint[0] + logicPoint[0] * space + defaultSize, basePoint[1] + logicPoint[1] * space)
        p4 = Point(basePoint[0] + logicPoint[0] * space, basePoint[1] + logicPoint[1] * space + defaultSize)
        
        body = Rectangle(p1, p2)
        body.setOutline('black') #外围轮廓颜色
        GameObject.__init__(self, logicPoint, body)
        
        self.line1 = Line(p1, p2)
        self.line1.setOutline('black') #外围轮廓颜色
        
        self.line2 = Line(p3, p4)
        self.line2.setOutline('black') #外围轮廓颜色

    def draw(self, graphWindow):
        GameObject.draw(self, graphWindow)
        self.line1.draw(graphWindow)
        self.line2.draw(graphWindow)
        
    def undraw(self):
        GameObject.undraw(self)
        self.line1.undraw()
        self.line2.undraw()
    
    def _draw(self, canvas, options):
        GameObject._draw(self, canvas, options)
        self.line1._draw(canvas, options)
        self.line2._draw(canvas, options)
        
class Bread(GameObject):
    def __init__(self, logicPoint):
        p = Point(basePoint[0] + logicPoint[0] * space + defaultSize / 2, basePoint[1] + logicPoint[1] * space + defaultSize / 2)
        body = Circle(p, defaultSize / 2)
        body.setOutline('red') #外围轮廓颜色
        body.setFill('yellow') #填充颜色
        GameObject.__init__(self, logicPoint, body)


                

class Game:
    def __init__(self):
        #设置画布窗口名和尺寸
        self.width = maxX * space + basePoint[0]
        self.height = maxY * space + basePoint[1] + 50
        self.win = GraphWin('HungrySnake', self.width, self.height) 
        
        self.playground = Playground(basePoint)
        self.playground.draw(self.win)
        
        self.initBricks()

        newFood = Bread(firstFood)
        
        self.snake = Snake(startPoint, startDirection, newFood, self.win)
        
        self.speed = 250

        #显示文字
        self.message = Text(Point(self.width/2, self.height - 20), 'Press s to start.\nPress q to quit.')
        self.message.draw(self.win)
    
    def initBricks(self):
        for x in range(0, maxX):
            for y in range(0, maxY):
                if logicMap[x][y] == 1:
                    newPoint = (x, y)
                    bricks.append(newPoint)
                    newBrick = Brick(newPoint)
                    newBrick.draw(self.win)

    def start(self):
        while True:
            key = self.win.getKey()
            if 'q' == key:
                return
            elif 's' == key:
                break
        self.message.setText('Press p to pause/start.\nPress q to quit.')
        self.win.master.after(self.speed, self.run)#开始自动移动
        self.win.master.mainloop()
        
    def run(self):
        key = self.win.checkKey()
        if 'q' == key:
            self.win.close()
            sys.exit()
            return
        elif 'p' == key:
            if not self.waitForStartAgain():
                self.win.close()
                sys.exit()
                return
        self.snake.move(key)
        self.win.master.after(self.speed, self.run)

    def waitForStartAgain(self):
        while True:
            key = self.win.getKey()
            if 'q' == key:
                return False
            elif 'p' == key:
                return True

    def close(self):
        self.win.close()
        
if __name__ == '__main__':
    game = Game()
    game.start()
    game.close()