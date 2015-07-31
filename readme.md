**A dynamic static website running on Pelican (Python) with data visualizations via IFTTT/GoogleDocs.**

## Intro

This site runs on [Pelican](http://docs.getpelican.com), a Python powered static site generator. It is served on GitHub Pages, via [CloudFare](https://www.cloudflare.com/) ([with easy & free SSL](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/)).

**Homepage**: The hompage content changes regularly. The data is stored in Google Docs (via [IFTTT](http://ifttt.com), [this tutorial](http://jlord.us/blog/your-own-instagram.html), and [a custom Pelican plugin](https://github.com/joehand/joeahand/tree/master/plugins/pelican_gdocs)). Data is processed on my server (or computer). I have a cron job to generate the site daily.

![Coffee Drinking Chart](https://dl.dropboxusercontent.com/u/34000599/imgs/coffee_chart.png "Coffee Drinking")

**Charts**: Coffee chart is made using a `<table>`, CSS, and lots of Joe. Daily Steps chart is made with the [Chartist.js](http://gionkunz.github.io/chartist-js/index.html) library.

**Design**: The Fonts are Garamond and Open Sans, served from Google. I used [Pure CSS](http://purecss.io/layouts/) as my css foundation.

## Data Gathering

All of my data comes through Google Spreadsheets. The plugin (`pelican_gdocs`) handles all of the data (and cleans/organizes it).

1. Set Up [IFTTT](http://ifttt.com). You can send your tweets to a google spreadsheet using [this recipe](https://ifttt.com/recipes/112226-save-your-tweets-in-a-google-spreadsheet). Check out other recipies. My coffee chart is done using the [Do Button App](https://ifttt.com/products/do/button), which adds a coffee button to my phone's homescreen.
2. Gather your spreadsheets!
3. Use plugin to clean and organize your data & jinja to format it. 

## Development

Interesting in using this site to make something of your own? Great! Feel free to open an issue if you have a question.

Things you'll need (not in this order):

* Python
* Pelican
* A Computer

You can copy my theme, but it will break without the GDocs plugin as well.

## Resources & Thanks

* [Pelican](http://docs.getpelican.com)
* [Pure CSS](http://purecss.io/)
* [Chartist](http://gionkunz.github.io/chartist-js/index.html)
* [JLord - Your Own Instagram](http://jlord.us/blog/your-own-instagram.html)
* [CodePen Thing](http://codepen.io/hackthevoid/pen/AIoba/)
* [Google Fonts](https://www.google.com/fonts)
* [SSL w/ GitHub Pages & Cloudfare](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/)


