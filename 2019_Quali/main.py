import numpy as np
import math
import os
import random
from operator import itemgetter

files = os.listdir('Input_Files_2019/')
l = len(files)

for i in range(l):
    files[i] = files[i][:-4]


# class Photos(self,id,direction,tags):
#     self.id = id
#     self.direction = direction
#     self.tags = tags
#
#     self.num_of_tags = len(tags)

def solve(Horizontals, Verticals):
    score = 0
    slides = []
    if len(Verticals) < 2:
        s = Horizontals.pop(0)  # maybe .pop([0])
    elif len(Horizontals) == 0:
        s = Verticals.pop(0)
    else:
        s = Horizontals.pop(0)
    slides = [s]
    if len(Verticals) < 2:
        if len(Horizontals) > 0:
            Horizontals = sorted(Horizontals, key = lambda n: (int(n[1])))
            for i in range(len(Horizontals)-1):
                slides.append(Horizontals[i])
                a_not_b = list(set(slides[i][2:]) - set(slides[i+1][2:]))
                b_not_a = list(set(slides[i][2:]) - set(slides[i+1][2:]))
                a_and_b = list(set(slides[i][2:]) | set(slides[i+1][2:]))
                intersection = list(set(a_and_b) - set(b_not_a) - set(a_not_b))
                comp_score = min(len(a_not_b), len(b_not_a), intersection)
                score += comp_score
                Horizontals.remove(Horizontals[i])

            # for i in range(len(Horizontals)):
            #     a_not_b = list(set(s[2:]) - set(Horizontals[i][2:]))
            #     b_not_a = list(set(Horizontals[i][2:]) - set(s[2:]))
            #     a_and_b = list(set(s[2:]) | set(Horizontals[i][2:]))
            #     intersection = list(set(a_and_b) - set(b_not_a) - set(a_not_b))
            #     if min([len(a_not_b), len(b_not_a), len(intersection)]) > comp_score:
            #         comp_score = min([len(a_not_b), len(b_not_a), len(intersection)])
            #         next_slide_i = Horizontals[i][0]
            #         index = i
            # slides.append(next_slide_i)
            # Horizontals.remove(Horizontals[index])
            # score += comp_score
                #ben bu alt küme işini yapamadım başka bir şey deniyorum


        else:
            if len(Horizontals) == 0:
                #DAMLA
                # Arrange the vertical photos to form slides
                # Sort the verticals by their number of tags
                Verticals = sorted(Verticals, key = lambda n: (int(n[1])))
                # create slides
                vertical_slides = []
                low = 0
                high = len(Verticals) - 1
                while(low < high):
                    vertical_slides.append([Verticals[low][0], Verticals[high][0], Verticals[low][2:], Verticals[high][2:]])
                    #how to store the IDs ??
                    low += 1
                    high -= 1
                    # vertical slides preview --> [id1,id2,[tags1],[tags2]]
                # Vertical slides are ready
                for i in range(len(vertical_slides)-1):
                    # start checking by zero and increment
                    check = vertical_slides[i]
                    temp_score = 0
                    for j in range(i+1,len(vertical_slides)):
                        # check every slide from i to the last item
                        a_not_b = (check[2] + check[3]) - (vertical_slides[j][2] + vertical_slides[j][3])
                        b_not_a = (vertical_slides[j][2] + vertical_slides[j][3]) - (check[2] + check[3])
                        a_and_b = set((check[2] + check[3]).intersection(vertical_slides[j][2] + vertical_slides[j][3]))
                        if(min(len(a_not_b), len(b_not_a), len(a_and_b)) > temp_score):
                            temp_score =  min(len(a_not_b), len(b_not_a), len(a_and_b))
                            next_slide = vertical_slides[j]
                    slides.append(next_slide)
                    score += temp_score
                return score
            if len(Horizontals) > 0:
                # #ATAKAN
                # # Arrange the vertical photos to form slides
                # # Sort the verticals by their number of tags
                # Verticals = sorted(Verticals, itemgetter(1))
                # # create slides
                # vertical_slides = []
                # low = 0
                # high = len(Verticals) - 1
                # while(low < high):
                #     vertical_slides.append([Verticals[low][0], Verticals[high][0], Verticals[low][2:], Verticals[high][2:]])
                #     #how to store the IDs ??
                #     low += 1
                #     high -= 1
                #     # vertical slides preview --> [id1,id2,[tags1],[tags2]]
                # # Vertical slides are ready

                # sort the horizontals by their number of tags
                for i in range(len(Horizontals)):




for i in range(1):
    with open('Input_Files_2019/'+files[i]+'.txt', 'r') as f:

        content = f.readlines()
        N = int(content[0])  # Number of photos
        Horizontals , Verticals = [], []

        for j in range(1, N+1):
            if content[j][0] == 'H':
                Horizontals.append(content[j].split(' ')[1:])
                Horizontals[len(Horizontals)-1].insert(0, j-1)
                Horizontals[len(Horizontals)-1][len(Horizontals[len(Horizontals))-1])-1] = Horizontals[len(Horizontals)-1][len(Horizontals[len(Horizontals)-1])-1][:-1]
            else:
                Verticals.append(content[j].split(' ')[1:])
                Verticals[len(Verticals)-1].insert(0, j-1)
                Verticals[len(Verticals)-1][len(Verticals[len(Verticals)-1])-1] = Verticals[len(Verticals)-1][len(Verticals[len(Verticals)-1])-1][:-1]
        print(Verticals)
        print(Horizontals)


# V = [[1, '2', 'selfie', 'smile'], [2, '2', 'garden', 'selfie']]
# H = [[0, '3', 'cat', 'beach', 'sun'], [3, '2', 'garden', 'cat']]
