const mongoose = require('mongoose');
const url = process.env.MONGODB_URI 
mongoose.connect(url, {useNewUrlParser: true, useUnifiedTopology: true});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
    //connected!
});
var autoIncrement = require('mongoose-auto-increment');
autoIncrement.initialize(db);

module.exports = autoIncrement;