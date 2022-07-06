import fuzzification
import numpy as np


def defuzzify(sick1_pow, sick2_pow, sick3_pow, sick4_pow, healthy_pow):
    points = np.linspace(0, 4, 5000)
    answers = []
    for p in points:
        out = fuzzification.output_mem(p)
        sick1 = out[0]
        sick2 = out[1]
        sick3 = out[2]
        sick4 = out[3]
        healthy = out[4]

        if sick1 > sick1_pow:
            sick1 = sick1_pow
        if sick2 > sick2_pow:
            sick2 = sick2_pow
        if sick3 > sick3_pow:
            sick3 = sick3_pow
        if sick4 > sick4_pow:
            sick4 = sick4_pow
        if healthy > healthy_pow:
            healthy = healthy_pow
        ans = max(sick1, sick2, sick3, sick4, healthy)
        answers.append(ans)

    dx = points[1] - points[0]
    sum1 = 0
    sum2 = 0
    for i in range(len(points)):
        sum1 += (answers[i] * points[i] * dx)
        sum2 += (answers[i] * dx)
    if sum2 == 0:
        return 0
    force = sum1/sum2
    return force
