import urllib.request
import urllib.error


def check_health(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)

        if response.status == 200:
            print(f"HEALTHY: {url} returned HTTP 200")
        else:
            print(f"WARNING: {url} returned HTTP {response.status}")

    except urllib.error.URLError as error:
        print(f"UNHEALTHY: Could not reach {url}")
        print(f"Reason: {error}")


if __name__ == "__main__":
    check_health("https://www.google.com")