from app.utils import getPublicData
import datetime
travelInfoList = getPublicData.getAllTravelInfoMapData()
from app.models import User,HealthInfo
def cityCharDataOne():
    result = [
              ['product', '男性', '女性'],
              ['肥胖', len(HealthInfo.objects.filter(sex="男性").filter(bmi="肥胖")), len(HealthInfo.objects.filter(sex="女性").filter(bmi="肥胖"))],
              ['正常', len(HealthInfo.objects.filter(sex="男性").filter(bmi="正常")), len(HealthInfo.objects.filter(sex="女性").filter(bmi="正常"))],
              ['超重', len(HealthInfo.objects.filter(sex="男性").filter(bmi="超重")), len(HealthInfo.objects.filter(sex="女性").filter(bmi="超重"))],
            ]
    return result




def cityCharDataTwo():
    cityDic = {}
    for travel in travelInfoList:
        if cityDic.get(travel.sex, -1) == -1:
            cityDic[travel.sex] = 1
        else:
            cityDic[travel.sex] += 1
    resultData = []
    for key,value in cityDic.items():
        resultData.append({
            'name':key,
            'value':value
        })
    return resultData





from django.db.models import Avg

def getRateCharDataOne(category=None):
    name_li = ["睡眠呼吸暂停","无","失眠"]
    num_li = [
        HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg('age'))["avg_age"],
        HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg('age'))["avg_age"],
        HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg('age'))["avg_age"],
              ]
    if category == "睡眠时长":
        num_li = [
            HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg("sleep_duration"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg("sleep_duration"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg("sleep_duration"))["avg_age"],
        ]
    elif category == "睡眠质量":
        num_li = [
            HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg("sleep_quality"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg("sleep_quality"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg("sleep_quality"))["avg_age"],
        ]
    elif category == "身体活动水平":
        num_li = [
            HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg("physical_activity_level"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg("physical_activity_level"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg("physical_activity_level"))["avg_age"],
        ]
    elif category == "压力水平":
        num_li = [
            HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg("pressure"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg("pressure"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg("pressure"))["avg_age"],
        ]
    elif category == "心率":
        num_li = [
            HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg("heart_rate"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg("heart_rate"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg("heart_rate"))["avg_age"],
        ]
    elif category == "每日步数":
        num_li = [
            HealthInfo.objects.filter(sleep_disorders="睡眠呼吸暂停").aggregate(avg_age=Avg("daily_steps"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="无").aggregate(avg_age=Avg("daily_steps"))["avg_age"],
            HealthInfo.objects.filter(sleep_disorders="失眠").aggregate(avg_age=Avg("daily_steps"))["avg_age"],
        ]
    return name_li, num_li



def getRateCharDataTwo(travelList):
    startDic = {}
    for travel in travelList:
        if startDic.get(travel.like_count, -1) == -1:
            startDic[travel.like_count] = 1
        else:
            startDic[travel.like_count] += 1
    resultData = []
    for key, value in startDic.items():
        resultData.append({
            'name': key,
            'value': value
        })
    return resultData

def getPriceCharDataOne(traveList):
    xData = ['5000以内','7000以内','8000以内','9000以内','10000以内','10000以外']
    yData = [0 for x in range(len(xData))]
    for travel in traveList:
        price = float(travel.daily_steps)
        if price <= 5000:
            yData[0] += 1
        elif price <= 7000:
            yData[1] += 1
        elif price <= 8000:
            yData[2] += 1
        elif price <= 9000:
            yData[3] += 1
        elif price <= 10000:
            yData[4] += 1
        elif price > 10000:
            yData[5] += 1
    return xData,yData

def getPriceCharDataTwo(traveList):
    xData = ['6小时以内', '6小时-6.5小时', '6.5小时-7小时', '7小时以上']
    yData = [0 for x in range(len(xData))]
    for travel in traveList:
        price = float(travel.sleep_duration)
        if price <= 6:
            yData[0] += 1
        elif price <= 6.5:
            yData[1] += 1
        elif price <= 7:
            yData[2] += 1
       
        elif price > 7:
            yData[3] += 1
    return xData, yData




def getCommentsCharDataOne():
    commentsList = getPublicData.getAllCommentsData()
    xData = []
    def get_list(date):
        return datetime.datetime.strptime(date,'%Y-%m-%d').timestamp()
    for comment in commentsList:
        xData.append(comment['date'])
    xData = list(set(xData))
    xData = list(sorted(xData,key=lambda x: get_list(x),reverse=True))
    yData = [0 for x in range(len(xData))]
    for comment in commentsList:
        for index,date in enumerate(xData):
            if comment['date'] == date:
                yData[index] += 1
    return xData,yData

def getCommentsCharDataTwo():
    commentsList = getPublicData.getAllCommentsData()
    startDic = {}
    for travel in commentsList:
        if startDic.get(travel['score'], -1) == -1:
            startDic[travel['score']] = 1
        else:
            startDic[travel['score']] += 1
    resultData = []
    for key, value in startDic.items():
        resultData.append({
            'name': key,
            'value': value
        })
    return resultData




def getCommentsCharDataOne2(traveList):
    li = [nn.heart_rate for nn in traveList]
    li2 = list(set(li))
    print(li2)
    xData = sorted(li2)
    yData = []
    for xx in xData:
        yData.append(len(HealthInfo.objects.filter(heart_rate=xx)))

    return xData,yData


def getCommentsCharDataOne3(traveList):
    li = [nn.blood_pressure.split("/")[0] for nn in traveList]
    li2 = list(set(li))
    print(li2)
    xData = sorted(li2)
    yData = []
    for xx in xData:
        yData.append(len(HealthInfo.objects.filter(blood_pressure__icontains=(xx+"/"))))

    li5 = [nn.blood_pressure.split("/")[1] for nn in traveList]
    li6 = list(set(li5))
    print(li6)
    xData2 = sorted(li6)
    yData2 = []
    for xx2 in xData2:
        yData2.append(len(HealthInfo.objects.filter(blood_pressure__icontains=("/"+xx2))))

    return xData,yData,xData2,yData2