const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const multer = require('multer');
const path = require('path');
const Event = require('./models/event'); // Define Event model
const Team = require('./models/team'); // Define Team model

const app = express();
const PORT = process.env.PORT || 3000;
const MONGODB_URI = 'your_mongodb_uri_here';

// Connect to MongoDB
mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useFindAndModify: false,
    useCreateIndex: true
})
.then(() => {
    console.log('Connected to MongoDB');
})
.catch((err) => {
    console.error('Failed to connect to MongoDB:', err);
    process.exit(1);
});

// Middleware
app.use(bodyParser.json());
app.use(express.static('public'));

// Configure multer for file uploads
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/')
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + path.extname(file.originalname))
    }
});
const upload = multer({ storage: storage });

// Routes
// GET all events
app.get('/events', async (req, res) => {
    try {
        const events = await Event.find();
        res.json(events);
    } catch (err) {
        console.error('Error fetching events:', err);
        res.status(500).json({ message: 'Failed to fetch events' });
    }
});

// POST new event
app.post('/events', async (req, res) => {
    const eventData = req.body;
    try {
        const event = new Event(eventData);
        await event.save();
        res.status(201).json(event);
    } catch (err) {
        console.error('Error saving event:', err);
        res.status(500).json({ message: 'Failed to save event' });
    }
});

// POST file upload
app.post('/upload', upload.single('file'), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ success: false, message: 'No file uploaded' });
    }
    res.status(201).json({ success: true, filename: req.file.filename });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
const mongoose = require('mongoose');

const teamMemberSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    team: {
        type: String,
        required: true,
        enum: ['IT', 'Marketing']
    }
});

module.exports = mongoose.model('TeamMember', teamMemberSchema);
