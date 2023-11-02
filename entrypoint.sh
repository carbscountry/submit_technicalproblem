#!/bin/sh

# Check if directory exists and create if not
if [ ! -d "/workspace/output_log" ]; then
    mkdir -p /workspace/output_log && touch /workspace/output_log/out.log
fi

# Execute the main command (e.g., start your application)
exec "$@"
