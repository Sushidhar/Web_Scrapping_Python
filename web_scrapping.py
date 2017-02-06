# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 23:32:21 2016

@author: Selva
"""
import os
from bs4 import BeautifulSoup
from datetime import datetime
import pandas
import matplotlib.pyplot as plt
import json
import urllib
import requests
import time


class Pokemon_Scrapping:
    def __init__(self,initial_path):
        'Constructor'
        self.dir_path=initial_path    
        
    def open_directories(self):
        'Method to iterate through directories'
        
        ios_data=dict()
        for file_name in range(len(os.listdir(self.dir_path))):
            if (datetime.strptime(os.listdir(self.dir_path)[file_name],'%Y-%m-%d') >=datetime.strptime('2016-07-21','%Y-%m-%d')) & (datetime.strptime(os.listdir(self.dir_path)[file_name],'%Y-%m-%d')<datetime.strptime('2016-10-31','%Y-%m-%d')):
                
                print("Processing directory #"+ str(file_name+1)+ " of "+str(len(os.listdir(self.dir_path)))+" ....\nProcessing Files...")
                for html_file_name in os.listdir(self.dir_path+'\\'+os.listdir(self.dir_path)[file_name]):
                    #print os.listdir(self.dir_path)[file_name]
                    if "ios" in html_file_name:
                        data=dict()
                        
                        #print html_file_name
                        time=html_file_name.split("_")
                        date_time=os.listdir(self.dir_path)[file_name]+"_"+time[0]+"_"+time[1]
                        html_page=open(self.dir_path+"\\"+os.listdir(self.dir_path)[file_name]+"\\"+html_file_name)
                        #print self.dir_path+"\\"+os.listdir(self.dir_path)[file_name]+"\\"+html_file_name
                        soup=BeautifulSoup(html_page,'lxml')
                
                        try:
                            data['total_rating']=soup.find_all('span',{'class':'rating-count'})[0].text.split()[0].encode('utf-8')
                        except:
                            data['total_rating']=''
                        try:
                            data['total_rating_current_version']=soup.find_all('span',{'class':'rating-count'})[1].text.split()[0].encode('utf-8')
                        except:
                            data['total_rating_current_version']=''
                        try:
                            data['file_size']=soup.find_all('div',{'id':'left-stack'})[0].find_all('ul')[0].find_all('li')[4].text.split()[1].strip().encode('utf-8')
                        except:
                            data['file_size']=''
                        try:    
                            data['version']=soup.find_all('div',{'id':'left-stack'})[0].find_all('ul')[0].find_all('li')[3].text.split()[1].strip().encode('utf-8')
                        except:
                            data['version']=''
                        try:
                            data['description']=soup.find('p',{'itemprop':'description'}).text.encode('utf-8')
                        except:
                            data['description']=''
                    
                            
                            
                        ios_data[date_time]=data
                        
        with open("pokemon_ios.json",'a') as file_object:
            json.dump(ios_data,file_object,indent=4)       
#        df=pandas.DataFrame.from_dict(ios_data, orient='columns')
#        for date in df['date_time']:
#            df['Date']=datetime.strptime(date, '%Y-%m-%d_%H_%M')
#            print df['Date']
#            df_date_filtered=df[(df['Date']>=datetime.strptime('2016-07-21','%Y-%m-%d')) & (df['Date']<datetime.strptime('2016-10-31','%Y-%m-%d'))]
#            print df_date_filtered
#            graph_df=df[['Date','Current Rating']]
#            print graph_df.columns
#            graph_df.plot(kind='bar')

            #for data in ios_data:
#            plot_data=dict()
#            current_ratings=[]
#            print ios_data[data]
#            datetime_object = datetime.strptime(data, '%Y-%m-%d_%H_%M')
#            date_formated= datetime_object.strftime('%Y-%m-%d')
#            
#            if (datetime.strptime(date_formated,'%Y-%m-%d') >=datetime.strptime('2016-07-21','%Y-%m-%d')) & (datetime.strptime(date_formated,'%Y-%m-%d')<datetime.strptime('2016-10-31','%Y-%m-%d')):
#                if(date_formated in plot_data):
#                    plot_data[date_formated].append(ios_data[data]['total_rating_current_version'])
#                    print plot_data
#                else:
#                    rating_data=[]
#                    rating_data.append(ios_data[data]['total_rating_current_version'])
#                    plot_data[date_formated]=rating_data
#        print plot_data
#        #plt.bar(plot_data.keys,plot_data.values)
#        #plt.xticks(range(len(plot_data)), list(plot_data.keys()))
    
    def plot_graph(self):
        date=[]
        current_ratings=[]
        all_ratings=[]
        file_size=[]
        
        with open("pokemon_ios.json","r") as file_object:
            data=json.load(file_object)
        for datum in data:
            date.append(datetime.strptime(datum, '%Y-%m-%d_%H_%M').strftime('%Y-%m-%d'))
            current_ratings.append(data[datum]["total_rating_current_version"].encode('utf-8'))
            all_ratings.append(data[datum]["total_rating"].encode('utf-8'))
            file_size.append(data[datum]["file_size"].encode('utf-8'))
            
        #self.plt_grp(date,current_ratings,'Current Ratings')
        #self.plt_grp(date,all_ratings,'All Ratings')
        #self.plt_grp(date,file_size,'File Size')
        
#        for x in current_ratings:
#            if x=='':
#                x=0
#            xaxis.append(int(x))
#        #print xaxis
#        plt.xticks(range(len(date)),date)
#        plt.bar(date,xaxis)
#        plt.show()
#   
    def scrap_ios_img(self):
        #ios_data=dict()
        for file_name in range(len(os.listdir(self.dir_path))):
            if (datetime.strptime(os.listdir(self.dir_path)[file_name],'%Y-%m-%d') >=datetime.strptime('2016-08-02','%Y-%m-%d')) & (datetime.strptime(os.listdir(self.dir_path)[file_name],'%Y-%m-%d')<=datetime.strptime('2016-10-31','%Y-%m-%d')):
                
                print("Processing directory #"+ str(file_name+1)+ " of "+str(len(os.listdir(self.dir_path)))+" ....\nProcessing Files...")
                for html_file_name in os.listdir(self.dir_path+'\\'+os.listdir(self.dir_path)[file_name]):
                    #print os.listdir(self.dir_path)[file_name]
                    if "ios" in html_file_name:
                        #data=dict() 
                        
                        #print html_file_name
                        #time=html_file_name.split("_")
                        #date_time=os.listdir(self.dir_path)[file_name]+"_"+time[0]+"_"+time[1]
                        html_page=open(self.dir_path+"\\"+os.listdir(self.dir_path)[file_name]+"\\"+html_file_name)
                        #print self.dir_path+"\\"+os.listdir(self.dir_path)[file_name]+"\\"+html_file_name
                        
                        soup=BeautifulSoup(html_page,'lxml')
                        
                        for image in soup.find_all('img',{'itemprop':'screenshot'}):
                            filename = image['alt'].replace(' ','')
                            image_name='Images_ios\\'+os.listdir(self.dir_path)[file_name]+"_"+html_file_name+"_"+filename+'.jpeg'
                            print("Processing "+image_name)
                            if(os.path.isfile(image_name)!=True):
                                with open(image_name,'wb') as img_file:
                                    img_file.write(requests.get(image['src']).content)
                                    time.sleep(1)
                                    

    def scrap_android_img(self):
        #ios_data=dict()
        for file_name in range(len(os.listdir(self.dir_path))):
            if (datetime.strptime(os.listdir(self.dir_path)[file_name],'%Y-%m-%d') >=datetime.strptime('2016-07-30','%Y-%m-%d')) & (datetime.strptime(os.listdir(self.dir_path)[file_name],'%Y-%m-%d')<=datetime.strptime('2016-10-31','%Y-%m-%d')):
                
                print("Processing directory #"+ str(file_name+1)+ " of "+str(len(os.listdir(self.dir_path)))+" ....\nProcessing Files...")
                for html_file_name in os.listdir(self.dir_path+'\\'+os.listdir(self.dir_path)[file_name]):
                    #print os.listdir(self.dir_path)[file_name]
                    if "ios" in html_file_name:
                        #data=dict()
                        
                        #print html_file_name
                        #time=html_file_name.split("_")
                        #date_time=os.listdir(self.dir_path)[file_name]+"_"+time[0]+"_"+time[1]
                        html_page=open(self.dir_path+"\\"+os.listdir(self.dir_path)[file_name]+"\\"+html_file_name)
                        #print self.dir_path+"\\"+os.listdir(self.dir_path)[file_name]+"\\"+html_file_name
                    
                        soup=BeautifulSoup(html_page,'lxml')
                        
                        for image in soup.find_all('img',{'itemprop':'screenshot'}):
                            filename = image['data-expand-to'].replace('-','')
                            image_name='Images_android\\'+os.listdir(self.dir_path)[file_name]+"_"+html_file_name+"_"+filename+'.jpeg'
                            print("Processing "+image_name)
                            if(os.path.isfile(image_name)!=True):
                                with open(image_name,'wb') as img_file:
                                    img_file.write(requests.get(image['src']).content)
                                    time.sleep(1)

    def plt_grp(self,xlist,ylist,name):
        yaxis=[]
        for x in ylist:
            if x=='':
                x=0
            yaxis.append(int(x))
        df=pandas.DataFrame({'Date':xlist,name:yaxis})
        
        df=df[df[name]!=0]
        pandas.to_datetime(df['Date'],format="%Y-%m-%d")
        
        df=df.sort_values(['Date'])
        padding=min(df[name])-(max(df[name])-min(df[name]))%10
        df.plot(x='Date',figsize=(20,10),ylim=(min(df[name])-padding,max(df[name])+padding))
if __name__=='__main__':
    class_object1=Pokemon_Scrapping("pokemon_5378/data")
    #class_object1.open_directories()
    #class_object1.plot_graph()
    class_object1.scrap_ios_img()
    #class_object1.scrap_android_img()