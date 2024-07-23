# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from texttospeech import Texttospeech
from organization import Organization
from speaker import Speaker
class Event(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.dbSpeaker=Speaker()
        self.dbOrganization=Organization()
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists event(
        id integer primary key autoincrement,
        date text,
            heure text,
            organization_id text,
            subtitle text,
            place_id text,
            privpubl text,
            recording text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall_speaker_withid(self,myid):
        self.cur.execute("select event.*,organization.name as organizationname,event.place_id as place from event left join organization on organization.myvalue = event.organization_id group by event.id having event.id = ?", (myid,))

        x=self.cur.fetchone()
        y=dict(x)
        self.cur.execute("select speaker.*,e.heure from speaker left join event e on e.id = speaker.event_id group by speaker.id having speaker.event_id = ? ",(myid,))
        hey=self.cur.fetchall()
        y["language"]="ORIGINAL"
        y["nombre"]="1"
        if hey:
          y["speakers"]=hey
        else:
          y["speakers"]=[]
        return y
    def getall_speaker(self):
        self.cur.execute("select event.*,organization.name as organizationname,event.place_id as place from event left join organization on organization.myvalue = event.organization_id group by event.id")

        row=self.cur.fetchall()
        rows=[]
        for x in row:
            y=dict(x)
            self.cur.execute("select speaker.*,e.heure from speaker left join event e on e.id = speaker.event_id group by speaker.id having speaker.event_id = ? ",(x["id"],))
            hey=self.cur.fetchall()
            if hey:
              y["speakers"]=hey
            else:
              y["speakers"]=[]
            rows.append(y)
        return rows
    def getall(self):
        self.cur.execute("select * from event")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from event where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select event.*,o.name as organization,o.name as organizationname from event left join organization o on o.myvalue = event.id where event.id = ?",(myid,))
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
        print(myhash,myhash.keys())
        myid=None
        hey=Texttospeech(myhash["recording"])
        hey.script1()
        temps=0
        duration=60

        try:
          self.cur.execute("insert into event (recording,date,heure,organization_id,subtitle,place_id,privpubl) values (:recording,:date,:heure,:organization_id,:subtitle,:place_id,:privpubl)",myhash)
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
            speaker=self.dbSpeaker.create({"name":"Speaker","text":sometext,"time_debut":tempsdebut,"time_fin":tempsfin,"event_id":myid})

        except Exception as e:
          print("Hey",e)
        azerty={}
        azerty["event_id"]=myid
        azerty["notice"]="votre event a été ajouté"
        return azerty




