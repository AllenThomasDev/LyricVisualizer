# LyricVisualizer
This is essentially a clone of [SongSim](https://colinmorris.github.io/SongSim/#/) which is an online tool created by [Colin Morris](https://github.com/colinmorris)

This was built entirely in Python and is hosted [here](https://lyricviz.herokuapp.com/)

It creates a self-similarity matrix using text. Using a list of words (from a song lyrics) it creates an nxn matrix where (i,j) is filled when the ith word is the same as the jth word.

This can be used to visualize lyrical themes.

<img src="https://colinmorris.github.io/SongSim/img/about/barbie.png" alt="Example" width="200"/>

##### This is an example image provided by Colin Morris on his [site](https://colinmorris.github.io/SongSim/#/)
While SongSim has a lot of features, there are some that it lacks - 
1. Users cannot 'search' for songs, they have to manually copy and paste a lyrics in case the song they want to visualize is not in the examples
1. The heatmap is static, users cannot zoom or filter 

LyricViz tries to eliminate these issues.

There is a dropdown with a few example songs as well as a 2 search options-
1. Users can search by Artist Name and Song Name
1. In case of an error they can also manually enter a url.

Currently the data is scraped from MetroLyrics, so users have to enter a metrolyrics link.

The chart is built using Dash, so it is dynamic as well as interactive. Currently,the chart is a type of a scatter chart but in coming versions it will changed to a more suitable heatmap.
