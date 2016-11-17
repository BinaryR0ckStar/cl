<<<<<<< HEAD
import os
import time
from inspect import getsourcefile
from os.path import abspath

from PIL import Image
from selenium import webdriver


class listingInfoParse(object):
    def __init__(self, f):
        self.title = parse(f, "<Title>")
        self.type = parse(f, "<Type>")
        self.category = parse(f, "<Category>")
        self.email = parse(f, "<Email>")
        self.street = parse(f, "<Street>")
        self.city = parse(f, "<City>")
        self.xstreet = parse(f, "<CrossStreet>")
        self.state = parse(f, "<State>")
        self.postal = parse(f, "<Postal>")
        self.specificlocation = parse(f, "<SpecificLocation>")
        self.body = parse(f, "<Body>")
=======
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import datetime
import os
import shutil
from inspect import getsourcefile
from os.path import abspath
from gmail import Gmail
from datetime import date
from PIL import Image

gmailUser = ""
gmailPass = ""

#--------------------------------------- Importing Stuff ----------------------

file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)
listingsFolderDirectory = os.path.abspath(os.path.join(file_dir, "listings"))
listedFolderDirectory = os.path.join(listingsFolderDirectory,"listed")
chromedriver = file_dir + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#------------------------------- Set Up Necessary Directories ---------

class listingInfoParse(object):
    def __init__(self,f):
    	self.email = parsing(f,"<email>")
    	self.password = parsing(f,"<password>")
        self.title = parsing(f,"<Title>")
        self.type = parsing(f,"<Type>")
        self.category = parsing(f,"<Category>")
        self.email = parsing(f,"<Email>")
        self.street = parsing(f,"<Street>")
        self.city = parsing(f,"<City>")
        self.xstreet = parsing(f,"<CrossStreet>")
        self.state = parsing(f,"<State>")
        self.postal = parsing(f,"<Postal>")
        self.specificlocation = parsing(f,"<SpecificLocation>")
        self.body = parsing(f,"<Body>")
>>>>>>> origin/master
        # just get rid of everything that not unicode
        self.body = ''.join([i if ord(i) < 128 else '' for i in self.body])
        # tabs will actually go to the next field in craiglist
        self.body = " ".join(self.body.split("\t"))
<<<<<<< HEAD
        self.price = parse(f, "<Price>")


def login(driver, username, password):
    username_input = driver.find_element_by_id("inputEmailHandle")
    password_input = driver.find_element_by_id("inputPassword")

    username_input.send_keys(username)
    password_input.send_keys(password)

    driver.find_element_by_class_name("accountform-btn").click()


def clickPhoenixAZ(driver):
    driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/select/option[487]").click()


def clickGo(driver):
    driver.find_element_by_xpath("//input[@value='go']").click()


def clickContinue(driver):
    driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/input").click()


def clickForSaleByOwner(driver):
    driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[6]/input").click()


def clickelElectronicsByOwner(driver):
    driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[22]").click()


def clickDoneOnImageUploading(driver):
    driver.find_element_by_xpath("//*[@id='pagecontainer']/section/form/button").click()


def clickValleyWest(driver):
    driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[4]").click()


# Don't always have to do this
def clickAbideByGuidelines(driver):
    try:
        driver.find_element_by_xpath("//*[@id='pagecontainer']/section/div/form/button").click()
    except:
        pass


def clickClassImageUploader(driver):
    driver.find_element_by_id("classic").click()


def clickListingType(driver, listing):
    driver.find_element_by_xpath(
        "//*[@id='pagecontainer']/section/form/blockquote//label[contains(.,'" + listing.type + "')]/input").click()


def clickListingCategory(driver, listing):
    driver.find_element_by_xpath(
        "//*[@id='pagecontainer']/section/form/blockquote//label[contains(.,'" + listing.category + "')]/input").click()


def uploadImagePath(driver, image):
    driver.find_element_by_xpath(".//*[@id='uploader']/form/input[3]").send_keys(image)


def fillOutListing(driver, listing):
    driver.find_element_by_id("PostingTitle").send_keys(listing.title)
    driver.find_element_by_id("postal_code").send_keys(listing.postal)
    driver.find_element_by_id("PostingBody").send_keys(listing.body)
    if listing.specificlocation:
        driver.find_element_by_id("GeographicArea").send_keys(listing.specificlocation)
    driver.find_element_by_id("Ask").send_keys(listing.price)
    driver.find_element_by_xpath("//*[@id='postingForm']/button").click()


