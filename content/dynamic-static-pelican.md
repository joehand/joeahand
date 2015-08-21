Title: Building a Dynamic yet Static Website with Pelican & IFTTT
Slug: dynamic-site-pelican-ifttt
Date: 2015-08-08 00:00:00
Tags: pelican, python, ifttt
Category: programming
Summary: 

Static websites seem all the rage right now, and for good reason. A static site is a website that does not have a server creating pages on every request. They are easy to host (for free), fast, and help you offload all the server's work onto the computers visiting your site (d'oh!).

Static websites also have some serious downsides. Foremost, the content is static - only updated when you take action. If you want *dynamic* content on the site, you have to rely on APIs and Javascript, adding to the page size and load times. In this trade off, you are passing the work on to the user rather than doing it on the server, perhaps an unwise trade off.

Don't panic! You can have both! If you visit my [homepage](https://joeahand.com) you will notice dynamic content (twitters, fitbit steps, cups of joe drunk) - yet there are no API calls. How is this possible? It must be Magic! Not here, sorry.

The answer is Python, of course. You can [fly with Python](https://xkcd.com/353/) and make dynamic-static websites! *(You can build this with other languages, but you can't fly with them... In fact, I am flying as we speak! Probably thanks to Python.)*

### Quickstart (how I did it):

1. Set up [IFTTT](https://ifttt.com) (If This Then That) and start sending data to Google Spreadsheets ([sample recipe](https://ifttt.com/recipes/112226-save-your-tweets-in-a-google-spreadsheet)).
2. Grab the data with a custom [Pelican](http://getpelican.com) [plugin](https://github.com/joehand/joeahand/tree/master/plugins/pelican_gdocs), process it, and output to templates.
3. Make the data pretty.
4. Create a cron job to update data & regenerate site regularly (mine runs once daily).

## 1. IFTTT Awesomeness

If you haven't checked it out, IFTTT is great. When something happens (new tweet posted) IFTTT will do something else (add a row to a spreadsheet). I started using it to automatically send emails to loved ones when I arrived at airports (via check ins on FourSquare).

IFTTT also has a group of apps called DO (Button, Note, Camera). These apps skip the IF and just DO something. When I have a cup of joe, I tap the DO button on my phone to record it (unfortunately, as I just found out, this doesn't work on airplanes - remind me to record this cup of coffee I drank over Idaho).

All of my homepage data goes through IFTTT to Google spreadsheets:

* Drink Coffee > Tap Do Button > Add to Spreadsheet
* Joe Tweets > Add to Spreadsheet
* Pocket Article Archived > Add to Spreadsheet
* Instagram Picture Posted > Add to Spreadsheet
* Fitbit Daily Log > Add to Spreadsheet

Now think of the possibilities with all that data in spreadsheets! For now, let's make it into a nice dynamic-static website.

## 2. Grabbing Spreadsheet Data w/ Pelican Plugin

***Advisory:*** *We are going to start getting into some code here. I'm going to assume that you have a running [Pelican](http://getpelican.com) website. If not, check out the [Pelican getting started](http://docs.getpelican.com/en/3.6.2/quickstart.html) tutorial, it's pretty friendly.*

Once the data is in Google Docs, how do we get it out? Turns out, its quite simple. Google has an option to publish spreadsheets as csv files:

    File > Publish to Web > Publish as CSV

Now that you have a public csv, we can grab it with the great Python `requests` library, transform it into a Python object. This will all be a part of our [Pelican plugin](http://docs.getpelican.com/en/latest/plugins.html). My plugin is pretty customized (for processing the data) but you can copy the guts of it.

***Note:*** *You can hop over to [GitHub](https://github.com/joehand/joeahand) to check out the full code at any time (here is [plugin part](https://github.com/joehand/joeahand/tree/master/plugins/pelican_gdocs)).*

### Getting a Published CSV from Google

    :::python
    import requests
    response = requests.get(PUBLIC_CSV_URL)
    content = response.text

And now you have a csv in `content`. Yes, its really that easy.

### Creating Python List from CSV

Unfortunately, right now the `content` variable is just a big string of data, so it is not very useful. 

Now we will create a Python list, with each item in the list being a row of the spreadsheet. Our keys will be the spreadsheet headers.

***Note:*** *This code is for Python 3. If you aren't on 3, you should really switch.*

    :::python
    import csv
    lines = content.splitlines()
    header = [h.strip() for h in lines[0].split(',')]
    data = list(csv.DictReader(lines[1:], fieldnames=header))

Python's `csv` module makes this pretty simple. Each item in the data list is now a Python object, for example this is a row from the Instagram spreadsheet:
    
    {
        'Instagram_Link':'http://instagram/something', 
        'Photo_URL':'http://instagramcdn.com/url', 
        'Caption': 'This is a picture', 
        'Date':'June 21, 2015'
    }

Captain, we have data (I'm writing this on a plane, I apologize)!

## 3. Visualizing Data

From here, what you want to do will depend on your data and how you want to show it. The plugin will allow you to access the data in your templates and then you can let your imagination run wild!

Using Jinja, outputting to a javascript object is fairly easy. For example, here is the data output for my Fitbit steps:

    var steps_data = {
            labels: [
                {%- for row in gdocs_data.steps | reverse -%}
                   '{{row.Date}}',
                {%- endfor -%}
            ],
            series: [
                [
                {%- for row in gdocs_data.steps | reverse -%}
                    {{row.TotalSteps}},
                {%- endfor -%}
                ]
            ]
    };

The label/series organization is how Chartist.js likes data. But you can make it whatever kind of js object you like.

My coffee visualization uses a table created with Jinja loops. There are probably some other options depending on what kind of data you want to visualize.

## 4. Automatically Updating the Site

One of the biggest downsides to static sites is the fact they only update when you change the content (and then usually push the site somehow). To get around this, you need a process to run automatically on a schedule and update the website. This is exactly what [cron jobs](http://crontab.org/) are for.

Pelican also makes it fairly easy to push content with a single command (check out the make script). For my site, I use `make github` which grabs all the latest data, rebuilds the site, and pushes it to Github Pages. A similar process should work for the other `make` commands.

In my case, here is what I did:

1. Set up a [Digital Ocean server](https://www.digitalocean.com/?refcode=94657bdeab0c).
2. Clone my pelican repository.
3. Set up the `make github` command and make sure it all works manually.
4. Create a cron job to run daily (at midnight, if you must really know).
5. Profit!!?!!

The hardest part is step 3 and really depends on your server. I used a Python virtual environment but that didn't play very well with the PIL library. Safe to say, it was a pain and I recommend you not do what I did. In the case I go through this again, which is likely, I'll do a better job of documenting my steps the next time (sorry!).

## Boom - Static Dynamic Site!

So there you have it! A static dynamic site with Python! 

Let me know what you think on [Twitter](https://twitter.com/joeahand). If you want to see all the code it is on [GitHub](https://github.com/joehand/joeahand).


