# import os
# import random
# import numpy as np
# from collections import Counter
#
# files = os.listdir('Input_Files_2021/')
# l = len(files)
#
# for i in range(l):
#     files[i] = files[i][:-4]
#
# def solve(D,streets,cars):
#     intersections = list(streets[i][1] for i in range(len(streets)))
#     count = Counter(intersections)
#
#
#
#     print(len(count))
#     print(count)
#     for id in count:
#         print(id,count[id])
#
#     return count
#
#
#
# # class street(self,B,E,L):
# #     self.start = B
# #     self.finish = E
# #     self.duration = L
#
#
#
# for i in range(1):
#     with open('Input_Files_2021/'+files[i]+'.txt', 'r') as f:
#
#         content = f.readlines()
#         D, I, S, V, F = [int(x) for x in content[0].split()]
#
#         streets = []
#
#         for ii in range(1,S+1):
#             B, E, street_name, L = content[ii].split(' ')
#             streets.append([B, E, street_name, L.strip()])
#
#
#
#         cars = []
#
#         for jj in range(S+1,S + V + 1):
#              P = content[jj].split()[0]
#              name_street = content[jj].split()[1:]
#              cars.append([P,name_street])
#
#         count = solve(D,streets,cars)
#
# # [['2', '0', 'rue-de-londres', '1\n']
#     with open('Output_files_2021/'+'output_'+files[i]+'.txt', 'w') as w:
#         w.write(str(I) + '\n')
#         for id in count:
#             w.write(str(id) + '\n')
#             w.write(str(count[id]) + '\n')
#             for jj in range(count[id]):




import os
from collections import Counter

files = os.listdir('Input_Files_2021/')
l = len(files)

for i in range(l):
    files[i] = files[i][:-4]


def solve(streets):
    inter_incoming_st = list(streets[i][1] for i in range(len(streets)))
    count = Counter()
    count.update(inter_incoming_st)
    street_lights = []
    for key in count.keys():
        for i in range(len(streets)):
            if streets[i][1] == key:
                street_lights.append([key, streets[i][2])
    return count, street_lights



for i in range(l):
    with open('Input_Files_2021/' + files[i] + '.txt', 'r') as f:

        content = f.readlines()
        D, I, S, V, F = [int(x) for x in content[0].split()]

        streets = []

        for ii in range(1, S + 1):
            B, E, street_name, L = content[ii].split(' ')
            # streets.append([B, E, street_name, L[:-1]])
            streets.append([B, E, street_name, L.strip()])

    count, street_lights = solve(streets)

    with open('Output_Files_2021/'+'output_'+files[i]+'.txt', 'w') as f:
        f.write(str(len(count))+'\n')
        for key, value in count.items():
            f.write(key+'\n')
            f.write(str(value)+'\n')
            for i in range(len(street_lights)):
                if street_lights[i][0] == key:
                    f.write(street_lights[i][1]+ ' 1'+'\n')
