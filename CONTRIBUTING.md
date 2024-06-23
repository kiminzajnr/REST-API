# CONTRIBUTING

# Build the image
```
docker build -t IMAGE_NAME .
```
# Run the Dockerfile locally


```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"
```

# Common errors when using docker
`Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5000 -> 0.0.0.0:0: listen tcp 0.0.0.0:5000: bind: address already in use.`

- Use another port:
    - `docker run -dp 5005:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"`
- Or, kill process running on the port if not needed:
    - Run `lsof -i :5000` and note the `PID`
    - Run `kill -9 PID` - `PID` obtained from above

`docker: Cannot connect to the Docker daemon at ... docker.sock. Is the docker daemon running?.`
- If on macOS/Windows run docker desktop.
- On Linux start docker service.