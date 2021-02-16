#!C:\Users\Preetha\AppData\Local\Programs\Python\Python39\python

print("Content-Type: text/html\n")
def glucose():
    return 112

def temp():
    return 96

def diabetes():
    return 250

str1=(
    """<!DOCTYPE html> 

            <html>

                <head>
                    <style>
                    .content{
                    margin-top:1px;
                    height:750px;
                    background-color: white;
                    }

                    .body{
                    width=100%;
                    margin-top=0px;
                    padding-top=0px;
                    }

                    table{
                    border: 1px solid black;
                    background-color: skyblue;
                    }

                    </style>
                    
                </head>

            <body>

            <script language="javascript" type="text/javascript" 
            src="header.txt">
            </script>
            <script language="javascript" type="text/javascript" 
            src="nav.txt">
            </script>
             
            <div class="content">
            <br><br><br>
            <h1 font-style="bold" align="center">HEALTH STATUS</h1><br><br>  
            
            <div align="center">
            <form action="" method="post">
            <input type="text" value= glucose><input type="text" value= """ + str(glucose()) + "></br></br>"
            + """<input type="text" value= temperature ><input type="text" value= """ + str(temp()) +"></br></br>" 
            + """<input type="text" value= diabetes ><input type="text" value= """ + str(diabetes()) +"></br></br>" 
            + """</div></div></form>
            <script language="javascript" type="text/javascript" 
            src="footer.txt">
            </script>
            </body></html>"""

)

hs = open("UI_medikit.html", 'w')
hs.write(str1)

# str1_new = "hello"
# hs = open("UI_medikit_1.html", 'w')
# hs.write(str1_new)

print(str1)


