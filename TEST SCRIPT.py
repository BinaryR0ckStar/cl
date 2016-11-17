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
        # just get rid of everything that not unicode
        self.body = ''.join([i if ord(i) < 128 else '' for i in self.body])
        # tabs will actually go to the next field in craiglist
        self.body = " ".join(self.body.split("\t"))
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
    image = Image.open(fullFilename)
    data = list(image.getdata())
    imageNoExif = Image.new(image.mode, image.size)
    imageNoExif.putdata(data)
    imageNoExif.save(filename + "copy" + extension)
    os.remove(filename + extension)
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

    fsplit = f.split(splits)
    return fsplit[1]


def getOrderedListingImages(folder):
    print('listingFolder', folder)
    listingImages = [f for f in os.listdir(folder) if
                     os.path.isfile(os.path.join(folder, f)) and f[0] != '.' and f != 'info.txt']
    print('listingImages', listingImages)
    secondList = [os.path.abspath(os.path.join(folder, x)) for x in listingImages if
                  (x[1] != "_") or (x[0].isdigit() == False) and x[0] != '.']
    firstList = [os.path.abspath(os.path.join(folder, x)) for x in listingImages if
                 (x[1] == "_") and (x[0].isdigit()) and x[0] != '.']

    firstList.sort()
    secondList.sort()

    orderedListingImages = []
    for x in firstList: orderedListingImages.append(x)
    for x in secondList: orderedListingImages.append(x)
    return orderedListingImages


file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)

# List Items
listingsFolderDirectory = './listings'
listingFolders = [current_listing for current_listing in os.listdir(listingsFolderDirectory) if current_listing[0] != "." and current_listing != "listed"]

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

