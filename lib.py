import requests
import os
import scanners
import table


def scan_gmaps(apikey):

    headings = ["Api", "Cost", "Poc"]
    align = [("^", "<"), ("^", "<"), ("^", "<")]
    vulnerable_apis = []

    vulnerable_apis = scanners.custom_search(apikey, vulnerable_apis)

    vulnerable_apis = scanners.static_map(apikey, vulnerable_apis)

    vulnerable_apis = scanners.street_view(apikey, vulnerable_apis)

    vulnerable_apis = scanners.embed_basic(apikey, vulnerable_apis)

    vulnerable_apis = scanners.embed_advanced(apikey, vulnerable_apis)

    vulnerable_apis = scanners.directions(apikey, vulnerable_apis)

    vulnerable_apis = scanners.geocode(apikey, vulnerable_apis)

    vulnerable_apis = scanners.distance_matrix(apikey, vulnerable_apis)

    vulnerable_apis = scanners.find_place_from_text(apikey, vulnerable_apis)

    vulnerable_apis = scanners.autocomplete(apikey, vulnerable_apis)

    vulnerable_apis = scanners.elevation(apikey, vulnerable_apis)

    url = (
        "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("errorMessage") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Timezone API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Timezone 			|| $5 per 1000 requests")
    else:
        print("API key is not vulnerable for Timezone API.")
        print("Reason: " + response.json()["errorMessage"])

    url = (
        "https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|\
60.170877,24.942796&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Nearest Roads API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Nearest Roads 		|| $10 per 1000 requests")
    else:
        print("API key is not vulnerable for Nearest Roads API.")
        print("Reason: " + response.json()["error"]["message"])

    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + apikey
    postdata = {"considerIp": "true"}
    response = requests.post(url, data=postdata, verify=False)
    if response.text.find("error") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0mfor Geolocation API! Here is the PoC curl command \
which can be used from terminal:"
        )
        print(
            "curl -i -s -k  -X $'POST' -H $'Host: www.googleapis.com' -H $'Content-Length: 22' --data-binary \
$'{\"considerIp\": \"true\"}' $'"
            + url
            + "'"
        )
        vulnerable_apis.append("Geolocation 			|| $5 per 1000 requests")
    else:
        print("API key is not vulnerable for Geolocation API.")
        print("Reason: " + response.json()["error"]["message"])

    url = (
        "https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907&interpolate=true&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Route to Traveled API! Here is the PoC \
link which can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Route to Traveled 		|| $10 per 1000 requests")
    else:
        print("API key is not vulnerable for Route to Traveled API.")
        print("Reason: " + response.json()["error"]["message"])

    url = (
        "https://roads.googleapis.com/v1/speedLimits?path=38.75807927603043,-9.03741754643809&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Speed Limit-Roads API! Here is the PoC \
link which can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Speed Limit-Roads 		|| $20 per 1000 requests")
    else:
        print("API key is not vulnerable for Speed Limit-Roads API.")
        print("Reason: " + response.json()["error"]["message"])

    url = (
        "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4\
&fields=name,rating,formatted_phone_number&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Place Details API! Here is the PoC \
link which can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Place Details 		|| $17 per 1000 requests")
    else:
        print("API key is not vulnerable for Place Details API.")
        print("Reason: " + response.json()["error_message"])

    url = (
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.\
1957362&radius=100&types=food&name=harbour&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Nearby Search-Places API! Here is the \
PoC link which can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Nearby Search-Places		|| $32 per 1000 requests")
    else:
        print("API key is not vulnerable for Nearby Search-Places API.")
        print("Reason: " + response.json()["error_message"])

    url = (
        "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Sydney&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Text Search-Places API! Here is the PoC \
link which can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Text Search-Places 		|| $32 per 1000 requests")
    else:
        print("API key is not vulnerable for Text Search-Places API.")
        print("Reason: " + response.json()["error_message"])

    url = (
        "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CnRtAAAATLZNl354RwP_\
9UKbQ_5Psy40texXePv4oAlgP4qNEkdIrkyse7rPXYGd9D_Uj1rVsQdWT4oRz4QrYAJNpFX7rzqqMlZw2h2E2y5IKMUZ7ouD_SlcHxYq1yL\
4KbKUv3qtWgTK0A6QbGh87GB3sscrHRIQiG2RrmU_jF4tENr9wGS_YxoUSSDrYjWmrNfeEHSGSc3FyhNLlBU&key="
        + apikey
    )
    response = requests.get(url, verify=False, allow_redirects=False)
    if response.status_code == 302:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Places Photo API! Here is the PoC link \
which can be used directly via browser:"
        )
        print(url)
        vulnerable_apis.append("Places Photo 			|| $7 per 1000 requests")
    else:
        print("API key is not vulnerable for Places Photo API.")
        print(
            "Reason: Verbose responses are not enabled for this API, cannot determine the reason."
        )

    url = (
        "https://playablelocations.googleapis.com/v3:samplePlayableLocations?key="
        + apikey
    )
    postdata = {
        "area_filter": {"s2_cell_id": 7715420662885515264},
        "criteria": [
            {
                "gameObjectType": 1,
                "filter": {"maxLocationCount": 4, "includedTypes": ["food_and_drink"]},
                "fields_to_return": {"paths": ["name"]},
            },
            {
                "gameObjectType": 2,
                "filter": {"maxLocationCount": 4},
                "fields_to_return": {"paths": ["types", "snapped_point"]},
            },
        ],
    }
    response = requests.post(url, data=postdata, verify=False)
    if response.text.find("error") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0mfor Playable Locations API! Here is the \
