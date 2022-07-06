import inference
import defuzzification


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        chest_pain = input_dict["chest_pain"]
        cholestrol = input_dict["cholestrol"]
        ecg = input_dict["ecg"]
        exercise = input_dict["exercise"]
        thallium = input_dict["thallium_scan"]
        age = input_dict["age"]
        blood_pressure = input_dict["blood_pressure"]
        blood_sugar = input_dict["blood_sugar"]
        heart_rate = input_dict["heart_rate"]
        sex = input_dict["sex"]
        old_peak = input_dict["old_peak"]
        sick1_mem, sick2_mem, sick3_mem, sick4_mem, healthy_mem = inference.inference(age, blood_pressure, blood_sugar,
                                                                                      cholestrol, heart_rate, ecg,
                                                                                      old_peak, chest_pain, sex,
                                                                                      thallium, exercise)
        cmp = defuzzification.defuzzify(sick1_mem, sick2_mem, sick3_mem, sick4_mem, healthy_mem)
        res = ''
        if cmp < 1.78:
            res += 'healthy '
        if 1 <= cmp <= 2.51:
            if res is not '':
                res += '& '
            res += 'Sick1 '
        if 1.78 <= cmp <= 3.25:
            if res is not '':
                res += '& '
            res += 'Sick2 '
        if 1.5 <= cmp <= 4.5:
            if res is not '':
                res += '& '
            res += 'Sick3 '
        if cmp > 3.25:
            if res is not '':
                res += '& '
            res += 'Sick4 '
        res += ': ' + str(cmp)
        return res
