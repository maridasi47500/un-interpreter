# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from texttospeech import Texttospeech
from speakerrecording import Speakerrecording
class Myrecording(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.dbSpeaker=Speakerrecording()
        self.cur.execute("""create table if not exists myrecording(
        id integer primary key autoincrement,
        recording text,
            language text,
            event_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from myrecording")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from myrecording where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyeventidlanguage(self,myid,language):
        self.cur.execute("select * from myrecording where event_id = ? and language = ?",(myid,language,))
        row=self.cur.fetchall()
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from myrecording where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        myid=None
        hey=Texttospeech(myhash["recording"])
        hey.script1()
        temps=0
        duration=60
        print(myhash,myhash.keys())
        myid=None
        azerty={}
        try:
          self.cur.execute("insert into myrecording (recording,language,event_id) values (:recording,:language,:event_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)

          azerty["myrecording_id"]=myid
          azerty["notice"]="votre myrecording a été ajouté"
        except Exception as e:
          print("my error"+str(e))
          azerty["myrecording_id"]=""
          azerty["notice"]="il y a eu une erreur quand votre recording a été ajouté"+str(e)
        try:
          while True:
              tempsdebut=temps
              if temps == 0:
                  sometext=hey.get_text_hey(duration)
              else:
                  sometext=hey.get_text_hey(duration,temps)
                  temps+=60
                  tempsfin=temps
                  speaker=self.dbSpeaker.create({"name":"Speaker","text":sometext,"time_debut":tempsdebut,"time_fin":tempsfin,"event_id":myid})
        except Exception as e:
          print("Hey",e)
        return azerty




