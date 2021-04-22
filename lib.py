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

    vulnerable_apis = scanners.timezone(apikey, vulnerable_apis)

    vulnerable_apis = scanners.nearest_roads(apikey, vulnerable_apis)

    vulnerable_apis = scanners.geolocation(apikey, vulnerable_apis)

    vulnerable_apis = scanners.route_to_traveled(apikey, vulnerable_apis)

    vulnerable_apis = scanners.speed_limit_roads(apikey, vulnerable_apis)

    vulnerable_apis = scanners.place_details(apikey, vulnerable_apis)

    vulnerable_apis = scanners.nearby_search_places(apikey, vulnerable_apis)

    vulnerable_apis = scanners.text_search_places(apikey, vulnerable_apis)

    vulnerable_apis = scanners.places_photo(apikey, vulnerable_apis)

    vulnerable_apis = scanners.playable_locations(apikey, vulnerable_apis)

    vulnerable_apis = scanners.fcm_takeover(apikey, vulnerable_apis)

    fields = [0, 1, 2]
    with open(apikey + ".md", "w+") as f:
        table.table(f, vulnerable_apis, fields, headings, align)

    print("-------------------------------------------------------------")
    print("          Api                 ||           Cost")
    print("-------------------------------------------------------------")
    for i in range(len(vulnerable_apis)):
        print(vulnerable_apis[i][0] + " - " + vulnerable_apis[i][1])
    print("-------------------------------------------------------------")
    print("Reference for up-to-date pricing:")
    print("https://cloud.google.com/maps-platform/pricing")
    print("https://developers.google.com/maps/billing/gmp-billing")
    jsapi = input(
        "Do you want to conduct tests for Javascript API? (Will need manual confirmation + file creation) (Y/N)"
    )
    if jsapi == "Y" or jsapi == "y":
        scanners.js_test(apikey)
    print("Operation is over. Thanks for using GoogleMapsAPIScanner!")
    print("")
    print("https://github.com/Fricciolosa-Red-Team/GoogleMapsApiScanner")
