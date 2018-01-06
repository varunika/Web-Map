# Web-Map
Web map created using Python and Folium

In this post, I demonstrate the use of the Python package Folium to create a web map from a GeoJson data frame. Folium is built on the Leaflet javascript library, which is a great tool for creating interactive web maps.
The goal of this post is to demonstrate how Python and Folium make it really easy to create functional and visually appealing web maps.
In this example, I plot the point locations of volcanoes in the USA (since I could manage to obtain data only for US), overlaid on a Polygon layer of Population Density. Viewing these two layers together on a web map creates a nice way to get an overall sense of population and volcano distribution, while also being able to view individual information about population and volcanoes separately.

SCREEN SHOT :
https://user-images.githubusercontent.com/15067597/34639783-82bbf4c0-f30c-11e7-8f0c-1cc88072478b.PNG

The colors in the above screen shot indicate the following:
Red : high population density
Orange: medium population density
Green: low population density