def fillOutGeolocation(driver, listing):
    time.sleep(3)
    driver.find_element_by_id("xstreet0").send_keys(listing.street)
    driver.find_element_by_id("xstreet1").send_keys(listing.xstreet)
    driver.find_element_by_id("city").send_keys(listing.city)
    driver.find_element_by_id("region").send_keys(listing.state)
    time.sleep(1)
    driver.find_element_by_id("search_button").click()
    time.sleep(2)
    # driver.find_element_by_id("postal_code").send_keys(postal) #Should already be there
    driver.find_element_by_xpath("//*[@id='leafletForm']/button[1]").click()


def removeImgExifData(path):
    filename, extension = os.path.splitext(path)
    fullFilename = filename + extension
=======
        self.price = parsing(f,"<Price>")


#-------------------------------FUNCTIONING LOGIN From Reddit guy----------
from selenium import webdriver
import os
from inspect import getsourcefile
from os.path import abspath

file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)
driver = webdriver.Chrome(file_dir + "/chromedriver")
driver.get("https://accounts.craigslist.org/login?lang=en&cc=us")

username = driver.find_element_by_id("inputEmailHandle")
password = driver.find_element_by_id("inputPassword")

username.send_keys("")
password.send_keys("")

def clickPhoenixAZ(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/select/option[487]").click()
def clickContinue(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/input").click()


#------------------------------  Driver Navigation -----------------
#GDM - ignore for test DO I need to actually click my account? def clickmyaccount(listing):
#	listing.driver.find_element_by_xpath(".//*[@id='postlks']/li[2]/a").click()
 
#def filloutuserid(listing):
 #   listing.driver.find_element_by_id("inputEmailHandle").send_keys(listing.email)
#def filloutpassword(listing):
#    listing.driver.find_element_by_id("inputPassword").send_keys(listing.password)
def clickLogin(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/div/div[1]/form/div[3]/button").click()
def clickPhoenixAZ(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/select/option[487]").click()
def clickContinue(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/input").click()
def clickForSaleByOwner(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[6]/input").click()
def clickelElectronicsByOwner(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[22]").click()
def clickDoneOnImageUploading(listing):
	listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/form/button").click()
def clickValleyWest(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[4]").click()
def clickContinue(listing):
	listing.driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/button").click()
 
# Don't always have to do this
def clickAbideByGuidelines(listing):
    try:
        listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/div/form/button").click()
    except:
        pass

def clickClassImageUploader(listing):
	listing.driver.find_element_by_id("classic").click()

def clickListingType(listing):
    listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/form/blockquote//label[contains(.,'" + listing.type + "')]/input").click()

def clickListingCategory(listing):
    listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/form/blockquote//label[contains(.,'" + listing.category + "')]/input").click()

def uploadImagePath(listing,image):
	listing.driver.find_element_by_xpath(".//*[@id='uploader']/form/input[3]").send_keys(image)

def fillOutListing(listing):
 #  listing.driver.find_element_by_id("EmailHandle").send_keys(listing.email)
 #  listing.driver.find_element_by_id("ConfirmEMail").send_keys(listing.email)
    listing.driver.find_element_by_id("PostingTitle").send_keys(listing.title)
    listing.driver.find_element_by_id("postal_code").send_keys(listing.postal)
    listing.driver.find_element_by_id("PostingBody").send_keys(listing.body)
    listing.driver.find_element_by_id("GeographicArea").send_keys(listing.specificlocation)
    listing.driver.find_element_by_id("Ask").send_keys(listing.price)
    listing.driver.find_element_by_xpath("//*[@id='postingForm']/button").click()

def fillOutGeolocation(listing):
    time.sleep(3)
    listing.driver.find_element_by_id("xstreet0").send_keys(listing.street)
    listing.driver.find_element_by_id("xstreet1").send_keys(listing.xstreet)
    listing.driver.find_element_by_id("city").send_keys(listing.city)
    listing.driver.find_element_by_id("region").send_keys(listing.state)
    time.sleep(1)
    listing.driver.find_element_by_id("search_button").click()
    time.sleep(2)
    #listing.driver.find_element_by_id("postal_code").send_keys(postal) #Should already be there
    listing.driver.find_element_by_xpath("//*[@id='leafletForm']/button[1]").click()

def removeImgExifData(path):
    filename, extension = os.path.splitext(path)
    fullFilename = filename+extension
>>>>>>> origin/master
    image = Image.open(fullFilename)
    data = list(image.getdata())
    imageNoExif = Image.new(image.mode, image.size)
    imageNoExif.putdata(data)
    imageNoExif.save(filename + "copy" + extension)
    os.remove(filename + extension)
<<<<<<< HEAD
    os.rename(filename + "copy" + extension, fullFilename)


def uploadListingImages(driver, listing):
    clickClassImageUploader(driver)
    for image in listing.images:
        removeImgExifData(image)
        uploadImagePath(driver, image)
        time.sleep(5)
    clickDoneOnImageUploading(driver)


def clickAcceptTerms(driver):
    driver.find_element_by_xpath(
        "//*[@id='pagecontainer']/section/section[1]//button[contains(.,'ACCEPT the terms of use')]").click()


def clickPublishListing(driver):
    driver.find_element_by_xpath(
        "//*[@id='pagecontainer']/section/div[1]/form/button[contains(.,'publish')]").click()


def postListing(driver, listing):
    clickListingType(driver, listing)
    clickListingCategory(driver, listing)
    clickValleyWest(driver)
    clickAbideByGuidelines(driver)
    fillOutListing(driver, listing)
    fillOutGeolocation(driver, listing)
    uploadListingImages(driver, listing)
    clickPublishListing(driver)


def parse(f, splits):
    if splits not in f:
        return

=======
    os.rename(filename + "copy" + extension,fullFilename)

def uploadListingImages(listing):
    clickClassImageUploader(listing)
    for image in listing.images:
        removeImgExifData(image)
        uploadImagePath(listing,image)
        time.sleep(5)
    clickDoneOnImageUploading(listing)

def clickAcceptTerms(listing):
    listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/section[1]//button[contains(.,'ACCEPT the terms of use')]").click()

def clickPublishListing(listing):
	listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/div[1]/form/button[contains(.,'publish')]").click()

def postListing(listing):
    clickListingType(listing)
    clickListingCategory(listing)
    clickValleyWest(listing)
    clickAbideByGuidelines(listing)
    fillOutListing(listing)
    fillOutGeolocation(listing)
    uploadListingImages(listing)
    clickPublishListing(listing)

# --------------------------- Emails ---------------------

def getFirstCraigslistEmailUrl(listing,emails):
    for email in emails:
        email.fetch()
        email.read()
        if listing.title[0:15] in email.subject:
            emailMessage = email.body
            email.archive()
            acceptTermsLink = emailMessage.split("https")
            acceptTermsLink = acceptTermsLink[1].split("\r\n")
            return acceptTermsLink[0]

def acceptTermsAndConditions(listing,termsUrl):
    listing.driver.get("https" + termsUrl)
    clickAcceptTerms(listing)

def acceptEmailTerms(listing):
    gmail = Gmail()
    gmail.login(gmailUser,gmailPass)

    today = date.today()
    year = today.year
    month = today.month
    day = today.day

    time.sleep(120)
    print "Checking email"
    emails = gmail.inbox().mail(sender="robot@craigslist.org",unread=True,after=datetime.date(year, month, day-1))
    termsUrl = getFirstCraigslistEmailUrl(listing,emails)
    acceptTermsAndConditions(listing,termsUrl)

    gmail.logout()
    print "Done Checking Email"


# --------------------------- Craigslist Posting Actions ---------------

def moveFolder(folder,listedFolderDirectory):

    now = time.strftime("%c")

    # %x >>>get the date like this 7/16/2014
    today_dir = os.path.join(listedFolderDirectory,time.strftime("%x").replace("/","-"))

    # Make todays date under the listed directory
    
    #commented out since the function isn't defined - michael mitchell
    #makeFolder(today_dir)


    # added the below to create the dir for realsies - http://stackoverflow.com/questions/1274405/how-to-create-new-folder
    if not os.path.exists(today_dir):
    	os.makedirs(today_dir)
    # end of added code


    # Move the folder to the listed todays date directory
    shutil.move(folder, today_dir)

def parsing(f,splits):
>>>>>>> origin/master
    fsplit = f.split(splits)
    return fsplit[1]


<<<<<<< HEAD
def getOrderedListingImages(folder):
    print('listingFolder', folder)
    listingImages = [f for f in os.listdir(folder) if
                     os.path.isfile(os.path.join(folder, f)) and f[0] != '.' and f != 'info.txt']
    print('listingImages', listingImages)
    secondList = [os.path.abspath(os.path.join(folder, x)) for x in listingImages if
                  (x[1] != "_") or (x[0].isdigit() == False) and x[0] != '.']
    firstList = [os.path.abspath(os.path.join(folder, x)) for x in listingImages if
                 (x[1] == "_") and (x[0].isdigit()) and x[0] != '.']
=======
# If more than 24 hours passed will look like
# 1 day, 13:37:47.356000
def hasItBeenXDaysSinceFolderListed(folder,x):
    dateSplit = folder.split('-')
    folderDate = datetime.date(int(dateSplit[2]) + 2000, int(dateSplit[0]), int(dateSplit[1]))
    currentDatetime = datetime.datetime.now()
    folderTimePassed = currentDatetime - datetime.datetime.combine(folderDate, datetime.time())
    if "day" not in str(folderTimePassed):
        return False
    daysPassed = str(folderTimePassed).split('day')[0]
    if int(daysPassed.strip()) >= x:
        return True
    return False

def getOrderedListingImages(listingFolder):
    print 'listingFolder',listingFolder
    listingImages = [f for f in os.listdir(listingFolder) if os.path.isfile(os.path.join(listingFolder,f)) and f[0] != '.'  and f != 'info.txt' ]
    print 'listingImages',listingImages
    secondList = [os.path.abspath(os.path.join(listingFolder, x)) for x in listingImages if (x[1] != "_") or (x[0].isdigit() == False) and x[0] != '.']
    firstList = [os.path.abspath(os.path.join(listingFolder, x)) for x in listingImages if (x[1] == "_") and (x[0].isdigit()) and x[0] != '.']
>>>>>>> origin/master

    firstList.sort()
    secondList.sort()

    orderedListingImages = []
<<<<<<< HEAD
    for x in firstList: orderedListingImages.append(x)
    for x in secondList: orderedListingImages.append(x)
    return orderedListingImages


file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)

# List Items
listingsFolderDirectory = './listings'
listingFolders = [current_listing for current_listing in os.listdir(listingsFolderDirectory) if
                  current_listing[0] != "." and current_listing != "listed"]

for listingFolder in listingFolders:
    listingFolder = os.path.abspath(os.path.join(listingsFolderDirectory, listingFolder))
    with open(os.path.abspath(os.path.join(listingFolder, 'info.txt')), 'r') as info:
        current_listing = listingInfoParse(info.read())
    current_listing.images = getOrderedListingImages(listingFolder)

    # Set up the webdriver
    chrome_driver = webdriver.Chrome(file_dir + "/chromedriver")
    chrome_driver.get("https://accounts.craigslist.org/login?lang=en&cc=us")

    # Login to CraigsList
    login(chrome_driver, "stsrrmbq@pokemail.net", "stsrrmbq123456")

    # Select Phoenix, Arizona
    clickPhoenixAZ(chrome_driver)
    clickGo(chrome_driver)

    # Post the listing
    postListing(chrome_driver, current_listing)
    time.sleep(120)
    print "Waiting 2 minutes"

chrome_driver.close()

print "No More Craiglist Items To List"

=======
    for x in firstList:orderedListingImages.append(x)
    for x in secondList:orderedListingImages.append(x)
    return orderedListingImages

# Get all the date folders of listed items
listedItemsFolders = [folder for folder in os.listdir(listedFolderDirectory) if folder[0] != "."]

# Moving items that are 3 days or older back into the queue to get listed again
for dayListedFolder in listedItemsFolders:

    if (hasItBeenXDaysSinceFolderListed(dayListedFolder,3) == False):
        continue

    listedFolders = [listedFolders for listedFolders in os.listdir(os.path.join(listedFolderDirectory,dayListedFolder)) if listedFolders[0] != "."]
    dayListedFolderDirectory = os.path.join(listedFolderDirectory,dayListedFolder)

    for listedFolder in listedFolders:
        theListedFolderDirectory = os.path.join(dayListedFolderDirectory,listedFolder)
        shutil.move(theListedFolderDirectory,listingsFolderDirectory)
    shutil.rmtree(dayListedFolderDirectory)


# List Items
listingFolders = [listing for listing in os.listdir(listingsFolderDirectory) if listing[0] != "." and listing != "listed"]

for listingFolder in listingFolders:
    listingFolder = os.path.abspath(os.path.join(listingsFolderDirectory, listingFolder))
    with open(os.path.abspath(os.path.join(listingFolder, 'info.txt')), 'r') as info:
        listing = listingInfoParse(info.read())
    listing.images = getOrderedListingImages(listingFolder)
    listing.driver = webdriver.Chrome(chromedriver)
    listing.driver.get("https://accounts.craigslist.org/login/home");
    postListing(listing)
    acceptEmailTerms(listing)
    moveFolder(listingFolder,listedFolderDirectory)
    listing.driver.close()
    time.sleep(120)
    print "Waiting 2 minutes"
print "No More Craiglist Items To List"
>>>>>>> origin/master
