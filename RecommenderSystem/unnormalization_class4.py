import io
import csv
import os
import sys
import math

def my_cmp(a , b):
    if(a[0] == b[0]):
        return a[2] > b[2]
    else:
        return  a[0] > b[0]
def csv_out():
    filewrite=open('C:/Users/pkucc/Desktop/Assignment3.csv','r')
    filereader = csv.reader(filewrite)
    lines = []
    users = []
    k = 0
    for line in filereader:
        lines.insert(k,line)
        users.insert(k,line[0])
        k += 1
    movies = lines[0]
    ans_out = []
    kk = 0
    for i in range(1,len(lines)):#第i个用户
        for j in range(1,len(lines)):#第j个用户
            sum_i = 0
            sum_j = 0
            num = 0
            for k in range(1,len(lines[i])):
                if(lines[i][k] != '' and lines[j][k] != ''):
                    sum_i += float(lines[i][k])
                    sum_j += float(lines[j][k])
                    num += 1
            sum_i /= num
            sum_j /= num
            up = 0
            down1 = 0
            down2 = 0
            for k in range(1,len(lines[i])):
                if(lines[i][k] != '' and lines[j][k] != ''):
                    up += (float(lines[i][k]) - sum_i)*(float(lines[j][k]) - sum_j)
                  #  print(up)
                    down1 += (float(lines[i][k]) - sum_i)**2
                    down2 += (float(lines[j][k]) - sum_j)**2
            ans = up/((math.sqrt(down1))*(math.sqrt(down2)))
            if(users[i] == '89' ):#or users[i] == '89'):
                ans_out.insert(kk,(ans,users[i],users[j]))
    ans_out.sort(reverse = True)
    #89 is 14th


    ans_movie = []
    kk = 0
    for i in range(1,len(lines[3])):
        up = 0
        down = 0.0
        for j in range(1,6):#第j个用户的评分
            co_user = 0
            for k in range(1,len(users)):
                if(users[k] == ans_out[j][2]):
                    co_user = k
            #print(co_user)
            if(lines[co_user][i] != ''):
                up += float(lines[co_user][i])*ans_out[j][0]
                down += ans_out[j][0]
        if(down != 0):
            ans_movie.insert(kk,(up/down,movies[i]))
        else:
            ans_movie.insert(kk,(0,movies[i]))
    ans_movie.sort(reverse=True)
    print(ans_movie)
    print(ans_out)

if __name__ == "__main__":
    csv_out()
