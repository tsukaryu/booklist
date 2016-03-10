# -*- coding: utf-8 -*-
#読みたい本リストを作成
import sqlite3

def plist(booklist):
    print'\n読みたい本リスト\n'
    for i,v in enumerate(booklist):
        print i,v[0]+'「'+v[1]+'」'
def bksr(mi,mo):
    #\マークをバックスラッシュに変換してくれる
    for i in range(len(mo)):
        if mo[i]=='\\':
            mi=mi+'/'
            #print mi
        else:
            mi=mi+mo[i]
            #print mi
    return mi
def makedb():
    #テーブル作成
    connection = sqlite3.connect('booklist.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE booklist (id INTEGER PRIMARY KEY AUTOINCREMENT,
    foo TEXT(100) NOT NULL,
    bar TEXT(100) NOT NULL);
    ''')
    cursor.close()

def InsertList():
    #テーブルに挿入
    connection = sqlite3.connect('booklist.db')
    cursor = connection.cursor()
    sql = "INSERT INTO booklist(foo,bar) VALUES(?,?);"
    fact = [u"セルバンテス",u"ドン・キホーテ"]
    cursor.execute(sql,fact)
    connection.commit()
    cursor.close()
def SelectListALL():
    #テーブルから読み込み
    connection = sqlite3.connect('booklist.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM booklist;"
    cc = cursor.execute(sql)
    da = cc.fetchall()
    for i in da:
        print("%d"%i[0])+' '+("%s"%i[1].encode('utf-8'))+'「'+("%s"%i[2].encode('utf-8'))+'」' #foo
    cursor.close()
#-----------------------------ここからmainのとこ------------------------------------#

if __name__ == "__main__":

    print'読みたい本リスト閲覧:1\n本の登録:2\nバックスラッシュを変換:3\nデータベースから呼び出し:4\n'
    print'数字を選択'
    num=raw_input('-->')
#    print'お前は「'+num+'」を選んだな！'
#    print type(num)

booklist=[['ガルシア・マルケス','百年の孤独'],
          ['ジャン・ポール・サルトル','嘔吐'],
          ['セルバンテス','ドン・キホーテ']]

if num=='1':
    #makedb()
    #InsertList()
    SelectListALL()
elif num=='2':
    print'読みたい本リスト'
    book=[]
    book.append(raw_input('作者-->'))
    book.append(raw_input('題名-->'))
    booklist.append(book)
    plist(booklist)

elif num=='3':
    #C:\Users\1X12C024\Desktop\AgentSimulation\test1-1\booklist
    #C:/Users/1X12C024/Desktop/AgentSimulation/test1-1/booklist
    mo=raw_input('-->')
    mi=''
    print bksr(mi, mo)

else:
    print'指定した数字をうちこめオマンコ野郎！'