#!/usr/bin/env python3

import sys
import random
import math
import time
#import csv
import datetime
import pytz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import json
import cgi
import subprocess as un

#f = open("time.csv",'a')
#writer = csv.writer(f,lineterminator='\n',delimiter=',')
try:
    data = json.loads(open("kekka.json").read())
except:
    print("セットアップ中・・・")
    un.call("setup.py")
    data = json.loads(open("kekka.json").read())

maru = [int(data["0"]["seikai"]),int(data["1"]["seikai"]),int(data["2"]["seikai"]),int(data["3"]["seikai"])]
batsu = [int(data["0"]["machigai"]),int(data["1"]["machigai"]),int(data["2"]["machigai"]),int(data["3"]["machigai"])]
marukai = 0
batukai = 0

for i in maru:
    marukai += int(i)

for j in batsu:
        batukai += int(j)
def monsak(j):
    sisoku = random.randint(0,3)
    if sisoku == 0:
        a = random.randint(1,100)
        b = random.randint(1,100)
        awn = a + b
    if sisoku == 1:
        a = random.randint(50,200)
        b = random.randint(10,a-1)
        awn = a - b
    if sisoku == 2:
        a = random.randint(2,20)
        b = random.randint(2,20)
        awn = a * b
    if sisoku == 3:
        a = random.choice(j)
        m = []
        for z in range(1,200):
            if a % z == 0:
                m += [z]

        b = random.choice(m)
        awn = a / b
    return sisoku,a,b,awn


def keisans():
    j = []
    kekkas = []
    seikai = 0
    try:
      num = int(input("回数を入力してください:"))
    except:
        
        print("整数を入力してください。")
        sys.exit()
    if num < 1 :
        print("回数は1以上です。")
        sys.exit()
    sis = ["+","-","×","÷"]
    for i in range(200):
        if i % 2 == 0:
            j += [i]

    t = time.time()

    for i in range(num):
        kkkkk = []
        sisoku,a,b,awn = monsak(j)
        tss = time.time()
        kkkkk += ["問題" + str(i + 1) +  ":" + str(a) + sis[sisoku] + str(b),"四則演算:" + str(sisoku)]
        try:
            awnser = int(input(str(i + 1) + "問目：" + str(a) + sis[sisoku] + str(b) + "= ?"))
        except KeyboardInterrupt:
            print("終了します")
            sys.exit()
        except:
            awnser = -1

        kkkkk += ["答え: " + str(awn),"自分の答え：" + str(awnser)]
        jikann = time.time() - tss
        kkkkk += ["かかった時間:" + str(jikann)]
         
        if awnser == awn:
            print("正解！")
            seikai += 1
            kkkkk += ["正誤：○",'\n']
            data[str(sisoku)]["seikai"] += 1

        else:
            print("間違い..." + "正解は" + str(awn))
            kkkkk += ["正誤：×",'\n']
            data[str(sisoku)]["machigai"] += 1

        kekkas += kkkkk

    print(str(seikai) + "/" + str(num))
    print("正解率" + str(math.ceil((seikai / num) * 10000) / 100) + "％")
    ts = time.time() - t
    print(str(math.ceil((ts * 100)) / 100) + "秒かかりました。")
    
    print("ファイルの書き込みをします")
    # now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    # z = f'{now:%Y年%m月%d日 %H時%M分%S秒}'
    # wri = ["日付" + str(z),"かかった時間:" + str(math.ceil(ts * 100) / 100),"正解率:" + str((math.ceil((seikai / num) * 10000) / 100)) + "％"
    # ,"正解数" + str(seikai) + "/" + str(num)]
    #writer.writerow(wri)
    #writer.writerow(["問題"])
    #writer.writerow(kekkas)
    fw = open("kekka.json","w")
    json.dump(data,fw,indent=2)
    print("書き込みが終了しました。")

def kaiseki():
    # 3 7 10 13...と解析するところは移動する(間は4 3 3 ...)
    if marukai == 0 and batukai == 0:
        print("履歴がありません。")
    else:
        try:
            print("足し算の時の正解率は" + str(int(maru[0]) / (int(maru[0]) + int(batsu[0])) * 100) + "%で、結果は" + str(int(maru[0])) + "/" + str(int(maru[0]) + int(batsu[0])))
        except:
            print("足し算の問題は出題されていません。")
        try:
            print("引き算の時の正解率は" + str(int(maru[1]) / (int(maru[1]) + int(batsu[1])) * 100) + "%で、結果は" + str(int(maru[1])) + "/" + str(int(maru[1]) + int(batsu[1])))
        except:
            print("引き算の問題は出題されていません。")
        try:
            print("掛け算の時の正解率は" + str(int(maru[2]) / (int(maru[2]) + int(batsu[2])) * 100) + "%で、結果は" + str(int(maru[2])) + "/" + str(int(maru[2]) + int(batsu[2])))
        except:
            print("掛け算の問題は出題されていません。")
        try:
            print("割り算の時の正解率は" + str(int(maru[3]) / (int(maru[3]) + int(batsu[3])) * 100) + "%で、結果は" + str(int(maru[3])) + "/" + str(int(maru[3]) + int(batsu[3])))
        except:
            print("割り算の問題は出題されていません。")
        try:
            print("全体の正解率は、" + str(marukai / (marukai + batukai) * 100) + "%で、結果は、" + str(marukai) + "/" + str(marukai + batukai))
        except:
            print("全体の正解率は、100%で、結果は、" + str(marukai) + "/" + str(marukai))

def chart():
    # print(type(maru[0]))
    # sys.exit()
    if marukai > 0:
        plt.pie(maru,labels=["plus","minus","mul","div"],counterclock=False,startangle=90,colors=["yellow","gold","slateblue","lightcoral"])
        plt.legend(loc = "upper right")
        plt.savefig("maru.jpg")
    if batukai > 0:
        plt.pie(batsu,labels=["plus","minus","mul","div"],counterclock=False,startangle=90,colors=["yellow","gold","slateblue","lightcoral"])
        plt.savefig("batsu.jpg")
    print("ファイルへ書き込みをしました。（maru.jpg, batsu.jpg）")

def help():
    print("   \     |       /-   -\           ")
    print("         |        \   /            ")
    print(" -----   |      |------|           ")
    print("         |      |      |           ")
    print("  ---    |      |------|           ")
    print("      -------   |      |           ")
    print("  ---    |      |------|           ")
    print("         |      |      |           ")
    print("         |      |------|           ")
    print("  |-|    |        /  \             ")
    print("  | |    |    -----------          ")
    print("  |-|    |     /      \            ")
    print("                                   ")
    print("                                   ")
    print("keisan.py                          ")
    print("t  計算のテスト この場合はnumを指定")
    print("k  解析                            ")
    print("c 円グラフを作成                   ")
    print("h ヘルプ                           ")
    print("s 履歴削除                         ")
    print("e 終わる                           ")

try:
    while 1 == 1:
      i = input("オプションを入力してください( h でヘルプ):")
      if i == "t":
          keisans()
      elif i == "k":
          kaiseki()
      elif i == "c":
          chart()
      elif i == "h":
        help()
      elif i == "s":
        print("初期化しています。")
        un.call("setup.py")
      elif i == "e":
          print("")
          print("終了します。")
          break
      else:
        print("引数が正しくありません")
except KeyboardInterrupt:
    print("")
    print("終了します。")
    sys.exit()
except IndexError:
    print("引数が足りません")
        
