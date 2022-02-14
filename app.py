import random
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
import sys
from dotenv import load_dotenv
load_dotenv();

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
botauth = os.getenv("BOTAUTH")

browser = webdriver.Firefox(executable_path=r'C:\Users\Burak\Desktop\geckodriver\geckodriver.exe')


quotesList = ['“You are never too old to set another goal or to dream a new dream.”\n— Malala Yousafzai',
              '“You define your own life. Don’t let other people write your script.\n”— Oprah Winfrey',
              '“You don’t always need a plan. Sometimes you just need to breathe, trust, let go and see what happens.\n”— Mandy Hale',
              '“Belief creates the actual fact.”\n— William James',
              '“I just want you to know that if you are out there and you are being really hard on yourself right now for something that has happened … it’s normal. That is what is going to happen to you in life. No one gets through unscathed. We are all going to have a few scratches on us. Please be kind to yourselves and stand up for yourself, please.”\n— Taylor Swift'
              '“You make a choice: continue living your life feeling muddled in this abyss of self-misunderstanding, or you find your identity independent of it. You draw your own box.”\n— Duchess Meghan'
              '“People tell you the world looks a certain way. Parents tell you how to think. Schools tell you how to think. TV. Religion. And then at a certain point, if you’re lucky, you realize you can make up your own mind. Nobody sets the rules but you. You can design your own life.”\n— Carrie Ann Moss'
              '“I want to be in the arena. I want to be brave with my life. And when we make the choice to dare greatly, we sign up to get our asses kicked. We can choose courage or we can choose comfort, but we can’t have both. Not at the same time.”\n— Brene Brown'
              '“If you have good thoughts they will shine out of your face like sunbeams and you will always look lovely.”\n— Roald Dahl'
              '“Find out who you are and be that person. That’s what your soul was put on this earth to be. Find that truth, live that truth, and everything else will come.”\n— Ellen DeGeneres'
              '“Life is like riding a bicycle. To keep your balance, you must keep moving.”\n– Albert Einstein'
              '“Faith is love taking the form of aspiration.”\n—William Ellery Channing'
              '“I have learned over the years that when one’s mind is made up, this diminishes fear; knowing what must be done does away with fear.”\n— Rosa Parks'
              '“What you get by achieving your goals is not as important as what you become by achieving your goals.”\n– Zig Ziglar'
              '“Out of the mountain of despair, a stone of hope.”\n— Martin Luther King, Jr.']


tagName = "#InspirationalQuotes"


browser.get("https://twitter.com/i/flow/login")

time.sleep(5)


#Email Input Login Section Start

emailInput = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")

emailInput.send_keys(email)

emailNextButton = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]");

emailNextButton.click()

time.sleep(5)


#Email Input Login Section End

#Bot Auth Section Start

botInput = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")

if(botInput):
    
    botInput.send_keys(botauth)

    botNextButton = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div")

    botNextButton.click()

time.sleep(5)

#Bot Auth Section End

#Password Input Login Section Start

passwordInput  = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")

passwordInput.send_keys(password)

passwordNextButton = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]")

passwordNextButton.click()

time.sleep(5)

#Password Input Login Section End

#Auto Tweeting Section Start

tweetSection = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")

time.sleep(5)


while True:
    
    tweetSection = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")
    
    quote = random.choice(quotesList) + "\nQuoteNumber : " + str(random.randint(0,sys.maxsize)) +"\n"+tagName
    
    tweetSection.send_keys(quote)
    
    tweetSection.send_keys(Keys.CONTROL + Keys.ENTER)
    
    time.sleep(5)

#Auto Tweeting Section End