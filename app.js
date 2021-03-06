var express = require("express");
var app = express();
var port = 3000;
 
app.set('views', __dirname + '/views');
app.set('view engine', "jade");
app.engine('jade', require('jade').__express);
app.get("/", function(req, res){
    res.render("index.jade");
});
app.use(express.static(__dirname + '/public'));

app.listen(port);
console.log("Listening on port " + port);