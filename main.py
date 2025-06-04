import yaml
from strategies.console import ConsoleOutputStrategy
from strategies.redis import RedisStrategy
from strategies.kafka import KafkaStrategy
from data_loader import read_csv
from context import OutputContext

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
strategy_name = config['output_strategy']

if strategy_name == 'console':
    strategy = ConsoleOutputStrategy()
elif strategy_name == 'kafka':
    strategy = KafkaStrategy()
elif strategy_name == 'redis':
    strategy = RedisStrategy()
else:
    raise ValueError('Невідома стратегія')

data = read_csv('police_incidents.csv')
context = OutputContext(strategy)
context.execute(data)

