
const express = require('express');
const index = require('./index');
var app = express();

app.get("/",(req,res)=>{index.handler(req,res);});
app.listen(3001,()=>{console.log("server is up");})