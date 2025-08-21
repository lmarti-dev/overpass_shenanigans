# Using OverpassQL 

## All streets in town

To get all the streets in a given town it's pretty straightforward

```js
[out:csv("name";false)];
area[name="Erlangen"];
way(area)[highway][name];
out;
```

The query will also output all the paths, dirt roads, and back alleys. One can prevent this by specifically asking the property "highway" not to regex match -- by using the `!~` operator -- with any of those lesser ways. Note that, on top of these regex non-matches, output results are asked not to be private or inaccessible or mere footpaths. These conditions are laid in the three last lines. 
 
```js
[out:csv("name";false)];
area[name="Genève"];
(
way(area)
['name']
['highway']
['highway' !~ 'path']
['highway' !~ 'steps']
['highway' !~ 'motorway']
['highway' !~ 'motorway_link']
['highway' !~ 'raceway']
['highway' !~ 'bridleway']
['highway' !~ 'proposed']
['highway' !~ 'construction']
['highway' !~ 'elevator']
['highway' !~ 'bus_guideway']
['highway' !~ 'footway']
['highway' !~ 'cycleway']
['foot' !~ 'no']
['access' !~ 'private']
['access' !~ 'no'];
);
out;
```
It is also to discriminate between homonyms, by may rather identify the city through its wiki article:
```js
area[name="Paris"]["wikipedia"="en:Paris"];
```

## All the bars in the city

One can also list all the amenities (bars, etc.) registered by OpenStreetMaps users. It works in a way similar to the streets: instead of asking for a `way`, one looks for a `node` (a discrete point on the map), and then match the `amenity` key with one of the numerous food and drink establishment kinds. 

```js
[out:csv("name";false)];
area[name="Genève"];
node["amenity"~"pub|restaurant|biergarten|cafe|food_court|fast_food|ice_cream"](area);
out;
```

All the keys, values, and more are available in the [wiki](https://wiki.openstreetmap.org/wiki/Map_features), and there are also nifty [cheat sheets](https://osm-queries.ldodds.com/syntax-reference.html).


