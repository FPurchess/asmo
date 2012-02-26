<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;utf-8">
    <title>asmo - arduino serial monitor online</title>

    <link rel="stylesheet" type="text/css" href="/static/style.css">

    <script type="text/javascript" src="/static/jquery-1.7.1.min.js"></script>
    <script type="text/javascript" src="/static/script.js"></script>
</head>
<body>
%if not init:
<div class="warning">Warning: Serial Connection has not be established!</div>
%end
<form method="post" action="/">
    <label for="serial">Serial Command:</label>
    <input id="serial" type="text" name="serial" value="">
</form>
<pre></pre>
<p>&copy; asmo - arduino serial monitor online; 2012 Florian Purchess</p>
</body>
</html>