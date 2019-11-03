const express = require('express');
const router = express.Router();
require('./db_connection');
var msg = require("../../models/message");
router.post('/', (req, res) => {
    console.log('post request made');
    msg.create({
        author_id: req.body.author_id,
        conv_id: req.body.conv_id,
        timestamp: req.body.timestamp,
        content: req.body.content
    }, function (err, doc) {
        if (err) {
            return res.send(err)
        }
        return res.send(doc);
    });
});

router.get('/', (req, res) => {
    if (typeof req.query.conv_id !== 'undefined') {
        msg.find({conv_id: req.query.conv_id}, (err, docs) => {
            if (err) {
                return res.send(err);
            }
            return res.send(docs);
        });
    }
});

module.exports = router;