import json
import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from decouple import config
import cv2
import io


def doOCR(imgPath):
    with open(imgPath, "rb") as f:
        data = f.read()

    endpoint = "https://roadduty.cognitiveservices.azure.com/" + "vision/v3.2/read/analyze"
    subscriptionKey = config("OCR_SUBSCRIPTION_KEY")
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey, 'Content-Type': 'application/octet-stream'}

    response = requests.post(endpoint, headers=headers, data=data)
    response.raise_for_status()
    operationUrl = response.headers["Operation-Location"]

    res = {}
    poll = True
    while poll:
        responseFinal = requests.get(operationUrl, headers=headers)
        res = responseFinal.json()

        if "analyzeResult" in res:
            poll = False
        if "status" in res and res["status"] == "failed":
            poll = False

        time.sleep(1)

    lines = res["analyzeResult"]["readResults"][0]["lines"]
    s = ""
    for line in lines:
        s += line["text"]

    return s


print(doOCR(r"C:\# Everyday\RutvikLocal\1_PROJECTS\road-duty\service\test_output\lp-58405fe12226412aacaeb99afaa59773.jpg"))

