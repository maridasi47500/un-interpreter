# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Speakerrecording(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists speakerrecording(
        id integer primary key autoincrement,
        myrecording_id text,
            name text,
            text text,
            time_debut text,
            time_fin text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from speakerrecording")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from speakerrecording where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyrecordingid(self,myid):
        self.cur.execute("select speakerrecording.*,myrecording.event_id,event.heure from speakerrecording left join myrecording on myrecording.id = speakerrecording.myrecording_id left join event on event.id = myrecording.event_id group by speakerrecording.id having speakerrecording.myrecording_id = ?",(myid,))
        job=self.cur.fetchall()
        return job
    def getbyid(self,myid):
        self.cur.execute("select * from speakerrecording where id = ?",(myid,))
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
        try:
          self.cur.execute("insert into speakerrecording (myrecording_id,name,text,time_debut,time_fin) values (:myrecording_id,:name,:text,:time_debut,:time_fin)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["speakerrecording_id"]=myid
        azerty["notice"]="votre speakerrecording a été ajouté"
        return azerty




