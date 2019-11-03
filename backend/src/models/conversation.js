var mongoose = require('mongoose');
var autoIncrement = require('../routes/api/db_connection');
var conversationSchema = new mongoose.Schema({
    id: Number,
    user_ids: Array
});

conversationSchema.plugin(autoIncrement.plugin, 'Conversation');
var Conversation = mongoose.model('Conversation', conversationSchema);
module.exports = Conversation;