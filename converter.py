START = '\tFrame\tX pixels\tY pixels\tZ pixels\t\n'
END = 'End of Keyframe Data\n'

BASE_LINES = [
    'Adobe After Effects 6.0 Keyframe Data\n',
    '\n',
    '\tUnits Per Second\t60\n',
    '\tSource Width\t1920\n',
    '\tSource Height\t1080\n',
	'\tSource Pixel Aspect Ratio\t1\n',
	'\tComp Pixel Aspect Ratio\t1\n'
]

class Position():
     def __init__(self, xPos, yPos):
        self.x = round(xPos, 3)
        self.y = round(yPos, 3)

class BasePosition():
    pixelsDif = 10

    def __init__(self, frame, xPos, yPos):
        self.frame = frame
        self.position = Position(xPos, yPos)

    @property
    def p1(self):
        return Position(self.position.x - self.pixelsDif , self.position.y + self.pixelsDif)
    @property
    def p2(self):
        return Position(self.position.x - self.pixelsDif , self.position.y - self.pixelsDif)
    @property
    def p3(self):
        return Position(self.position.x + self.pixelsDif , self.position.y - self.pixelsDif)
    @property
    def p4(self):
        return Position(self.position.x + self.pixelsDif , self.position.y + self.pixelsDif)

def getBaseLines():
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return lines


def getFrameBaseInfos(positionsBase):
    framesBaseInfos = []
    for positionBase in positionsBase:
        infos = [position for position in str(positionBase).split('\t') if position != '' and position != '\n']
        framesBaseInfos.append(BasePosition(int(infos[0]), float(infos[1]), float(infos[2])))
    return framesBaseInfos


def getPositionsBase(lines: list):
    positionsBase = []
    startingLine = lines.index(START)
    positionsBase = lines[startingLine+1:-3]
    return positionsBase

def createPowerPin(powerPinNum: int, framesBaseInfos: list):
    BASE_LINES.append(f'\nEffects\tCC Power Pin #1\tCC Power Pin-000{powerPinNum}\n')
    BASE_LINES.append('\tFrame\tX pixels\tY pixels\n')
    if(powerPinNum == 2):
        frame: BasePosition
        for frame in framesBaseInfos:
            BASE_LINES.append(f'\t{frame.frame}\t{frame.p1.x}\t{frame.p1.y}\n')
    elif(powerPinNum == 3):
        frame: BasePosition
        for frame in framesBaseInfos:
            BASE_LINES.append(f'\t{frame.frame}\t{frame.p2.x}\t{frame.p2.y}\n')
    if(powerPinNum == 4):
        frame: BasePosition
        for frame in framesBaseInfos:
            BASE_LINES.append(f'\t{frame.frame}\t{frame.p3.x}\t{frame.p3.y}\n')
    elif(powerPinNum == 5):
        frame: BasePosition
        for frame in framesBaseInfos:
            BASE_LINES.append(f'\t{frame.frame}\t{frame.p4.x}\t{frame.p4.y}\n')

def createFile(framesBaseInfos):
    createPowerPin(2, framesBaseInfos)
    createPowerPin(3, framesBaseInfos)
    createPowerPin(4, framesBaseInfos)
    createPowerPin(5, framesBaseInfos)
    BASE_LINES.append('\nEnd of Keyframe Data\n')
    with open("output.txt", "w") as f:
        f.writelines(BASE_LINES)

def execute():
    lines = getBaseLines()
    positionsBase = getPositionsBase(lines)
    framesBaseInfos = getFrameBaseInfos(positionsBase)
    createFile(framesBaseInfos)

if __name__ == "__main__":
    execute()