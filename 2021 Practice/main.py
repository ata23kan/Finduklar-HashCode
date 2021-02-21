# Team Finduklar
# Google Hash Code 2021 Practice Round: Even More Pizza

import os
import random
import math
import heapq
import numpy as np


files = os.listdir('Input_Files/')
l = len(files)

for i in range(l):
    files[i] = files[i][:-3]


def solve(M,T2,T3,T4,num_of_ing,ingredients):
    delivered, score = 0, 0

    tt, ttt, tttt = [], [], []
    # While delivered pizzas are less than the total number
    while delivered < M:

        # Delivering pizzas to 2-member teams
        if delivered + 2 <= M and T2 > 0:
            T2 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min_index] = np.nan

            tt.append([max_index,min_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min_index]))
            delivered += 2

        # Delivering pizzas to 3-member teams
        elif delivered + 3 <= M and T3 > 0:
            T3 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min1_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min1_index] = np.nan

            min2_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min2_index] = np.nan
            ttt.append([max_index,min1_index, min2_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index]+ingredients[min1_index]+ingredients[min2_index]))
            delivered += 3

        # Delivering pizzas to 4-member teams
        elif delivered + 4 <=M and T4 > 0:
            T4 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min1_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min1_index] = np.nan

            min2_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min2_index] = np.nan

            min3_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min3_index] = np.nan

            tttt.append([max_index, min1_index, min2_index, min3_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min1_index] + ingredients[min2_index] + ingredients[min3_index]))
            delivered += 4
        else:
            break

        score += ss**2

    return score, tt, ttt, tttt

def solve2(M,T2,T3,T4,num_of_ing,ingredients):
    delivered, score = 0, 0

    tt, ttt, tttt = [], [], []
    # While delivered pizzas are less than the total number
    while delivered < M:

        # Delivering pizzas to 2-member teams
        if delivered + 2 <= M and T2 > 0:
            T2 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min_index] = np.nan

            tt.append([max_index,min_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min_index]))
            delivered += 2

        # Delivering pizzas to 3-member teams
        elif delivered + 3 <= M and T3 > 0:
            T3 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min1_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min1_index] = np.nan

            min2_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min2_index] = np.nan
            ttt.append([max_index,min1_index, min2_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index]+ingredients[min1_index]+ingredients[min2_index]))
            delivered += 3

        # Delivering pizzas to 4-member teams
        elif delivered + 4 <=M and T4 > 0:
            T4 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min1_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min1_index] = np.nan

            min2_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min2_index] = np.nan

            min3_index = num_of_ing.index(np.nanmin(num_of_ing))
            num_of_ing[min3_index] = np.nan

            tttt.append([max_index, min1_index, min2_index, min3_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min1_index] + ingredients[min2_index] + ingredients[min3_index]))
            delivered += 4
        else:
            break

        score += ss**2

    return score, tt, ttt, tttt

def solve3(M,T2,T3,T4,num_of_ing,ingredients):
    delivered, score = 0, 0

    tt, ttt, tttt = [], [], []
    # While delivered pizzas are less than the total number
    while delivered < M:

        # Delivering pizzas to 2-member teams
        if delivered + 2 <= M and T2 > 0:
            T2 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min_index] = np.nan

            tt.append([max_index,min_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min_index]))
            delivered += 2

        # Delivering pizzas to 3-member teams
        elif delivered + 3 <= M and T3 > 0:
            T3 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min1_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min1_index] = np.nan

            min2_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min2_index] = np.nan
            ttt.append([max_index,min1_index, min2_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index]+ingredients[min1_index]+ingredients[min2_index]))
            delivered += 3

        # Delivering pizzas to 4-member teams
        elif delivered + 4 <=M and T4 > 0:
            T4 -= 1
            max_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[max_index] = np.nan

            min1_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min1_index] = np.nan

            min2_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min2_index] = np.nan

            min3_index = num_of_ing.index(np.nanmax(num_of_ing))
            num_of_ing[min3_index] = np.nan

            tttt.append([max_index, min1_index, min2_index, min3_index])
            # ****Check if math.NaN does not work****

            ss = len(set(ingredients[max_index] + ingredients[min1_index] + ingredients[min2_index] + ingredients[min3_index]))
            delivered += 4
        else:
            break

        score += ss**2

    return score, tt, ttt, tttt

for i in range(4):
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
        print("\nCalculating..")
        score,tt, ttt,tttt = solve3(M,T2,T3,T4,numbers_of_ingredients,ingredients)

        print(score)

# Results for solve :
# 50
# 8327
# 179958812
# 1806570
# 48025 ????

# Results for solve2 :
# 61
# 7174
# 363996296

# Results for solve3 :
# 61
# 7018
# 477546981
