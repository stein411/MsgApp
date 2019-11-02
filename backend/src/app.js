const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Routes
const conversations = require('./routes/api/conversations');

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