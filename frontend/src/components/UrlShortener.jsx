import React, { useState } from 'react';
import { motion } from 'framer-motion';
import '../styles/app.css';

const UrlShortener = () => {
    const [url, setUrl] = useState('');
    const [shortUrl, setShortUrl] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setShortUrl('');
        setLoading(true);

        try {
            const response = await fetch('http://127.0.0.1:5000/shorten', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url })
            });

            const data = await response.json();
            setLoading(false);

            if (response.ok) {
                setShortUrl(data.short_url);
            } else {
                setError(data.error || 'Something went wrong!');
            }
        } catch (err) {
            setLoading(false);
            setError('Server not reachable!');
        }
    };

    return (
        <motion.div
            className="container"
            initial={{ opacity: 0, y: -50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
        >
            <h1>URL Shortener</h1>
            <form onSubmit={handleSubmit}>
                <input 
                    type="url" 
                    placeholder="Enter your URL here" 
                    value={url} 
                    onChange={(e) => setUrl(e.target.value)} 
                    required 
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Shortening...' : 'Shorten URL'}
                </button>
            </form>

            {error && <p className="error-message">{error}</p>}
            {shortUrl && (
                <div className="shortened-list">
                    <div className="shortened-item">
                        <span>Your Short URL:</span>
                        <a href={shortUrl} target="_blank" rel="noopener noreferrer">{shortUrl}</a>
                    </div>
                </div>
            )}
        </motion.div>
    );
};

export default UrlShortener;