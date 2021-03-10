from urllib.parse import urlparse, parse_qs


def extract_video_id(url):
    # eg:
    # - http://youtu.be/SA2iWivDJiE
    # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    # - http://www.youtube.com/embed/SA2iWivDJiE
    # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    query = urlparse(url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in {"www.youtube.com", "youtube.com"}:
        if query.path == "/watch":
            return parse_qs(query.query)["v"][0]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]
    return None


def yt_duration_to_seconds(duration):
    # eg: P1W2DT6H21M32S
    week = 0
    day = 0
    hour = 0
    min = 0
    sec = 0

    duration = duration.lower()

    value = ""
    for c in duration:
        if c.isdigit():
            value += c
            continue

        elif c == "p":
            pass
        elif c == "t":
            pass
        elif c == "w":
            week = int(value) * 604800
        elif c == "d":
            day = int(value) * 86400
        elif c == "h":
            hour = int(value) * 3600
        elif c == "m":
            min = int(value) * 60
        elif c == "s":
            sec = int(value)

        value = ""

    return week + day + hour + min + sec
