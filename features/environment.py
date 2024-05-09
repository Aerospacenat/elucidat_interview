
def before_scenario(context, scenario):
    """
    before setups the environment for the scenario
    """
    context.environment = {}


def after_scenario(context, scenario):
    """
    this is the teardown function for the scenario
    the below method will be called after the scenario is executed
    otherwise it will be skipped
    """
    try:
        context.driver.quit()
    except AttributeError:
        pass

