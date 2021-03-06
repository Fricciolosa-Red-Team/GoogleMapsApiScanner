import requests


def custom_search(apikey, vulnerable_apis):
    url = (
        "https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=lectures&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("errors") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Custom Search API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)

        api = ("custom search", "5$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Custom Search API.")
        print("Reason: " + str(response.json()["error"]["errors"][0]["message"]))

    return vulnerable_apis


def static_map(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Staticmap API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)

        api = ("static map", "2$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Staticmap API.")
        print("Reason: " + str(response.content))

    return vulnerable_apis


def street_view(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,\
-73.988354&fov=90&heading=235&pitch=10&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Streetview API! Here is the PoC \
link which can be used directly via browser:"
        )
        print(url)

        api = ("Streetview", "7$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Streetview API.")
        print("Reason: " + str(response.content))

    return vulnerable_apis


def embed_basic(apikey, vulnerable_apis):
    url = "https://www.google.com/maps/embed/v1/place?q=Seattle&key=" + apikey
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Embed (Basic) API! Here is \
the PoC HTML code which can be used directly via browser:"
        )
        print(
            '<iframe width="600" height="450" frameborder="0" style="border:0" src="'
            + url
            + '" allowfullscreen></iframe>'
        )
        poc = (
            '<iframe width="600" height="450" frameborder="0" style="border:0" src="'
            + url
            + '" allowfullscreen></iframe>'
        )

        api = ("embed basic", "Free", poc)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Embed (Basic) API.")
        print("Reason: " + str(response.content))

    return vulnerable_apis


def embed_advanced(apikey, vulnerable_apis):
    url = (
        "https://www.google.com/maps/embed/v1/search?q=record+stores+in+Seattle&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Embed (Advanced) API! Here is \
the PoC HTML code which can be used directly via browser:"
        )
        print(
            '<iframe width="600" height="450" frameborder="0" style="border:0" src="'
            + url
            + '" allowfullscreen></iframe>'
        )

        poc = (
            '<iframe width="600" height="450" frameborder="0" style="border:0" src="'
            + url
            + '" allowfullscreen></iframe>'
        )

        api = ("embed advanced", "Free", poc)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Embed (Advanced) API.")
        if len(str(response.content).split('"')) < 77:
            print("Reason: " + str(response.content))
        else:
            print("Reason: " + str(response.content).split('"')[77])

    return vulnerable_apis


