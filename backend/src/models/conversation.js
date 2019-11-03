var mongoose = require('mongoose');
var Schema = mongoose.Schema;
// var connection = mongoose.createConnection("mongodb://localhost/test");
// var autoIncrement = require('mongoose-auto-increment');
// autoIncrement.initialize(connection);
var conversationSchema = new mongoose.Schema({
    id: Number,
    user_ids: Array
});

// conversationSchema.plugin(autoIncrement.plugin, 'Conversation');
var Conversation = mongoose.model('Conversation', conversationSchema);

module.exports = Conversation;