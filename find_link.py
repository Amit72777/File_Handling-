
# find a link in txt file 

with open("index.html","r") as web :    # open index.html file in read mode 
    with open("output.txt","a") as link: # open output.txt file in append mode 
        for line in web.readlines():
            # append a link in a new file 
            if "<a" in line :  
                first_quote = line.find('\"')
                second_quote = line.find("\"",first_quote+1)
                link.write ( line[first_quote +1 : second_quote] + '\n ')


'''   index.html content 
index.html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-US-Compatible " content=" IE-edge">
    <title> Page title </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta rel = 'stylesheet' type = "text/css" media = "screet" href = "main.css" />
    <script src = "main.js" > </script>
    <title></title>
</head>
<body>
    <h1>Hi there I'm Amit Kushwaha      </h1>
    <a href="https://www.facebook.com" target="_blank"> Click to open facebook </a>
    <br>
    <a href = "https://www.youtube.com" target="_blank"> youtube</a>
    <br>
    <a href="https://www.twitter.com" target=" _blank ">twitter</a>
    <br>
    <a href="https://www.google.com" target="_blank"> Go to Goolgle</a>

</body>
</html>

'''

'''
Output.txt content 
https://www.facebook.com
 https://www.youtube.com
 https://www.twitter.com
 https://www.google.com
 

'''