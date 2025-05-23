import click
from decision_simulator.simulator import DecisionSimulator


@click.command()
@click.option("--scenario", "-s", help="Decision scenario to simulate")
@click.option("--iterations", "-i", default=1, help="Number of simulation iterations")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def main(scenario, iterations, verbose):
    """Decision Simulator - Simulate outcomes of decisions using AI agents."""
    if not scenario:
        click.echo("Please provide a scenario with --scenario or -s")
        return

    simulator = DecisionSimulator(verbose=verbose)
    results = simulator.simulate(scenario, iterations=iterations)

    click.echo(f"\nSimulation Results for: {scenario}")
    click.echo("=" * 50)
    for i, result in enumerate(results, 1):
        click.echo(f"\nIteration {i}:")
        click.echo(f"Decision: {result['decision']}")
        click.echo(f"Outcome: {result['outcome']}")
        if verbose:
            click.echo(f"Reasoning: {result['reasoning']}")


if __name__ == "__main__":
    main()
