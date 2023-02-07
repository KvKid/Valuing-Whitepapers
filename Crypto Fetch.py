
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import base64
from fpdf import FPDF
import random
import logging
logging.basicConfig(filename="logfileerror.log", level=logging.INFO)
import pandas as pd

#Open Scraper window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://golden.com/query/p/WzE4LFtbNywwLCJleGlzdHMiLGZhbHNlLG51bGwsbnVsbF1dLGZhbHNlLFstMSwtMiw3LDU1LDQxLDQwXSxbXV0/")

finaldf = pd.DataFrame({"Name":[], "Links":[]})
k=1
input()
while k<103:
    print("GETTING DATA.")
    links = driver.find_elements(By.XPATH,"//a[@href]") # Get all elements that contain a link
    
    #linkstext contains all elements with a hyperlink
    linkstext = []
    for elem in links:
        linkstext.append(elem.text) # get links from selenium object
    
    #names contains the name of the whitepaper
    #thelinks contaisn the corresponding links associated with the name
    # element i from names corresponds to element i form thelinks
    names = []
    thelinks = []
    i = 0
    #How it works:
    # Take advantage of pattern in which the links appear. We can find contiguous elements where the
    # name of the whitepaper is followed by links to the whitepapers
    while i<len(linkstext):
        elem = linkstext[i]
        if elem[0:5] == "https":
            names.append(linkstext[i-1])
            j = i+1
            while j<len(linkstext):
                if linkstext[j][0:5] == "https":
                    j+=1
                else:
                    break
            thelinks.append(linkstext[i:j])
            i=j
        i+=1
    
    print(i)
    df = pd.DataFrame({"Name":names, "Links": thelinks})
    print(finaldf.tail(3))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scrolls to bottom
    print("CLICK ON NEXT PAGE NOW: " + str(k))
    time.sleep(15)
    
    k+=1
    #Append data collected from current window to our main df
    finaldf = finaldf.append(df)
    finaldf.to_csv()