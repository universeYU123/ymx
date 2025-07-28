from app.models import User

def changeSelfInfo(username,formData,file):
    print(formData)
    user = User.objects.get(username=username)
    user.phone = formData['phone']
    user.sex = formData['sex']
    user.age = formData['age']
    user.career = formData['career']
    user.sleep_duration = formData['sleep_duration']
    user.sleep_quality = formData['sleep_quality']
    user.physical_activity_level = formData['physical_activity_level']
    user.pressure = formData['pressure']
    user.bmi = formData['bmi']
    user.blood_pressure = formData['blood_pressure']
    user.heart_rate = formData['heart_rate']
    user.daily_steps = formData['daily_steps']
    user.sleep_disorders = formData['sleep_disorders']
    user.state = formData['state']

    if formData['textarea']:
        user.textarea = formData['textarea']
    if file.get('avatar') != None:
        user.avatar = file.get('avatar')

    user.save()

def getChangePassword(userInfo,passwordInfo):
    oldPwd = passwordInfo['oldPassword']
    newPwd = passwordInfo['newPassword']
    newPwdConfirm = passwordInfo['newPasswordConfirm']
    user = User.objects.get(username=userInfo.username)
    if oldPwd != userInfo.password:return '原始密码不正确'
    if newPwd != newPwdConfirm :return '两次密码输入不正确'

    user.password = newPwd
    user.save()
