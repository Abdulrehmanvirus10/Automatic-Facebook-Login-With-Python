import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from webdriver_manager.firefox import GeckoDriverManager
import getpass
import keyboard #pip install keyboard

# Initiliaze Webdriver
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
	# Else Try this driver = webdriver.Chrome(executable_path="") Downloaded from https://chromedriver.chromium.org/downloads
except:
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def FacebookLogin():
    #Enter Your Email ID And Password
	user=input('Enter Email Id:')  
	password= getpass('Enter Password:')

	#Opening Facebook.
	driver.get('https://www.facebook.com/') 
	print ("Facebook Opened") 
	time.sleep(1) 
	  
    #Entering Email and Password
	username_box = driver.find_element_by_id('email') 
	username_box.send_keys(user) 
	print ("Email Id entered") 
	time.sleep(1) 
	  
	password_box = driver.find_element_by_id('pass') 
	password_box.send_keys(password) 
	print ("Password entered") 

	#Pressing The Login Button  
	login_box = driver.find_element_by_id('loginbutton') 
	login_box.click() 

	  
	print ("Done") 
	closing = input('Press anything to quit')
	if key.is_pressed('esc'):
		driver.quit() 
		print("Finished")

FacebookLogin()


