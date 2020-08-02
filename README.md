# Twitter Geo Tool Backend  
REST API written in Python using Flask and deployed to Heroku. Returns tweets in and around a given location (specified by coordinates) sorted by topic using the Twitter API.

## API paths

**POST /location/coordinates**
with a request body of the form:
```
{
    "latitude" : [num],
    "longitude" : [num]
}
```
**GET /topic** with a query parameter of any of the following:
```
"politics", "food", "pop culture", "technology", or "latest"
```
