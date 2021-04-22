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
