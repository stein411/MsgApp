var mongoose = require('mongoose');
var autoIncrement = require('../routes/api/db_connection');
var userSchema = new mongoose.Schema({
    name: String,
    password: String,
    id: Number
});

userSchema.plugin(autoIncrement.plugin, 'User');

var User = mongoose.model('User', userSchema);

module.exports = User;