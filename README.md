## References
---

### fips
* [national_county.txt](
https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt) - list of state and county fips
* [2018 FIPS Codes](
https://www.census.gov/geographies/reference-files/2018/demo/popest/2018-fips.html) - contains lists of geocodes
    * download `all-geocodes-v2018.xlsx` from here
    * convert to CSV using Pandas (see `convert_xlsx_to_csv.py`)
    * delete the first four lines, consisting of the following:
```
Estimates Geography File: Vintage 2018,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
"Source: U.S. Census Bureau, Population Division",,,,,,
Internet Release Date: May 2019,,,,,,
,,,,,,
```
First file with FIPS: 60th in the list

### Saving images
* [Static Image Export in Python](https://plotly.com/python/static-image-export/)
    1. `$ npm install -g electron@1.8.4 orca`
    2. `$ poetry add psutil`

### Creating animated GIFs
* ImageMagick (standalone application): [How to Make Gifs Using Python](
http://superfluoussextant.com/making-gifs-with-python)
* PIL (slower than OpenCV): [Png to Gif](https://pythonprogramming.altervista.org/png-to-gif/)
* OpenCV (doesn't create animated GIFs): [Creating GIFs with OpenCV](
https://www.pyimagesearch.com/2018/11/05/creating-gifs-with-opencv/)
* imageio (built on top of PIL): 
    * [Create Animated Images Using Python](https://medium.com/swlh/python-animated-images-6a85b9b68f86)
    * [Programmatically generate video or animated GIF in Python?](
    https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python)

To figure out possible parameters for plotly, try entering a bogus one, like `legend_order='reverse'` (this one for 
`fig.update_layout()`), and the console error message will show a list of available parameters (more than the help, 
I think).

## Data issues
---

### Duplicate fips
Sample file: `03-24-2020.csv`
Errant data:
```csv
32007,Elko,Nevada,US,2020-03-24 23:37:31,41.14531606,-115.3577619,0,0,0,0,"Elko, Nevada, US"
32007,Elko County,Nevada,US,2020-03-24 23:37:31,41.14531606,-115.3577619,2,0,0,0,"Elko County, Nevada, US"
35013,Dona Ana,New Mexico,US,2020-03-24 23:37:31,32.35275771,-106.8329387,13,0,0,0,"Dona Ana,New Mexico,US"
35013,Doña Ana,New Mexico,US,2020-03-24 23:37:31,32.35275771,-106.83293870000001,0,0,0,0,"Doña Ana, New Mexico, US"
```

Queries to find duplicates:
```python
# place at end of `validate_data()`
series = df['fips']
print(series.duplicated().any())
# prints: True
if series.duplicated().any():
    duplicates = series[series.duplicated()].unique()
    print(duplicates)
# prints: ['35013' '32007']
print(df[series == '35013'])
# prints:
#       fips  confirmed  deaths        date confirmed_bins deaths_bins
# 798  35013         13       0  03-24-2020              2           0
# 818  35013          0       0  03-24-2020              0           0
```

## Plotly
---
 
layout.title.xref='container' refers to the "entire width of the plot", meaning the width of the PNG itself.
layout.title.xref='paper' refers to "the width of the plotting area only", i.e., the box containing the map.

## Watchdog
* [Watching a directory for file changes with Python](http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html)
* [How to create a watchdog in Python to look for filesystem changes](http://thepythoncorner.com/dev/how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/)

## Speed
---

### Downloading files

Downloading files is I/O-Bound, so using `asyncio` seemed a good choice for obtaining some easy speed gains.  I tested 
this in late April or early May (90+ files) by measuring the time required to download all available files.

Summary of results (all trials in seconds, ascending order)

Method | Trial 1 | Trial 2 | Trial 3 | Trial 4 | Trial 5 | Trial 6
------ | ------- | ------- | ------- | ------- | ------- | -------
synchronous | 23 | 25 | 26 | 34 | 35 | 
asynchronous, using `asyncio` | 2 | 4 | 4 | 5 | 12 | 40
asynchronous, using `asyncio` and `aiofiles` to write files | 3 | 4 | 5 | 11 | | 

### Future optimizations

Assume a file of the form MM-DD-YYYY.csv is available and download it and all previous ones (to 01-22-2020) without
retrieving the index first.

updates on https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
 <time-ago datetime="2020-04-16T16:09:49Z" class="no-wrap" title="Apr 16, 2020, 9:09 AM PDT">23 days ago</time-ago>
 
 I tried the npm electron first
 then
 
 $ conda install -c plotly plotly-orca
 https://github.com/plotly/orca/issues/269
 $ sudo codesign --force --deep --sign - /Users/acetone/miniconda3/lib/orca.app
 $ sudo codesign --force --deep --sign - /Users/acetone/miniconda3/pkgs/plotly-orca-1.3.1-1/lib/orca.app
 
 1 file single processor: 10.111267805099487 seconds
 53 files single processor: 252.75397300720215 seconds
 manual: 1 file multiple processors: 9.606199026107788 seconds
 manual: 53 files multiple processors: 92 s
 subprocess: 59 files multiple processors: 160.9226689338684 s
 manual: 56 files multiple processors: 195.0839967727661 s
 manual: 59 files multiple processors: 85.35867428779602 s
