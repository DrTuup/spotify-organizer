FROM astral/uv:python3.14-trixie-slim

# Copy the project into the image
COPY . /app

# Disable development dependencies
ENV UV_NO_DEV=1

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

# Run the installed package directly from the virtual environment
# Use --no-sync to prevent reinstalling dependencies on every container start
CMD ["uv", "run", "--no-sync", "spotify-organizer"]