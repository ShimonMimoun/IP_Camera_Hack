import requests,re,os
import time
import sys

print("""
      
      
\033[1;31m******************************************************************************************************************************
\033[1;31m******************************************************************************************************************************
\033[1;31m******************************************************************************************************************************
\033[1;31m******************************************************************************************************************************
\033[1;31m****************************************\033[1;37m       Hack IP Camera:                      V1.0.Beta\033[1;31m ********************************
\033[1;31m****************************************\033[1;37m                       By Shimon Mimoun       \033[1;31m        ********************************
\033[1;31m****************************************\033[1;37m                                   && Omer Paz\033[1;31m        ********************************
\033[1;31m******************************************************************************************************************************
\033[1;31m******************************************************************************************************************************
\033[1;31m******************************************************************************************************************************
\033[1;31m******************************************************************************************************************************


\033[1;37m                                                         Enter Number :        
\033[1;37mPRESS 1 --> \033[1;31mUnited States   
            
\033[1;37mPRESS 2 --> \033[1;31mFrench                      

\033[1;37mPRESS 3 --> \033[1;31mIsrael                      

\033[1;37mPRESS 4 --> \033[1;31mIran  
                      
\033[1;37mPRESS 5 --> \033[1;31mArgentina              

        

""")
 
try:                                                               
    num = int(input("\033[1;37m                                                         INPUT : "))
    printcolor="\n \033[0;37;41mTarget : \033[1;32;40m"
    
    if num == 1:
        print("United States\n")
        print(printcolor)	
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,3000):
			
                url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
           
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;32m",hasil)
                 
                     count += 1
        except:
            print (" ")
    elif num == 2:		
        print("French\n")
        print(printcolor)	
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,500):
			
                url = ("https://www.insecam.org/en/bycountry/FR/?page="+str(page))
            
                res = requests.get(url, headers=headers)

                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;32m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 3:
        print("Israel\n")	
        print(printcolor)			
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,171):
			
                url = ("https://www.insecam.org/en/bycountry/IL/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;32m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 4:	
        print("Iran\n")	
        print(printcolor)		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,70):
			
                url = ("https://www.insecam.org/en/bycountry/PL/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;32m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 5:	
        print("Argentina\n")	
        print(printcolor)		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,40):
			
                url = ("https://www.insecam.org/en/bycountry/AR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;32m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    else:
        print(" ")

except KeyboardInterrupt:
        print (" ")
