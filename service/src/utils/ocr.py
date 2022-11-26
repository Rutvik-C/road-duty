import time

import requests
from decouple import config


def doOCR(imgPath):
    with open(imgPath, "rb") as f:
        data = f.read()

    endpoint = "https://roadduty.cognitiveservices.azure.com/" + "vision/v3.2/read/analyze"
    subscriptionKey = config("OCR_SUBSCRIPTION_KEY")
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey, 'Content-Type': 'application/octet-stream'}

    try:
        response = requests.post(endpoint, headers=headers, data=data)
        response.raise_for_status()
        operationUrl = response.headers["Operation-Location"]

        print(f"INFO: OCR: Request submitted. Waiting.")
        while True:
            responseFinal = requests.get(operationUrl, headers=headers)
            res = responseFinal.json()

            if "analyzeResult" in res:
                break
            if "status" in res and res["status"] == "failed":
                return None, None

            time.sleep(1)

        lines = res["analyzeResult"]["readResults"][0]["lines"]
        s = ""
        add, count = 0, 0
        for line in lines:
            s += line["text"]
            add += line["appearance"]["style"]["confidence"]
            count += 1

        return s.strip(), add / count
    
    except Exception as e:
        print(f"ERROR: OCR: Exception {e}")
        return None, None
