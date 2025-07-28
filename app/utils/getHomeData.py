from app.utils import getPublicData
import random
import time

travelMapData = getPublicData.getAllTravelInfoMapData()
userData = getPublicData.getAllUsersInfoData()


def getHomeTagData():
    a5Len = 0
    commentsLenMax = 0
    commentsLenTitle = ''
    provienceDic = {}
    for travel in travelMapData:
        if travel.bmi == '正常': a5Len += 1
        if int(travel.age) > commentsLenMax:
            commentsLenMax = int(travel.age)
            commentsLenTitle = travel.career
        if provienceDic.get(travel.sleep_disorders, -1) == -1:
            provienceDic[travel.sleep_disorders] = 1
        else:
            provienceDic[travel.sleep_disorders] += 1

    provienceDicSort = list(sorted(provienceDic.items(), key=lambda x: x[1], reverse=True))[0][0]
    # provienceDicSort = []
    return a5Len, commentsLenTitle, provienceDicSort


def getAnthorData():
    scoreTop10 = []
    for travel in travelMapData:
        if int(travel.daily_steps) > 5000:
            scoreTop10.append(travel)

    maxLen = len(scoreTop10)
    scoreTop10Data = []
    for i in range(10):
        randomIndex = random.randint(0, maxLen - 1)
        scoreTop10Data.append(scoreTop10[randomIndex])

    saleCountTop10 = list(sorted(travelMapData, key=lambda x: int(x.heart_rate), reverse=True))[:10]

    return scoreTop10Data, saleCountTop10


def getNowTime():
    timeFormat = time.localtime()
    year = timeFormat.tm_year
    mon = timeFormat.tm_mon
    day = timeFormat.tm_mday
    return year, mon, day


def getGeoData():
    dataDic = {}
    for i in travelMapData:
        for j in getPublicData.cityList:
        #     for city in j['city']:
        #         if city.find(i.province) != -1:
            if dataDic.get(j['province'], -1) == -1:
                dataDic[j['province']] = 1
            else:
                dataDic[j['province']] += 1

    resutData = []
    for key, value in dataDic.items():
        resutData.append({
            'name': key,
            'value': value
        })
    return resutData


def getUserCreateTimeData():
    dataDic = {}
    for user in userData:
        if dataDic.get(str(user.createTime), -1) == -1:
            dataDic[str(user.createTime)] = 1
        else:
            dataDic[str(user.createTime)] += 1

    resutData = []
    for key, value in dataDic.items():
        resutData.append({
            'name': key,
            'value': value
        })
    return resutData

