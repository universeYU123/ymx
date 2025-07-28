from app.models import HealthInfo,User
from app.utils.getHomeData import getNowTime
import json

def getTravelById(id):
    travel = HealthInfo.objects.get(id=id)
    travel.comments = json.loads(travel.comments)

    return travel

def addComments(commentData):
    # 'author': author,
    # 'content': content,
    # 'date': date,
    # 'score': score
    # authorId
    year,month,day = getNowTime()
    travelInfo = commentData['travelInfo']
    travelInfo.comments.append({
        'author':commentData['userInfo'].username,
        'score':commentData['rate'],
        'content':commentData['content'],
        'date':str(year) + '-' + str(month) + '-' + str(day),
        'userId':commentData['userInfo'].id,
    })
    travelInfo.comments = json.dumps(travelInfo.comments)
    travelInfo.save()
    
    
    
def getTravelById2(id):
    travel = User.objects.get(id=id)
    travel.comments = json.loads(travel.comments)

    return travel

def addComments2(commentData):
    # 'author': author,
    # 'content': content,
    # 'date': date,
    # 'score': score
    # authorId
    year,month,day = getNowTime()
    travelInfo = commentData['travelInfo']
    travelInfo.comments.append({
        'author':commentData['userInfo'].username,
        'score':commentData['rate'],
        'content':commentData['content'],
        'date':str(year) + '-' + str(month) + '-' + str(day),
        'userId':commentData['userInfo'].id,
    })
    travelInfo.comments = json.dumps(travelInfo.comments)
    travelInfo.save()