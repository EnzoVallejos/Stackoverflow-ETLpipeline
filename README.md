<h1 align="center">ETL pipeline</h1>

[![license](https://img.shields.io/github/license/EnzoVallejos/Stackoverflow-ETLpipeline)](https://github.com/EnzoVallejos/Stackoverflow-ETLpipeline/blob/master/LICENSE.md)
<img src="https://www.codefactor.io/Content/badges/APlus.svg">

This repository is an example of an ETL pipeline made in Python:snake:.
The end of this pipeline is to get data, from the stackoverflow questions, their stats, etc.

The code consists of three modules:

- :page_with_curl:Extract: get html data from the page.
- :arrows_clockwise:Transform: take the html and parse it to get the text plane.
- :heavy_check_mark:Load: save this data in .csv format.
