const mongoose = require('mongoose');
const url = process.env.MONGODB_URI 
mongoose.connect(url, {useNewUrlParser: true});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
    //connected!
});

// var connection = mongoose.createConnection("mongodb://localhost/test");
// var autoIncrement = require('mongoose-auto-increment');
// autoIncrement.initialize(connection);
