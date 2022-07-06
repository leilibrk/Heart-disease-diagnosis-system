def chestPain_mem(chest_pain):
    chest_pain = int(chest_pain)
    mem_chest_pain = [0 for i in range(4)]
    if chest_pain == 1:
        mem_chest_pain[0] = 1
    if chest_pain == 2:
        mem_chest_pain[1] = 1
    if chest_pain == 3:
        mem_chest_pain[2] = 1
    if chest_pain == 4:
        mem_chest_pain[3] = 1
    return mem_chest_pain


def sex_mem(sex):
    sex = int(sex)
    mem_sex = [0 for i in range(2)]
    if sex == 0:
        mem_sex[0] = 1
    if sex == 1:
        mem_sex[1] = 1
    return mem_sex


def thallium_mem(thallium):
    thallium = int(thallium)
    mem_thallium = [0 for i in range(3)]
    if thallium == 3:
        mem_thallium[0] = 1
    if thallium == 6:
        mem_thallium[1] = 1
    if thallium == 7:
        mem_thallium[2] = 1
    return mem_thallium


def exercise_mem(exe):
    exe = int(exe)
    mem_exercise = [0 for i in range(2)]
    if exe == 0:
        mem_exercise[0] = 1
    if exe == 1:
        mem_exercise[1] = 1
    return mem_exercise


def age_mem(age):
    age = int(age)
    membership_age = [0 for i in range(4)]
    if age < 29:
        membership_age[0] = 1
    if 29 <= age <= 38:
        membership_age[0] = (38 - age) / 9
    if 33 <= age <= 38:
        membership_age[1] = (age - 33) / 5
    if 38 <= age <= 45:
        membership_age[1] = (45 - age) / 7
    if 40 <= age <= 48:
        membership_age[2] = (age - 40) / 8
    if 48 <= age <= 58:
        membership_age[2] = (58 - age) / 10
    if 52 <= age <= 60:
        membership_age[3] = (age - 52) / 8
    if age >= 58:
        membership_age[3] = 1
    return membership_age


def blood_pres_mem(blood_pressure):
    blood_pressure = int(blood_pressure)
    membership_bloodpres = [0 for i in range(4)]
    if blood_pressure < 111:
        membership_bloodpres[0] = 1
    if 111 <= blood_pressure <= 134:
        membership_bloodpres[0] = (134 - blood_pressure) / 23
    if 127 <= blood_pressure <= 139:
        membership_bloodpres[1] = (blood_pressure - 127) / 12
    if 139 <= blood_pressure <= 153:
        membership_bloodpres[1] = (153 - blood_pressure) / 14
    if 142 <= blood_pressure <= 157:
        membership_bloodpres[2] = (blood_pressure - 142) / 15
    if 157 <= blood_pressure <= 172:
        membership_bloodpres[2] = (172 - blood_pressure) / 15
    if 154 <= blood_pressure <= 171:
        membership_bloodpres[3] = (blood_pressure - 154) / 17
    if blood_pressure > 171:
        membership_bloodpres[3] = 1
    return membership_bloodpres


def blood_sugar_mem(blood_sugar):
    blood_sugar = int(blood_sugar)
    membership_bloodSugar = [0 for i in range(1)]
    if blood_sugar < 105:
        membership_bloodSugar[0] = 0
    if 105 <= blood_sugar <= 120:
        membership_bloodSugar[0] = (blood_sugar - 105) / 15
    if blood_sugar > 120:
        membership_bloodSugar[0] = 1
    return membership_bloodSugar


def cholesterol_mem(cholesterol):
    cholesterol = int(cholesterol)
    membership_chol = [0 for i in range(4)]
    if cholesterol < 151:
        membership_chol[0] = 1
    if 151 <= cholesterol <= 197:
        membership_chol[0] = (197 - cholesterol) / 46
    if 188 <= cholesterol <= 215:
        membership_chol[1] = (cholesterol - 188) / 27
    if 215 <= cholesterol <= 250:
        membership_chol[1] = (250 - cholesterol) / 35
    if 217 <= cholesterol <= 263:
        membership_chol[2] = (cholesterol - 217) / 46
    if 263 <= cholesterol <= 307:
        membership_chol[2] = (307 - cholesterol) / 44
    if 281 <= cholesterol <= 347:
        membership_chol[3] = (cholesterol - 281) / 66
    if cholesterol > 347:
        membership_chol[3] = 1
    return membership_chol


