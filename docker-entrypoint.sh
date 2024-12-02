#!/bin/bash

# Run database migrations
echo "Running migrations..."
flask db upgrade

# Seed data (optional)
echo "Seeding data..."
python seed.py

# Start the Flask application
echo "Starting Flask application..."
exec "$@"