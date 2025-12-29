from dotenv import load_dotenv

load_dotenv()

import logging
import os

from agents import Agent, OpenAIProvider, RunConfig, Runner, function_tool

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

MODEL_NAME = os.getenv("OPENAI_MODEL")


@function_tool(strict_mode=False)
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


@function_tool(strict_mode=False)
def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


calc_agent = Agent(
    name="Calculator",
    instructions="You are a calculator. Use tools and return only the final number.",
    model=MODEL_NAME,
    tools=[add, multiply],
)

writer_agent = Agent(
    name="Writer",
    instructions="Use one short Chinese sentence to explain the calculation result.",
    model=MODEL_NAME,
)

run_config = RunConfig(model_provider=OpenAIProvider(use_responses=False))
calc_result = Runner.run_sync(calc_agent, "Please compute (12 + 30) * 2.", run_config=run_config)
explain_result = Runner.run_sync(
    writer_agent,
    f"The result is {calc_result.final_output}. Explain the steps in one short sentence.",
    run_config=run_config,
)
logger.info("Result: %s", calc_result.final_output)
logger.info("Explanation: %s", explain_result.final_output)
