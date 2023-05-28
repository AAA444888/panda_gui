#計算BMR
def count(age,sex,BMI):
    BMI=float(BMI)
    BMR=((1.2)*BMI+(0.23)*int(age)-5.4-(10.8)*(2-int(sex)))
    BMR=round(BMR,2)
    return BMR
#BMR判定
def category(sex,BMR):
    sex=int(sex)
    #區分男生及女生的判定
    if sex==2:
        if BMR<=13:
            print('BMR:'+str(BMR)+"%, 基礎脂肪")
            return "基礎脂肪"
        elif BMR<=20:
            print('BMR:'+str(BMR)+"%, 運動員")
            return "運動員"
        elif BMR<=24:
            print('BMR:'+str(BMR)+"%, 健康")
            return "健康"
        elif BMR<=31:
            print('BMR:'+str(BMR)+"%, 正常")
            return "正常"
        else:
            print('BMR:'+str(BMR)+"%, 肥胖")
            return "肥胖"
    else:
        if BMR<=5:
            print('BMR:'+str(BMR)+"%, 基礎脂肪")
            return "基礎脂肪"
        elif BMR<=13:
            print('BMR:'+str(BMR)+"%, 運動員")
            return "運動員"
        elif BMR<=17:
            print('BMR:'+str(BMR)+"%, 健康")
            return "健康"
        elif BMR<=24:
            print('BMR:'+str(BMR)+"%, 正常")
            return "正常"
        else:
            print('BMR:'+str(BMR)+"%, 肥胖")
            return "肥胖"