# Sitewatcher

Currently this manually watches the RSS feed from the Zoom App Changelog page

BSRSS is not novel, and is mostly a tutorial smushed into what I wanted for this. 
BSRSS.news(url) returns a dictionary of the information in the url, check your individual RSS formatting to tailor it to other sites, 
currently it uses mostly the guid ( url ) and description

Sitewatcher reads in the known state, checks the site and compares. 
Any new posts are sent as individual emails 
Then they are written to the known state json file

the json file name is a slice of the url after the http[s]:// and not including any following /...
