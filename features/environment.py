import os
import yaml
from utils.browser_manager import BrowserManager

def before_all(context):
    # Get environment from CLI arg or default to 'development'
    env = os.getenv('TEST_ENV', 'development')
    context.env = env

    # Load config.yaml
    config_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'config.yaml')
    with open(config_path, 'r') as f:
        context.config = yaml.safe_load(f)[env]

def before_scenario(context, scenario):
    if "ui" in scenario.feature.filename:
        context.driver = BrowserManager.get_driver()

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
