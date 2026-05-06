from google.adk.evaluation.agent_evaluator import AgentEvaluator
from google.adk.evaluation.eval_config import EvalConfig
from google.adk.evaluation.eval_set import EvalSet
import pytest


@pytest.mark.asyncio
async def test_weather_agent():
    with open("tests/evalsets/basic.evalset.json", "r") as f:
        eval_set = EvalSet.model_validate_json(f.read())
    
    with open("tests/eval_config.json", "r") as f:
        eval_config = EvalConfig.model_validate_json(f.read())

    await AgentEvaluator.evaluate_eval_set(
        agent_module="sample_agent",
        eval_set=eval_set,
        eval_config=eval_config,
    )
