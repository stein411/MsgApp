var mongoose = require('mongoose');
var autoIncrement = require('../routes/api/db_connection');

var messageSchema = new mongoose.Schema({
    id: Number,
    conv_id: Number,
    timestamp: Date,
    author_id: String
});

messageSchema.plugin(autoIncrement.plugin, 'Message');
var Message = mongoose.model('Message', messageSchema);

module.exports = Message;