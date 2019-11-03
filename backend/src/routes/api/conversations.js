const express = require('express');
const router = express.Router();
require('./db_connection');
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