require('dotenv').config()// import dotenv
const configViewEngine = require('./config/viewEngine');
const express = require('express')// common js import express

const app = express() // app express
const port = process.env.PORT || 8888;// port => hardcode 
const webRoutes = require('./routes/web')

// config template engine
configViewEngine(app);
//Khai báo route
app.use('',webRoutes);
//log
app.listen(port, () => {
    console.log(`Example app listening on port http://localhost:${port}`)
})