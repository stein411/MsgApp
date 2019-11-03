const express = require('express');
const router = express.Router();
require('./db_connection');
var convo = require("../../models/user.js");
router.post('/', (req, res) => {
    console.log('post request made');
    convo.create({
        name: req.body.name
        // TODO do password stuff
    }, function (err, doc) {
        if (err) {
            return res.send(err)
        }
        return res.send(doc); // TODO just send id
    });
    
});
router.get('/', (req, res) => {
    if (typeof req.query.name !== 'undefined') {
        convo.findOne({name: req.query.name}, (err, doc) => {
            if (err) {
                return res.send(err);
            }
            return res.send(doc);
        })
    } else if (typeof req.query.id !== 'undefined') {
        convo.findById(req.query.id, (err, doc) => {
            if (err) {
                return res.send(err);
            }
            return res.send(doc);
        })
    }
 })

module.exports = router;