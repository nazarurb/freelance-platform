#!/bin/bash

DB_NAME="freelance_platform"
DB_USER="melnyk"

echo "🚀 Setting up the database..."

psql -U $DB_USER -h localhost -p 5432 -c "DROP DATABASE IF EXISTS $DB_NAME;"

psql -U $DB_USER -h localhost -p 5432 -c "CREATE DATABASE $DB_NAME;"

psql -U $DB_USER -h localhost -p 5432 -d $DB_NAME -f app/database/backup.sql

echo "✅ Database setup complete!"
