Title: Filtering a Shapefile with Python
Slug: filtering-a-shapefile-with-python
Date: 2015-08-11 19:39:12
Tags: python, spatial, data
Category: programming
Summary: 
    
Recently I've been using Python more to work with shapefiles. Frequently I have to create a shapefile by filtering a set of features of a larger shapefile, for instance I wanted to get a shapefile for blocks in New York City from a shapefile of the whole country. While this isn't very difficult in QGIS (and probably ArcGIS), it gets a bit annoying to do over and over. In the last project, I wanted to create files for over 900 cities in the US - so I definitely wasn't going to do that by hand.

### Quickstart 

I'll walk through the three main steps to do this in Python:

1. Creating a shapefile when `my_field = my_value` from a large shapefile.
2. Finding all values in `my_field` from your large shapefile.
3. Putting 1 & 2 together to create many shapefiles for every value in `my_field`.

*** If you want to see how it all comes together, [see the full code here](https://gist.github.com/joehand/498a1656e028c6163aa9).***

There are a few Python-based shapefile libraries. The most extensive is [GDAL](http://www.gdal.org/) with [Python bindings](https://pypi.python.org/pypi/GDAL/). I decided to use GDAL because of the speed (some of the other libraries are pure Python, thus slower). The only downside is that it can be a pain to install (especially in a virtual environment).

### Command Line Filtering

If you want to filter a shapefile by a specific field/value OGR has a attribute filter function. If you just need to do this once, I recommend using the command line:

    :::bash
    ogr2ogr -f "ESRI Shapefile" -where \
        "my_field = some_value" new_shapefile.shp source_shapefile.shp

But I needed to filter many times and in the context of another program, so let's look at the Python version of this command.

## Creating a Single Shapefile for a Known Filter Value

In this case, we know our field and know the value we want to filter. We just need to create a single shapefile from the larger one. First, we will open our larger input file and use OGR's filter function to get the filtered features. Then we can create a new shapefile by copying the filtered input file:

    :::python
    from osgeo import ogr

    def create_filtered_shapefile(value, filter_field, in_shapefile):
        input_layer = ogr.Open(in_shapefile).GetLayer()
        out_shapefile = 'out_shapefile.shp'

        # Filter by our query
        query_str = '"{}" = "{}"'.format(filter_field, value)
        input_layer.SetAttributeFilter(query_str)

        # Copy Filtered Layer and Output File
        driver = ogr.GetDriverByName('ESRI Shapefile')
        out_ds = driver.CreateDataSource(out_shapefile)
        out_layer = out_ds.CopyLayer(input_layer, str(value))
        del input_layer, out_layer, out_ds
        return out_shapefile       

Great! We have a filtered shapefile. But what if we want to do this for every value in some field? 

## Getting All Values for a Field

If we want to create a shapefile for each value in some field, first we need to figure out all the values for `my_field`. Luckily, OGR allows you to execute SQL queries on the shapefiles. So we can get our values with some simple SQL: `SELECT DISTINCT 'my_field' FROM 'my_shapefile'`. And putting it in a function:

    :::python
    def get_unique_values(filter_field, in_shapefile):
        """ Return unique values of filter from source shapefile.
        """
        sql = 'SELECT DISTINCT "{}" FROM {}'.format(
            filter_field, in_shapefile)
        layer = ogr.Open(in_shapefile).ExecuteSQL(sql)
        values = []
        # Unfortunately, you have to loop
        # over every feature to get the values. 
        # This seems common in dealing w/ Shapefiles
        for feature in layer:
            values.append(feature.GetField(0))
        return values 

## Creating Many Filtered Shapefiles

Finally, we will put the last two functions together with a loop. First, we  get all the possible values from some field and then loop over the values and create a shapefile for each one. This can be pretty slow depending on how many shapefiles you need to create. 

    :::python
    def create_all_shapefiles(filter_field, in_shapefile):
        """ Returns list of new shapefiles
            Creates shapefiles for filtered data
        """
        out_files = []
        values = get_unique_values(filter_field, in_shapefile)
        for val in values:
            out_file = '{}.shp'.format(val)
            if os.path.isfile(out_file):
                # Don't overwrite existing files
                pass
            else:
                out_file = create_filtered_shapefile(val, filter_field, in_shapefile)
            out_files.append(out_file)
        return out_files

That's it! We now have a shapefile for each value in `my_field`. I've written this up as a full Python `class` you can plug into your own projects. ***[Check that code out here](https://gist.github.com/joehand/498a1656e028c6163aa9).***

Let me know if you have questions or found this useful! You can [find me on Twitter](http://twitter.com/joeahand).