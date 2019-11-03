
const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');

// var connection = mongoose.createConnection("mongodb://localhost/test");
// var autoIncrement = require('mongoose-auto-increment');
// autoIncrement.initialize(connection);

const url = process.env.MONGODB_URI 
mongoose.connect(url, {useNewUrlParser: true});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
    //connected!
});
var convo = require("../../models/conversation.js");
router.post('/', (req, res) =>{
    console.log('post request made');
    convo.create({
        
        user_ids: req.body.user_ids  
    
    }, function (err, doc) {
        if (err) {
            return res.send(err)
        }
        return res.send(doc);
    });
    
});

module.exports = router;