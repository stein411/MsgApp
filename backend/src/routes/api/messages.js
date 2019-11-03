const express = require('express');
const router = express.Router();
require('./db_connection');
var msg = require("../../models/message");
router.post('/', (req, res) => {
    console.log('post request made');
    msg.create({
        author_id: req.body.author_id,
        conv_id: req.body.conv_id,
        timestamp: req.body.timestamp
    }, function (err, doc) {
        if (err) {
            return res.send(err)
        }
        return res.send(doc);
    });
});

module.exports = router;