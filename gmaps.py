import warnings
import sys
from lib import scan_gmaps


def main():

    warnings.filterwarnings("ignore")
    if len(sys.argv) > 1:
        if sys.argv[1] == "--api-key" or sys.argv[1] == "-a":
            if len(sys.argv) > 2:
                scan_gmaps(sys.argv[2])
            else:
                print("Missing api key, aborting.")
                print(
                    'Either use --api-key as argument such "python gmaps.py --api-k\
    ey KEY" or directly run script as "python gmaps.py" and supply API key via input.'
                )
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(
                'Either use --api-key as argument such "python gmaps.py --api-key KEY" o\
    r directly run script as "python gmaps.py" and supply API key via input.'
            )
        else:
            print("Invalid arguments, aborting.")
            print(
                'Either use --api-key as argument such "python gmaps.py --api-key KEY" o\
    r directly run script as "python gmaps.py" and supply API key via input.'
            )
    else:
        apikey = input("Please enter the Google Maps API key you wanted to test: ")
        scan_gmaps(apikey)


if __name__ == "__main__":
    main()
