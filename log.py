import mechanize 
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")]

sign_in = br.open("https://recruitment.medpanel.com/newdesign/site/medpanel/login.php")  

br.select_form(nr = 0) 
br["managerUsername"] = "praveen@medpanel.com" 
br["managerPassword"] = "Test1234"    

logged_in = br.submit()   

logincheck = logged_in.read()  
bs = BeautifulSoup(logincheck, "html.parser")
title= bs.find_all('h3')
print(title)
print('------------------------------------------------------------------------')
print(logincheck) 

#req = br.open("http://school.dwit.edu.np/mod/assign/").read()
#accessing other url(s) after login is done this way 