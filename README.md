# adk-tool-trajectory-eval-sample

A minimal sample for evaluating an ADK agent with the `tool_trajectory_avg_score` criterion.

Article (Japanese): TODO: add Zenn URL

## Layout

```
.
├── sample_agent/         # the agent under evaluation
│   └── agent.py
└── tests/
    ├── eval_config.json  # evaluation criteria
    ├── evalsets/         # test cases
    └── test_sample_agent.py
```

## Setup

```bash
uv sync
cp .env.example .env  # fill in the values
```

## Run the evaluation

```bash
uv run pytest
```