PoC curl command which can be used from terminal:"
        )
        print(
            'curl -i -s -k  -X $\'POST\' -H $\'Host: playablelocations.googleapis.com\' \
-H $\'Content-Length: 302\' --data-binary $\'{"area_filter":{"s2_cell_id":77154206628855152\
64},"criteria":[{"gameObjectType":1,"filter":{"maxLocationCount":4,"includedTypes":["fo\
od_and_drink"]},"fields_to_return": {"paths": ["name"]}},{"gameObjectType":2,"filter":{"maxLoca\
tionCount":4},"fields_to_return": {"paths": ["types", "snapped_point"]}}]}\' $\''
            + url
            + "'"
        )
        vulnerable_apis.append("Playable Locations 	|| $10 per 1000 daily active users")
    else:
        print("API key is not vulnerable for Playable Locations API.")
        print("Reason: " + response.json()["error"]["message"])

    url = "https://fcm.googleapis.com/fcm/send"
    postdata = "{'registration_ids':['ABC']}"
    response = requests.post(
        url,
        data=postdata,
        verify=False,
        headers={"Content-Type": "application/json", "Authorization": "key=" + apikey},
    )
    if response.status_code == 200:
        print(
            "API key is \033[1;31;40m vulnerable \033[0mfor FCM API! Here is the PoC curl \
command which can be used from terminal:"
        )
        print(
            'curl --header "Authorization: key='
            + apikey
            + '" --header Content-Type:"application/json" https://fcm.googleapis.com/fc\
m/send -d \'{"registration_ids":["ABC"]}\''
        )
        vulnerable_apis.append("FCM Takeover 			|| https://abss.me/posts/fcm-takeover/")
    else:
        print("API key is not vulnerable for FCM API.")
        for lines in response.iter_lines():
            if ("TITLE") in str(lines):
                print(
                    "Reason: "
                    + str(lines).split("TITLE")[1].split("<")[0].replace(">", "")
                )

    print("-------------------------------------------------------------")
    print("  Results 			|| Cost Table/Reference to Exploit:")
    print("-------------------------------------------------------------")
    for i in range(len(vulnerable_apis)):
        print("- " + vulnerable_apis[i])
    print("-------------------------------------------------------------")
    print("Reference for up-to-date pricing:")
    print("https://cloud.google.com/maps-platform/pricing")
    print("https://developers.google.com/maps/billing/gmp-billing")
    jsapi = input(
        "Do you want to conduct tests for Javascript API? (Will need manual confirmation + file creation) (Y/N)"
    )
    if jsapi == "Y" or jsapi == "y":
        f = open("jsapi_test.html", "w+")
        f.write(
            '<!DOCTYPE html><html><head><script src="https://maps.googleapis.com/maps/api/js?key='
            + apikey
            + '&callback=initMap&libraries=&v=weekly" defer></script><style type="text/cs\
s">#map{height:100%;}html,body{height:100%;margin:0;padding:0;}</style><script>let map;func\
tion initMap(){map=new google.maps.Map(document.getElementById("map"),{center:{lat:-34\
.397,lng:150.644},zoom:8,});}</script></head><body><div id="map"></div></body></html>'
        )
        f.close()
        print(
            "jsapi_test.html file is created for manual confirmation. Open it at your \
browser and observe whether the map is successfully loaded or not."
        )
        print(
            "If you see 'Sorry! Something went wrong.' error on the page, it means \
that API key is not allowed to be used at JavaScript API."
        )
        os.remove("jsapi_test.html")
    print("Operation is over. Thanks for using G-Maps API Scanner!")
    return True