def directions(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Directions API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)

        api1 = ("Directions", "5$/1000 reqs.", url)
        api2 = ("Directions (Advanced)", "5$/1000 reqs.", url)

        vulnerable_apis.append(api1)
        vulnerable_apis.append(api2)
    else:
        print("API key is not vulnerable for Directions API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def geocode(apikey, vulnerable_apis):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=" + apikey
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Geocode API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)

        api = ("Geocode", "5$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Geocode API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def distance_matrix(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,\
-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C\
-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.\
659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.\
659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Distance Matrix API! Here is the PoC link \
which can be used directly via browser:"
        )
        print(url)

        api1 = ("Distance Matrix", "5$/1000 reqs.", url)
        api2 = ("Distance Matrix (Advanced)", "10$/1000 reqs.", url)

        vulnerable_apis.append(api1)
        vulnerable_apis.append(api2)
    else:
        print("API key is not vulnerable for Distance Matrix API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def find_place_from_text(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemp\
orary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Find Place From Text API! Here is the \
PoC link which can be used directly via browser:"
        )
        print(url)

        api = ("Find place from text", "17$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Find Place From Text API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def autocomplete(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Autocomplete API! Here is the PoC link \
which can be used directly via browser:"
        )
        print(url)

        api1 = ("Autocomplete", "2.83$/1000 reqs", url)
        api2 = ("Autocomplete Per Session", "17$/1000 reqs", url)

        vulnerable_apis.append(api1)
        vulnerable_apis.append(api2)
    else:
        print("API key is not vulnerable for Autocomplete API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def elevation(apikey, vulnerable_apis):
    url = (
        "https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key="
        + apikey
    )
    response = requests.get(url, verify=False)
    if response.text.find("error_message") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0m for Elevation API! Here is the PoC link which \
can be used directly via browser:"
        )
        print(url)

        api = ("Elevation", "5$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Elevation API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def timezone(apikey, vulnerable_apis):
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

        api = ("Timezone", "5$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Timezone API.")
        print("Reason: " + response.json()["errorMessage"])

    return vulnerable_apis


def nearest_roads(apikey, vulnerable_apis):
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

        api = ("Nearest roads", "10$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Nearest Roads API.")
        print("Reason: " + response.json()["error"]["message"])

    return vulnerable_apis


def geolocation(apikey, vulnerable_apis):
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + apikey
    postdata = {"considerIp": "true"}
    response = requests.post(url, data=postdata, verify=False)
    if response.text.find("error") < 0:
        print(
            "API key is \033[1;31;40m vulnerable \033[0mfor Geolocation API! Here is the PoC curl command \
which can be used from terminal:"
        )
        poc = (
            "curl -i -s -k  -X $'POST' -H $'Host: www.googleapis.com' -H $'Content-Length: 22' --data-binary \
$'{\"considerIp\": \"true\"}' $'"
            + url
            + "'"
        )
        print(poc)

        api = ("Geolocation", "5$/1000 reqs.", poc)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Geolocation API.")
        print("Reason: " + response.json()["error"]["message"])

    return vulnerable_apis


def route_to_traveled(apikey, vulnerable_apis):
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

        api = ("Route to traveled", "10$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Route to Traveled API.")
        print("Reason: " + response.json()["error"]["message"])

    return vulnerable_apis


def speed_limit_roads(apikey, vulnerable_apis):
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

        api = ("Speed Limit Roads", "20$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Speed Limit-Roads API.")
        print("Reason: " + response.json()["error"]["message"])

    return vulnerable_apis


def place_details(apikey, vulnerable_apis):
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

        api = ("Place Details", "17$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Place Details API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def nearby_search_places(apikey, vulnerable_apis):
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

        api = ("Nearby Search Places", "32$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Nearby Search-Places API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def text_search_places(apikey, vulnerable_apis):
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

        api = ("Text Search Places", "32$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Text Search-Places API.")
        print("Reason: " + response.json()["error_message"])

    return vulnerable_apis


def places_photo(apikey, vulnerable_apis):
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

        api = ("Places Photo", "7$/1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Places Photo API.")
        print(
            "Reason: Verbose responses are not enabled for this API, cannot determine the reason."
        )

    return vulnerable_apis


def playable_locations(apikey, vulnerable_apis):
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
        poc = (
            'curl -i -s -k  -X $\'POST\' -H $\'Host: playablelocations.googleapis.com\' \
-H $\'Content-Length: 302\' --data-binary $\'{"area_filter":{"s2_cell_id":77154206628855152\
64},"criteria":[{"gameObjectType":1,"filter":{"maxLocationCount":4,"includedTypes":["fo\
od_and_drink"]},"fields_to_return": {"paths": ["name"]}},{"gameObjectType":2,"filter":{"maxLoca\
tionCount":4},"fields_to_return": {"paths": ["types", "snapped_point"]}}]}\' $\''
            + url
            + "'"
        )
        print(poc)

        api = ("Playable Locations", "10$/1000 daily active users", poc)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Playable Locations API.")
        print("Reason: " + response.json()["error"]["message"])

    return vulnerable_apis


def fcm_takeover(apikey, vulnerable_apis):
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
        poc = (
            'curl --header "Authorization: key='
            + apikey
            + '" --header Content-Type:"application/json" https://fcm.googleapis.com/fc\
m/send -d \'{"registration_ids":["ABC"]}\''
        )
        print(poc)

        api = ("FCM Takeover", "https://abss.me/posts/fcm-takeover/", poc)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for FCM API.")
        for lines in response.iter_lines():
            if ("TITLE") in str(lines):
                print(
                    "Reason: "
                    + str(lines).split("TITLE")[1].split("<")[0].replace(">", "")
                )

    return vulnerable_apis


def js_test(apikey):
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
