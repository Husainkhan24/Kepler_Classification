import requests
from bs4 import BeautifulSoup
from googlesearch import search
from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/actor",methods=['POST'])
def actor_url():
    val=request.form['ACTOR_NAME']
    
    for i in search(val, stop=10):
        if i.endswith("_filmography"):
                r=requests.get(i)
                bsoup=BeautifulSoup(r.text,"html.parser")

    

    
    
    
    bsoup.tittle

    res2=bsoup.find_all('a',href=True)
    results=bsoup.find_all('table',attrs={'class':"wikitable sortable plainrowheaders"})
    len(results)


    if len(results)==0:
        results=bsoup.find_all('table',attrs={'class':"wikitable sortable plainrowheaders"})
        results
    ##class="wikitable sortable plainrowheaders jquery-tablesorter
    else:
        results=bsoup.find_all('table',attrs={'class':"wikitable plainrowheaders sortable"})
        results
    ##class="wikitable plainrowheaders sortable jquery-tablesorter"
        results

    results=bsoup.find_all('table',attrs={'class':"wikitable plainrowheaders sortable"})
    results
    
    lost=[]
    for i in results:
        k=i.find_all("i")
        for j in k:
            lost.append(j.text)
    
    
    desc=tuple(reversed(lost))
    desc


    return render_template("res.html",desc=desc)
if __name__ == '__main__':
    app.run(debug = True) 