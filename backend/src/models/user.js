var mongoose = require('mongoose');

var userSchema = new mongoose.Schema({
    name: String,
    password: String,
    id: int
});

//need to create join conversation method?
userSchema.methods.send = function () {
}

var User = mongoose.model('User', userSchema);

module.exports = User;