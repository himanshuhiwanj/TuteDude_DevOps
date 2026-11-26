const express = require('express');
const path = require('path');

const app = express();
const port = Number(process.env.PORT) || 3000;
const flaskBackendUrl = process.env.FLASK_BACKEND_URL || 'http://127.0.0.1:5000';

app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/tasks', async (req, res) => {
	const response = await fetch(`${flaskBackendUrl}/submittodoitem`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
		body: new URLSearchParams(req.body),
	});
	res.status(response.status).json({ message: await response.text() });
});

if (require.main === module) {
	app.listen(port, () => {
		console.log(`Frontend running at http://localhost:${port}`);
	});
}

module.exports = app;
