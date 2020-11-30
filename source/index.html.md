---
title: Wisdom Garden API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - python
  - javascript

includes:
  - errors
  - test

search: true

code_clipboard: true
---

# Introduction
智园API

# Room

## Get room stat to external application

```python
import requests
url = '/external-api/v2/shtvu/room/stat?room_code=11&app_key=1234567890&ts=1234567890'
response = requests.get(url)
print(response.content())

```

> The above command returns JSON structured like this:

```json
{
  "attendance_stat": {
    "attendance_count": 2,
    "attendance_rate": 100,
    "student_count": 2
  },
  "course_name": "测试模版课程1",
  "course_time": "2019-10-29T02:00:00Z - 2019-10-29T14:00:00Z",
  "instructors": "i",
  "interaction_stat": {
    "interaction_count": 21,
    "interaction_rate": 1.1
  }
}

```

This endpoint retrieves all kittens.

### HTTP Request

`GET /external-api/v2/shtvu/room/stat?room_code=11&app_key=1234567890&ts=1234567890`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
app_key | | 我方提供给贵方的app_key
ts | | timestamp, 详细请见实例代码
token | | token, 详细请见实例代码
