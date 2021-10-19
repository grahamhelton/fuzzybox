# What is this?
Fuzzy box is a quick program I wrote to fuzz a URL that is in the format https://\<url\>/20characterstring.\<extension\>. I have redacted the URL.

If the http response is 200, a file will be created with the link to the URL that returned the 200 resposne.

# Example
A Quick demo of what this looks like once you fill out the `base` and `extension` variable 
![](/fuzzybox.gif)
