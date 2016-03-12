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

def InsertList(name,title):
    #テーブルに挿入
    try:
        connection = sqlite3.connect('booklist.db')
        cursor = connection.cursor()
        sql = "INSERT INTO booklist(foo,bar) VALUES(?,?);"
        fact = [name.decode('utf-8'),title.decode('utf-8')]
        cursor.execute(sql,fact)
        connection.commit()
        cursor.close()
    except:
        print'挿入できないエラーだにょ～'
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
def DeleteList(dlt):
    connection = sqlite3.connect('booklist.db')
    cursor = connection.cursor()
    sql = "DELETE from booklist where id=?;"
    try:
        cursor.execute(sql,[dlt,])
        connection.commit()
        cursor.close()
    except:
        print'削除できないエラーだにょ～'
    SelectListALL()

#-----------------------------ここからmainのとこ------------------------------------#

if __name__ == "__main__":
    while True:
        print'読みたい本リスト閲覧:1\n本の登録:2\n本の削除:3\nバックスラッシュを変換:4\n終了:10\n'
        print'数字を選択'
        num=raw_input('-->')
        if num=='1':
            #makedb()
            SelectListALL()
        elif num=='2':
            while True:
                end=1
                print'読みたい本リスト'
                while True:
                    name=raw_input('作者-->')
                    title=raw_input('題名-->')
                    end=raw_input('決定:1 変更:2-->')
                    if end=='1':break
                #print type(name)
                InsertList(name,title)
                SelectListALL()
                end =raw_input('続けて入力？:1\n終わる:2\n-->')
                if end=='2':break

        elif num=='3':
            SelectListALL()
            dlt=raw_input('削除する本の番号-->')
            DeleteList(dlt)
        elif num=='4':
            #C:\Users\1X12C024\Desktop\AgentSimulation\test1-1\booklist
            #C:/Users/1X12C024/Desktop/AgentSimulation/test1-1/booklist
            mo=raw_input('-->')
            mi=''
            print bksr(mi, mo)
        elif num=='10':break
        else:
            print'指定した数字をうちこめ！'