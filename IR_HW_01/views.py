from queue import Empty
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import xml.etree.ElementTree as ET
import json

def IR_HW_01_respond(request):

    xmlSentence=readXmlfromFile()
    xmlList=sentence_split(xmlSentence)
    xmlListInclude=[]
    iItem=1
    strXmlTableContent=""

    JsonSentence=readJsonfromFile()
    JsonList=sentence_split(JsonSentence)
    JsonListInclude=[]
    iItem=1
    strJsonTableContent=""
    
    if request.method=='GET':
        if request.GET.get('QueryString')==Empty:
            strXmlTableContent=""
        else:

            strQueryString=request.GET.get('QueryString').strip()
            xmlListInclude=findStringIndex(strQueryString,xmlList)
            for (i, ilist) in enumerate(xmlListInclude, start=1):
            #for ilist in ListInclude:
                if ilist is not Empty:
                    for (j, jlist) in enumerate(ilist, start=1):
                    #for jlist in ilist: 
                        if jlist is not Empty:
                            strXmlTableContent+="<tr><td> "+ str(iItem) +" </td><td> "+ str(i) +" </td><td>"+ str(jlist+1) +"</td><td>" + str(xmlList[i-1]) + "</td></tr>"
                            iItem=iItem+1

            iItem=1

            JsonListInclude=findStringIndex(strQueryString,JsonList)
            for (i, ilist) in enumerate(JsonListInclude, start=1):
            #for ilist in ListInclude:
                if ilist is not Empty:
                    for (j, jlist) in enumerate(ilist, start=1):
                    #for jlist in ilist: 
                        if jlist is not Empty:
                            strJsonTableContent+="<tr><td> "+ str(iItem) +" </td><td> "+ str(i) +" </td><td>"+ str(jlist+1) +"</td><td>" + str(JsonList[i-1]) + "</td></tr>"
                            iItem=iItem+1            


    
    print(xmlList)
    #print(findStringIndex(strQueryString,word_split("How do you turn this on.")))
    print(findStringIndex(strQueryString,xmlList))
    
    print( "========Time:" + str(datetime.now()),strQueryString+"==============")
    return render(request, 'IR_HW_01_respond.html', {
        'current_time': str(datetime.now()),
        'xmltotalLine':str(len(xmlList)),
        'xmltotalWord':str(sum(len(row) for row in xmlList)),
        'xmltableContent': strXmlTableContent,
        'JsontotalLine':str(len(JsonList)),
        'JsontotalWord':str(sum(len(row) for row in JsonList)),
        'JsontableContent': strJsonTableContent,
        'QueryString':strQueryString,
    })


def IR_HW_01_request(request):
 
    xmlSentence=readXmlfromFile()
    xmlList=sentence_split(xmlSentence)
    
    JsonSnetence=readJsonfromFile()
    JsonList=sentence_split(JsonSnetence)

    return render(request,'IR_HW_01_Request.html', {
        'current_time': str(datetime.now()),
        'XmlData':xmlSentence,
        'XmlDataList':xmlList,
        'JsonData':JsonSnetence,
        'JsonDataList':JsonList,
    })



def sentence_split(str_centence):

    str_centence=str_centence.replace('\n      ', '')
    sentence_list_ret = list()

    for s_str in str_centence.split('.'):
        if '?' in s_str:
            for s_Qstr in s_str.split('?'):
                sentence_list_ret.append(word_split(s_Qstr))

        elif '!' in s_str:
            for s_Xstr in s_str.split('?'):
                sentence_list_ret.append(word_split(s_Xstr))

        else:
            sentence_list_ret.append(word_split(s_str))
    
    #return sentence_list_ret
    return list(filter(None, sentence_list_ret))



def word_split(str_centence):
    word_list_ret = list()
    for s_str in str_centence.split(' '):
            word_list_ret.append(s_str)
   
    return list(filter(None, word_list_ret))



def findStringIndex(QueryString,WordList):
   
    IndexList=[]
    for sList in WordList:
        IndexList.append([i for i,d in enumerate(sList) if QueryString.upper() in d.upper() ])
    
    if IndexList ==Empty:
        print( "=====not found======")
    return IndexList



def readXmlfromFile():

    mytree = ET.parse(('.\Files\sample.xml').replace('\\', '/'))
    myroot = mytree.getroot()
    strXmlSentence=""

    for x in myroot.findall('book'):
        sentence =x.find('description').text
        strXmlSentence+=sentence

    return strXmlSentence

def readJsonfromFile():

    with open(('.\Files\sample2.json').replace('\\', '/'), 'r') as json_file:
        JsonRawData = json.load(json_file)
        JsonDescriptionData=""

        for description in JsonRawData['books']:
            JsonDescriptionData+=description['description']
        
    return JsonDescriptionData