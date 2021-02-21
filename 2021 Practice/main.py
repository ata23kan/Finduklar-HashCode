# Team Finduklar
# Google Hash Code 2021 Practice Round: Even More Pizza

import os
import random
import math
import heapq


files = os.listdir('Input_Files/')
l = len(files)

for i in range(l):
    files[i] = files[i][:-3]

# for file in files:
#     print(file)
def solve(M,T2,T3,T4,num_of_ing,ingredients):
    delivered, score = 0, 0

    tt, ttt, tttt = [], [], []
    # While delivered pizzas are less than the total number
    while delivered < M:

        # Delivering pizzas to 2-member teams
        if delivered + 2 < M and T2 > 0:
            T2 -= 1
            max_index = num_of_ing.index(max(num_of_ing))
            min_index = num_of_ing.index(min(num_of_ing))
            tt.append([max_index,min_index])
            # ****Check if math.NaN does not work****
            num_of_ing[max_index] = math.nan
            num_of_ing[min_index] = math.nan
            ss = len(set(ingredients[max_index] + ingredients[min_index]))
            delivered += 2

        elif delivered + 3 < M and T3 > 0:
            T3 -= 1
            max_index = num_of_ing.index(max(num_of_ing))
            num_of_ing[max_index] = math.nan

            min1_index = num_of_ing.index(min(num_of_ing))
            num_of_ing[min1_index] = math.nan

            min2_index = num_of_ing.index(min(num_of_ing))
            num_of_ing[min2_index] = math.nan
            ttt.append([max_index,min1_index, min2_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index]+ingredients[min1_index]+ingredients[min2_index]))
            delivered += 3

        elif delivered + 4 < M and T4 > 0:
            T4 -= 1
            max_index = num_of_ing.index(max(num_of_ing))
            num_of_ing[max_index] = math.nan

            min1_index = num_of_ing.index(min(num_of_ing))
            num_of_ing[min1_index] = math.nan

            min2_index = num_of_ing.index(min(num_of_ing))
            num_of_ing[min2_index] = math.nan

            min3_index = num_of_ing.index(min(num_of_ing))
            num_of_ing[min3_index] = math.nan

            tttt.append([max_index, min1_index, min2_index, min3_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min1_index] + ingredients[min2_index] + ingredients[min3_index]))
            delivered += 4
        else:
            break

        score += ss**2

    return score


for i in range(l):

    with open('Input_Files/'+files[i]+'.in', 'r') as f:

        content = f.readlines()
        ingredients = []
        numbers_of_ingredients = []
        M, T2, T3, T4 = [int(x) for x in content[0].split()]
        for j in range(1,M+1):

            ingredient = content[j].split()[1:]
            ingredients.append((ingredient))
            number_of_ingredients = content[j].split()[0]
            numbers_of_ingredients.append(int(number_of_ingredients))

        # print(ingredients, numbers_of_ingredients)

        score = solve(M,T2,T3,T4,numbers_of_ingredients,ingredients)

        print(score)

# Results:
# 25
# 6864
# 179958812
# 9542
# 48025
