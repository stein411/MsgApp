require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose')
const bodyParser = require('body-parser');
const app = express();

// Routes
const conversations = require('./routes/api/conversations');
const messages = require('./routes/api/messages');
const users = require('./routes/api/users');
// console.log(process.env)
app.use(
    bodyParser.urlencoded({
        extended: true
    })
);

app.use(bodyParser.json());

app.use('/api/conversations', conversations);
app.use('/api/messages', messages);
app.use('/api/users', users);

var port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

