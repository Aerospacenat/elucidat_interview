def before_scenario(context, scenario):
    """
    before setups the environment for the scenario
    """
    context.environment = {}


def after_scenario(context, scenario):
    """
    this is the teardown function for the scenario
    """
    context.driver.quit()
