""" 'license_number': 'MH48CA9074',
  'location': 'Nanodiwadi Vasalai',
  'manual_check': False"""

import requests


def get_rider_id_from_vahan_api(license_number):
    return 1


def make_challan(license_number, location, manual_check, image_locs):
    """calls drf to make challan

    Args:
        license_number (_type_): _description_
        location (_type_): _description_
        manual_check (_type_): _description_
        image_locs (dict):
            {"whole": ["path_To_whole_image"],
            "cutout":[ "path_To_cutout_image"],
            "bulk": ["path_To_bulk_image", "path_To_bulk_image", "path_To_bulk_image"..]}
    """

    BASE_URL = "http://127.0.0.1:8000/"

    endpoint = "challan/"

    data = {
        "location": "7878788",
        "license_number": "0907876765",
        "rider": get_rider_id_from_vahan_api(license_number),
        "status": "to_check_manually" if manual_check else "unpaid",
    }
    response = requests.post(url=BASE_URL + endpoint, data=data)
    print(response)
    new_challan_id = response.json()["id"]

    image_url = BASE_URL + "challan_image/"

    for key in image_locs:
        payload = {'challan': str(new_challan_id), 'type': key}
        i = 0
        for image_loc in image_locs[key]:
            files = [('image', (f'{i}.jpg', open(image_loc, 'rb'), 'image/jpeg'))]
            response = requests.post(image_url, data=payload, files=files)
            i += 1
            print(response.content)


make_challan(
    "1231", "loc", True,
    {"whole": [r'C:\Users\shubh\Downloads\hacktime demo\beach-quotes-1559667853.jpg'],
     "cutout": [r'C:\Users\shubh\Downloads\hacktime demo\beach-quotes-1559667853.jpg'],
     "bulk":
     [r'C:\Users\shubh\Downloads\hacktime demo\beach-quotes-1559667853.jpg',
      r'C:\Users\shubh\Downloads\hacktime demo\beach-quotes-1559667853.jpg',
      r'C:\Users\shubh\Downloads\hacktime demo\beach-quotes-1559667853.jpg'], })
