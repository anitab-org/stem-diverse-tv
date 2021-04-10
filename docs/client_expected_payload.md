---
title: Client Expected Payload
slug: /Backend/client_expected_payload
---
# Frontend requirements:

STEM Diverse TV is a backend project which provides informations for our frontend. Frontend build using Applicaster App Builder and it support 8 platforms:
- Android mobile
- iOS
- Android TV
- Amazon Fire
- TvOS
- Samsung
- LG
- Roku

## Applicaster frontend require specific data structure to be provided by backend:
`url` in `entry.content.src` is Base64 url to section.
### Category structure:

```
{
  "type": {
    "value": "feed"
  },
  "title": "HOME",
  "id": "HOMEId",
  "entry": [
    {
      "type": {
        "value": "feed"
      },
      "title": "HOME",
      "id": "search",
      "content": {
        "type": "feed",
        "src": "general-provider://fetchData?type=FEED_JSON&url=aHR0cHM6Ly9kbC5kcm9wYm94LmNvbS9zLzlpcWdscTFsbTJ5bzFhei9pbmxpbmVwbGF5ZXIuanNvbj9kbD0w"
      }
    },
    {
      "type": {
        "value": "feed"
      },
      "title": "HOME2",
      "id": "search2",
      "content": {
        "type": "feed",
        "src": "general-provider://fetchData?type=FEED_JSON&url=aHR0cHM6Ly9kbC5kcm9wYm94LmNvbS9zL3hoc202cjl2NmVnc2M5dC9lbGJlX2ZlZWQuanNvbj9kbD0w"
      }
    }
  ]
}
```

### Section structure:
```
{
  "type": { "value": "feed" },
  "author": { "name": "STEM DIVERSE TV" },
  "id": "NSB-03",
  "title": "LATEST",
  "media_group": [],
  "entry": [
    {
      "author": { "name": "SAS Software" },
      "type": { "value": "video" },
      "id": "NSBT-0001",
      "title": "STEM Career Showcase for Students with Disabilities 2017",
      "summary": "Students with disabilities meet and learn from successful STEM role models with similar disabilities at the North Carolina Museum of Natural Sciences.",
      "published": "2005-04-06T20:25:05-08:00",
      "updated": "2005-04-06T20:25:05-08:00",
      "content": {
        "src": "https://www.youtube.com/watch?v=AsAvCVAiqJo",
        "type": "video/hls"
      },
      "link": { "type": "link", "href": "" },
      "media_group": [
        {
          "type": "image",
          "media_item": [
            {
              "key": "image_base",
              "src": "http://i3.ytimg.com/vi/AsAvCVAiqJo/maxresdefault.jpg",
              "type": "extern_image"
            }
          ]
        }
      ],
      "extensions": { "section": "None" }
    }
  ]
}
```

Custom data can be provided in extensions.
