## Personal Finance API


### Local Development

#### Set up Redis locally (docker desktop running)
`docker run -p 6379:6379 redis:latest`

#### Run the API
`export CONFIG_ENV_FILE=".env.local" && fastapi dev src/main.py`
