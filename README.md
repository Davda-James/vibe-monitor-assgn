### Setting up the project
#### Clone the repo
```bash
git clone https://github.com/Davda-James/vibe-monitor-assgn.git
```

#### Installing dependencies
Make sure uv package manager is installed, if not install it from here: [Installation](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

```bash
cd vibe-monitor-assgn
```

```bash
uv sync
```

#### Run the fastapi server

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 
```

### Running the prometheus and grafana 
```bash
cd prometheus-grafana
```

Make sure to install if you do not have docker and docker compose
```bash
docker compose up
```

#### !! Good to GO !!