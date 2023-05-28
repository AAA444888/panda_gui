#用身高來計算標準體重
def weight(height,BMI):
    a=18.5*((int(height)/100)**2)
    b=24*((int(height)/100)**2)
    BMI=float(BMI)
    a=round(a,2)
    b=round(b,2)
    #輸出理想體重
    if 18.5<=BMI and BMI<24:
        print("理想體重:"+str(a)+"~"+str(b))
        print("在理想體重內")
        return str(a)+"~"+str(b)
    else:
        print("理想體重:"+str(a)+"~"+str(b))
        return str(a)+"~"+str(b)