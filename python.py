class BusData:
    def __init__(self, lineID, lineName, order, sectionID, butStopID, ARS_ID, busStopName, xCoord, yCoord):
        self.lineID = lineID
        self.lineName = lineName
        self.order = order
        self.sectionID = sectionID
        self.butStopID = butStopID
        self.ARS_ID = ARS_ID
        self.busStopName = busStopName
        self.xCoord = xCoord
        self.yCoord = yCoord

def makeList(lineID, lineName, order, sectionID, butStopID, ARS_ID, busStopName, xCoord, yCoord, busdataList):
        busdata=BusData(lineID, lineName, order, sectionID, butStopID, ARS_ID, busStopName, xCoord, yCoord)
        busdataList.append(busdata)

busdataList=[]

with open("busdata.csv", 'r', encoding='UTF8') as file:
    for line in file:
        (lineID, lineName, order, sectionID, butStopID, ARS_ID, busStopName, xCoord, yCoord) = line.strip().split(",")
        if (not lineID) or (not lineName) or (not order) or (not sectionID) or (not butStopID) or (not ARS_ID) or (
        not busStopName) or (not xCoord) or (not yCoord):
            continue
        else:
            makeList(lineID, lineName, order, sectionID, butStopID, ARS_ID, busStopName, xCoord, yCoord, busdataList)

def printMenu():
    print('\n'.join([
        "="*35,
        "1. 정류장 정차 버스 찾기",
        "2. 버스노선의 정차 정류장 찾기",
        "3. 종료",
        "="*35,
        "정수값을 입력하시오: "
    ]))

def option():
    while True:
        printMenu()
        getNum = input()
        if getNum != "1" and getNum != "2" and getNum != "3":
            print("다시 입력해주세요")
            continue
        elif getNum == "1":
            getBusStopName = input("정류장 이름을 입력하세요 (일부 명칭도 가능): ")
            whichBusStopped(getBusStopName, busdataList)
        elif getNum == "2":
            getLineName = input("버스노선명을 입력하세요: ")
            whereItHadBeen(getLineName, busdataList)
        elif getNum == "3":
            break

def whichBusStopped(getBusStopName, busdataList):
    for element in busdataList:
        if getBusStopName in element.busStopName:
            print(element.lineName)

def whereItHadBeen(getLineName, busdataList):
    for element in busdataList:
        if getLineName in element.lineName:
            print(element.busStopName)


'''실제 구현파트'''
option()