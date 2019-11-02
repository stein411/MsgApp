var mongoose = require('mongoose');

var conversationSchema = new mongoose.Schema({
    id: int,
    user_ids: list
});

var Conversation = mongoose.model('Conversation', convesrationSchema);

module.exports = Conversation;