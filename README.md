## OpenAI Agents Case

A minimal example project using `openai-agents` with multiple agents, tools, and environment-based
configuration.

### Requirements

- Python 3.12+
- `uv` (optional, recommended)

### Configuration

Copy `.env.example` to `.env` (not committed) and fill in values:

```
cp .env.example .env
```

Then set:

```
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://your-base-url
OPENAI_MODEL=your-model-id
OPENAI_AGENTS_DISABLE_TRACING=true
```

### Run

```
python3 main.py
```
