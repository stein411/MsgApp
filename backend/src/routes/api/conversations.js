const express = require('express');
const router = express.Router();

router.post('/', (req, res) =>{
    console.log('post request made');
    res.send('hello world');
});

module.exports = router;