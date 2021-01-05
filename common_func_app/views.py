from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import json
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from .models import SearchText
from selenium.webdriver import ActionChains
import requests
from django.http import HttpResponse

def getHeaders(restApiKey): 
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Basic %s" %restApiKey
    }
    headers["Authorization"] = headers["Authorization"].replace('"', "")
    return headers

def index(request): 
    return render(request, "home.html", {})

@csrf_exempt
def shutDown(request): 
    os.system("shutdown /s /t 1")
    return render(request, "home.html", {})

@csrf_exempt
def allowNotifications(request): 
    return render(request, "notification.html", {})

@csrf_exempt
def sendNotification(request): 
    appId = "66600201-6c1c-41fb-b2ef-1970878b51e1"
    restApiKey = "OWFiNzc4YTgtZTFjNC00MWI5LWJiYzgtNDQ1YzcwYjZiNDBk"
    baseUrl = "https://onesignal.com/api/v1/notifications"
    headers = getHeaders(restApiKey)
    payload = {
        "app_id": appId,
        "included_segments": ["All"],
        "contents": {
            "en": "Hello Aditya"
        }
    }
    response = requests.post(baseUrl, headers=headers, data=json.dumps(payload))
    print(response.status_code, response.reason)
    return HttpResponse("Success")

@csrf_exempt
def launchYoutube(request):
    if request.method == "POST":
        form = SearchText(request.POST or None)
        if form.is_valid():
            text = form.cleaned_data.get("searchText")
            url = "https://www.youtube.com/"
            driver = webdriver.Chrome()
            driver.get(url)
            driver.implicitly_wait(15)
            driver.maximize_window()
            searchBar = driver.find_element_by_xpath("//input[@id='search']")
            searchBar.send_keys(text)
            searchBar.send_keys(Keys.ENTER)
            # ActionChains(driver).move_to_element(searchBar).click(searchBar).perform()
            # searchButton = driver.find_element_by_xpath("//button[@id='search-icon-legacy']")
            # searchButton.click()
            driver.implicitly_wait(15)
            driver.find_element_by_xpath("//a[@id='video-title']").click()
            # driver.find_element_by_id("video-title").click()
            # videoElement = driver.find_element_by_xpath("//img[@id='img']")
            # videoElement.click()
    return render(request, "home.html", {})
        
