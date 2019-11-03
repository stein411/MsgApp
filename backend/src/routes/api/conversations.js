const express = require('express');
const router = express.Router();
require('./db_connection');
var convo = require("../../models/conversation.js");
router.post('/', (req, res) => {
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
router.get('/', (req, res) => {
    if (typeof req.query.user_id1 !== 'undefined') {
        if (typeof req.query.user_id2 !== 'undefined') {
            convo.findOne({user_ids: [req.query.user_id1, req.query.user_id2]}, (err, doc) => {
                if (err) {
                    return res.send(err);
                }
                return res.send(doc);
            });
        } else {
            convo.find({user_ids: req.query.user_id1}, (err, docs) => {
                if (err) {
                    return res.send(err);
                }
                return res.send(docs);
            });
        }
    }
})

module.exports = router;