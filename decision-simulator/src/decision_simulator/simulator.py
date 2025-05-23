from typing import List, Dict, Any
from fast_agent import Agent


class DecisionSimulator:
    """Simulates decision outcomes using fast-agent."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.agent = Agent(
            model="gpt-3.5-turbo",
            system_prompt="You are a decision outcome simulator. Given a scenario, analyze potential decisions and their likely outcomes.",
        )

    def simulate(self, scenario: str, iterations: int = 1) -> List[Dict[str, Any]]:
        """
        Simulate decision outcomes for a given scenario.

        Args:
            scenario: The decision scenario to simulate
            iterations: Number of simulation iterations

        Returns:
            List of simulation results
        """
        results = []

        for _ in range(iterations):
            prompt = f"""
            Scenario: {scenario}
            
            Please analyze this scenario and provide:
            1. A recommended decision
            2. The likely outcome of that decision
            3. Brief reasoning for this prediction
            
            Format your response as:
            DECISION: [your decision]
            OUTCOME: [predicted outcome]
            REASONING: [brief explanation]
            """

            response = self.agent.run(prompt)
            result = self._parse_response(response)
            results.append(result)

        return results

    def _parse_response(self, response: str) -> Dict[str, str]:
        """Parse the agent's response into structured data."""
        lines = response.strip().split("\n")
        result = {"decision": "", "outcome": "", "reasoning": ""}

        for line in lines:
            if line.startswith("DECISION:"):
                result["decision"] = line.replace("DECISION:", "").strip()
            elif line.startswith("OUTCOME:"):
                result["outcome"] = line.replace("OUTCOME:", "").strip()
            elif line.startswith("REASONING:"):
                result["reasoning"] = line.replace("REASONING:", "").strip()

        return result
