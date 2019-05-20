class Tester:
    def __init__(self):
        # self.map = [
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','x','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','x','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','x','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','x','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','x','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','x','.','.','.','.','.','.','.','.','.'],
        #     ['.','.','.','.','.','.','.','.','.','.','.','.']
        # ]
        # self.sx = 4
        # self.sy = 5

        # self.map = [
        #     ['x','.','.','.','.','.'],
        #     ['.','x','.','.','.','.'],
        #     ['.','.','.','.','.','.'],
        #     ['.','x','.','.','.','.'],
        #     ['x','.','.','.','.','.'],
        #     ['.','.','.','.','.','.'],
        # ]
        # self.sx = 4
        # self.sy = 2

        # self.map = [
        #     ['x','.','x','.'],
        #     ['.','.','.','x'],
        #     ['x','.','x','.'],
        #     ['.','x','.','x']
        # ]
        # self.sx = 2
        # self.sy = 3

        # self.map = [
        #     ['.','.','.','.'],
        #     ['.','.','.','.'],
        #     ['x','.','.','.'],
        #     ['.','.','.','.']
        # ]
        # self.sx = 2
        # self.sy = 3

        mapa = []
        f = open("input", "r")

        nums = f.readline().split(' ')
        self.sx = int(nums[0])
        self.sy = int(nums[1])
        
        for line in f:
            l = list(line)[0:-1]
            mapa.append(l)
        f.close()

        self.map = mapa

        self.validMoves = ""
        self.movesCounter = 0
        self.found = 0

        self.treasureCount = 0
        for i in self.map:
            for j in i:
                if j == 'x':
                    self.treasureCount += 1

        self.x = len(self.map[0])
        self.y = len(self.map)

    def isValidPos(self, y, x):
        if y < 0 or x < 0 or x >= len(self.map[0]) or y >= len(self.map):
            return False
        return True

    def addMove(self, cmd):
        self.validMoves += cmd
        if cmd == 'H':
            return self.mov(-1, 0)
        if cmd == 'D':
            return self.mov(1, 0)
        if cmd == 'L':
            return self.mov(0, -1)
        if cmd == 'P':
            return self.mov(0, 1)

    def mov(self, dy, dx):
        if self.isValidPos(self.sy + dy, self.sx + dx):
            self.map[self.sy][self.sx] = '.'
            self.sx += dx
            self.sy += dy

            # print(self.sx, self.sy)
            
            if (self.map[self.sy][self.sx] == 'x'):
                self.found += 1
            self.movesCounter += 1

            if (self.found == self.treasureCount):
                return False
            return True

        return False

    def getFitness(self):
        fitness = (self.found*1000 - self.movesCounter*100)

        if (self.movesCounter):
            fitness *= (1 + (self.found/self.movesCounter))
        return fitness + 500

    def load(self, str):
        for i in str:
            if self.addMove(i) == False:
                break
        return self.getFitness()

    def foundAll(self):
        return self.treasureCount == self.found
    
    def printValid(self, str):
        print(self.validMoves)
    
    def printMap(self):
        for i in self.map:
            for j in i:
                print(j, end='')
            print('')
        print("start x:", self.sx, "y:", self.sy)
