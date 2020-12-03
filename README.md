# aoc-downloader
Grab your input data for Advent of Code!

### setup
Simply log into AoC, and use Chrome Devtools to grab your session cookie.
1. Go to the "Application" tab in Devtools
2. Click on "Cookies" on the left panel
3. Open cookies for the AoC website, and copy the value for "session" into the SESSION_TOKEN variable in the input.py file

You can now import the `data` function from `input.py` into your code, and pass in the day you wish to download input for!

### Example:
```python3
import input

day1_raw = input.data(1).text
```
This will pull in the data as raw text, so you'll need to do some parsing to get the data into the format you need. For day one where the data is a in list, delimited by newlines we can just split the data and run a quick list comp to get the data as a numerical list:
```python3
day1_data = [ int(s) for s in day1_raw.strip().split('\n') ]
```

Dependencies:
`requests` library. Install using:
```
python -m pip install requests
```

