require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose')
const bodyParser = require('body-parser');
const app = express();

// Routes
const conversations = require('./routes/api/conversations');
// console.log(process.env)
app.use(
    bodyParser.urlencoded({
        extended: true
    })
);

app.use(bodyParser.json());

app.use('/api/conversations', conversations);

var port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

