#計算BMI
def calculate(height,weight):
    BMI=int(weight)/((int(height)/100)**2)
    BMI=round(BMI,2)
    return BMI
#判定體位
def category(BMI):
    BMI=float(BMI)
    if BMI<18.5:
        print('BMI:'+str(BMI)+", 過輕")
        return "過輕"
    elif 18.5<=BMI and BMI<24:
        print('BMI:'+str(BMI)+", 理想體重")
        return "理想體重"
    elif 24<=BMI and BMI<27:
        print('BMI:'+str(BMI)+", 過重")
        return "過重"
    else:
        print('BMI:'+str(BMI)+", 肥胖")
        return "肥胖"
