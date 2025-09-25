# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from texttospeech import Texttospeech
from organization import Organization
from convert import Socialmedia

from speaker import Socialloginspeaker
class Mysocialmedia(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.dbSpeaker=Socialloginspeaker()
        self.dbOrganization=Organization()
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists mysocialmedia(
        id integer primary key autoincrement,
        date text,
            title text,
            recording text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall_speaker_withid(self,myid):
        self.cur.execute("select mysocialmedia.* where mysocialmedia.id = ?", (myid,))

        x=self.cur.fetchone()
        y=dict(x)
        self.cur.execute("select socialloginspeaker.*,e.heure from socialloginspeaker left join mysocialmedia e on e.id = speaker.socialloginspeaker_id group by socialloginspeaker.id having socialloginspeaker.mysocialmedia_id = ? ",(myid,))
        hey=self.cur.fetchall()
        y["language"]="ORIGINAL"
        y["nombre"]="1"
        if hey:
          y["speakers"]=hey
        else:
          y["speakers"]=[]
        return y
    def getall_speaker(self):
        self.cur.execute("select * from mysocialmedia")

        row=self.cur.fetchall()
        rows=[]
        for x in row:
            y=dict(x)
            self.cur.execute("select socialloginspeaker.* from socialloginspeaker left join mysocialmedia e on e.id = socialloginspeaker.mysocialmedia_id group by socialloginspeaker.id having socialloginspeaker.mysocialmedia_id = ? ",(x["id"],))
            hey=self.cur.fetchall()
            if hey:
              y["speakers"]=hey
            else:
              y["speakers"]=[]
            rows.append(y)
        return rows

    def getall(self):
        self.cur.execute("select * from mysocialmedia")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from mysocialmedia where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select mysocialmedia.* where mysocialmedia.id = ?",(myid,))
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
        if myhash['recording'].endswith('m4a'):
          print("goodbye678")
          hey=Socialmedia(myhash['recording']).ok()
          myhash['recording']=myhash['recording'].replace('.m4a','.mp3')

        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        hey=Texttospeech(myhash["recording"])
        hey.script1()
        temps=0
        duration=60

        try:
          self.cur.execute("insert into mysocialmedia (recording,title) values (:recording,:title)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        try:
          while True:
            tempsdebut=temps
            if temps == 0:
              sometext=hey.get_text_hey(duration)
            else:
              sometext=hey.get_text_hey(duration,temps)
            temps+=60
            tempsfin=temps
            speaker=self.dbSpeaker.create({"name":"Speaker","text":sometext,"time_debut":tempsdebut,"time_fin":tempsfin,"mysocialmedia_id":myid})

        except Exception as e:
          print("Hey",e)
        azerty={}
        azerty["mysocialmedia_id"]=myid
        azerty["notice"]="votre mysocialmedia a été ajouté"
        return azerty




