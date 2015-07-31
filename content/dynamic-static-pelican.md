Title: Dynamic Static Website with Pelican & IFTTT
Slug: dynamic-site-pelican-ifttt
Date: 2015-07-31 08:58:30
Tags: pelican, python, ifttt
Category: programming
Summary: 

Static websites seem all the rage right now, and for good reason. A static site is a website that does not have a server creating pages on every request. They are easy to host (for free), fast, and help avoid page bloat you often see on websites today.

However, there are downsides to having a static website. Foremost, the content is static - only updated when you take action. If you want *dynamic* content on the site, you have to rely on APIs and Javascript, adding to the page size and load times. In this tradeoff, you are passing the work on to the user rather than doing it on the server, perhaps an unwise tradeoff.

Don't panic! You can have both! If you visit my [homepage](/) you will notice dynamic content - yet there are no API calls. How is this possible? 

Python, of course. You can [fly with Python](http://xkcd.com/python) and make dynamic-static websites! *(You can build this with other languages, but you can't fly with them...)*

### Quickstart (how I did it):

1. Set up [IFTTT](https://ifttt.com) (If This Then That) and start sending data to Google Spreadsheets ([sample recipie](https://ifttt.com/)).
2. Grab the data with a [Pelican](http://getpelican.com) plugin.
3. Process data, add to html template, and make it pretty.
4. Create a cron job to update data & regenerate site regularly (mine runs once daily).

## IFTTT Awesomeness

If you haven't checked it out, IFTTT is great. When something happens (new tweet posted) IFTTT will do something else (add a row to a spreadsheet). I started using it to automatically send emails to loved ones when I arrived at airports (via checking in on FourSquare).

IFTTT also has a group of apps called DO (Button, Note, Camera). These apps skip the IF and just DO something. When I have a cup of joe, I tap the DO button on my phone to record it (unfortunately, as I just found out, this doesn't work on airplanes - remind me to record this cup of coffee I drank over Idaho).

All of my homepage data goes through IFTTT to Google spreadsheets:

* Drink Coffee > Tap Do Button > Add to Spreadsheet
* Joe Tweets > Add to Spreadsheet
* Pocket Article Archived > Add to Spreadsheet
* Instagram Picture Posted > Add to Spreadsheet
* Fitbit Daily Log > Add to Spreadsheet

Now think of the possibilities with all that data in spreadsheets! For now, let's make it into a nice dynamic-static website.

## Grabbing Spreadsheet Data w/ Pelican Plugin

***Advisory:*** *We are going to start getting into some code here. I'm going to assume that you have a running [Pelican](http://getpelican.com) website. If not, check out the [Pelican getting started](http://getpelican.com) tutorial, it's pretty friendly.*

Once the data is in Google Docs, how do we get it out? Turns out, its quite simple. Google has an option to publish spreadsheets as csv files:

    File > Publish to Web > Publish as CSV (note: check this)

Now that you have a public csv, we can grab it with the great Python `requests` library, transform it into a Python object. This will all be a part of our [Pelican plugin](http://docs.getpelican.com/en/latest/plugins.html). My plugin is pretty customized (for processing the data) but you can copy the guts of it.

***Note:*** *You can hop over to [GitHub](https://github.com/joehand/joeahand) to check out the full code at any time (here is [plugin part](https://github.com/joehand/joeahand/tree/master/plugins/pelican_gdocs)).*

### Getting a Published CSV from Google

    import requests
    response = requests.get(PUBLIC_CSV_URL)
    content = response.text

And now you have a csv in `content`. Yes, its really that easy.

### Creating Python List from CSV

Unfortunately, right now the `content` variable is just a big string of data, so it is not very useful. 

Now we will create a Python list, with each item in the list being a row of the spreadsheet. Our keys will be the spreadsheet headers.

***Note:*** *This code is for Python 3. If you aren't on 3, you should really switch already.*

    import csv
    lines = content.splitlines() # Create a list item for each line
    header = [h.strip() for h in lines[0].split(',')]
    data = list(csv.DictReader(lines[1:], fieldnames=header))

Python's `csv` module makes this pretty simple. Each item in the data list is now a object, for example:
    
    {
        'Instagram_Link':'http://instagram/something', 
        'Photo_URL':'http://instagramcdn.com/url', 
        'Caption': 'This is a picture', 
        'Date':'June 21, 2015'
    }

Captain, we have data (I'm writing this on a plane, I apologize)!

## Visualizing Data

From here, what you want to do will depend on your data and how you want to show it. The plugin will allow you to access the data in your templates and then you can let your imagination run wild!

(stuff about putting in templates).

## Automatically Updating the Site