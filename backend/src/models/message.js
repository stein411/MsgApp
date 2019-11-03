var mongoose = require('mongoose');
var autoIncrement = require('../routes/api/db_connection');

var messageSchema = new mongoose.Schema({
    id: int,
    conv_id: int,
    timestamp: Date,
    author_id: String
});

messageSchema.plugin(autoIncrement.plugin, 'Message');
var Message = mongoose.model('Message', messageSchema);

module.exports = Message;