var mongoose = require('mongoose');

var messageSchema = new mongoose.Schema({
    id: int,
    conv_id: int,
    timestamp: Date,
    author_id: String
});

var Message = mongoose.model('Message', messageSchema);

module.exports = Message;