from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from .models import SearchText


def index(request): 
    return render(request, "home.html", {})

@csrf_exempt
def shutDown(request): 
    os.system("shutdown /s /t 1")
    return render(request, "home.html", {})


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
            searchButton = driver.find_element_by_xpath("//button[@id='search-icon-legacy']")
            searchButton.click()
            driver.implicitly_wait(15)
            videoElement = driver.find_element_by_xpath("//img[@id='img']")
            videoElement.click()
    return render(request, "home.html", {})
        
