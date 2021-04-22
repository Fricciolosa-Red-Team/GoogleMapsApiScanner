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

        api = ("custom search", "5$ / 1000 reqs.", url)

        vulnerable_apis.append(api)
    else:
        print("API key is not vulnerable for Custom Search API.")
        print("Reason: " + str(response.json()["error"]["errors"][0]["message"]))

    return vulnerable_apis