def maximum_heart_rate_mem(maximum_heart_rate):
    maximum_heart_rate = int(maximum_heart_rate)
    membership_heartRate = [0 for i in range(3)]
    if maximum_heart_rate < 100:
        membership_heartRate[0] = 1
    if 100 <= maximum_heart_rate <= 141:
        membership_heartRate[0] = (141 - maximum_heart_rate) / 41
    if 111 <= maximum_heart_rate <= 152:
        membership_heartRate[1] = (maximum_heart_rate - 111) / 41
    elif 152 <= maximum_heart_rate <= 194:
        membership_heartRate[1] = (194 - maximum_heart_rate) / 42
    if 152 <= maximum_heart_rate <= 210:
        membership_heartRate[2] = (maximum_heart_rate - 152) / 58
    if maximum_heart_rate > 210:
        membership_heartRate[2] = 1
    return membership_heartRate


def ecg_mem(ECG):
    ECG = float(ECG)
    membership_ECG = [0 for i in range(3)]
    if ECG < 0:
        membership_ECG[0] = 1
    if 0 <= ECG <= 0.4:
        membership_ECG[0] = (0.4 - ECG) / 0.4
    if 0.2 <= ECG <= 1:
        membership_ECG[1] = (ECG - 0.2) / 0.8
    elif 1 <= ECG <= 1.8:
        membership_ECG[1] = (1.8 - ECG) / 0.8
    if 1.4 <= ECG <= 1.9:
        membership_ECG[2] = (ECG - 1.4) / 0.5
    if ECG > 1.9:
        membership_ECG[2] = 1
    return membership_ECG


def oldpeak_mem(oldPeak):
    oldPeak = float(oldPeak)
    membership_oldPeak = [0 for i in range(3)]
    if oldPeak < 1:
        membership_oldPeak[0] = 1
    if 1 <= oldPeak <= 2:
        membership_oldPeak[0] = (2 - oldPeak) / 1
    if 1.5 <= oldPeak <= 2.8:
        membership_oldPeak[1] = (oldPeak - 1.5) / 1.3
    elif 2.8 <= oldPeak <= 4.2:
        membership_oldPeak[1] = (4.2 - oldPeak) / 1.4
    if 2.5 <= oldPeak <= 4:
        membership_oldPeak[2] = (oldPeak - 2.5) / 1.5
    if oldPeak > 4:
        membership_oldPeak[2] = 1
    return membership_oldPeak


def output_mem(outputSick):
    membership_outputSick = [0 for i in range(5)]
    if outputSick < 0.25:
        membership_outputSick[4] = 1
    if 0.25 <= outputSick <= 1:
        membership_outputSick[4] = (1 - outputSick) / 0.75
    if 0 <= outputSick <= 1:
        membership_outputSick[0] = (outputSick - 0) / 1
    elif 1 <= outputSick <= 2:
        membership_outputSick[0] = (2 - outputSick) / 1
    if 1 <= outputSick <= 2:
        membership_outputSick[1] = (outputSick - 1) / 1
    elif 2 <= outputSick <= 3:
        membership_outputSick[1] = (3 - outputSick) / 1
    if 2 <= outputSick <= 3:
        membership_outputSick[2] = (outputSick - 2) / 1
    elif 3 <= outputSick <= 4:
        membership_outputSick[2] = (4 - outputSick) / 1
    if 3 <= outputSick <= 3.75:
        membership_outputSick[3] = (outputSick - 3) / 0.75
    if outputSick > 3.75:
        membership_outputSick[3] = 1
    return membership_outputSick
