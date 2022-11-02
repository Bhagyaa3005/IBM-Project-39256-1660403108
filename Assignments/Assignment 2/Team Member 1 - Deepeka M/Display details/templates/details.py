<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            body{
                display:flex;
                justify-content:center;
                align-items:center;
                flex-direction:column;
            }
            form{
                display:flex;
                flex-direction:column;
                justify-content:center;
                align-items:center;
                padding:20px;
                border:1px solid black;
            }
            header{
                font-size:30px;
                padding:10px;
            }
        </style>
    </head>
    <body>

        <form action="/display" method="POST">
            <header>Details<hr></header>
            <div>
                <label>Name : </label><br><br>
                <input name="name" id="name" type="text" />
            </div><br>
            <div>
                <label>Email ID :</label><br><br>
                <input name="email" id="email" type="text" />
            </div><br>
            <div>
                <label>Phone Number : </label><br><br>
                <input name="phone" id="phone" type="text" />
            </div><br>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
