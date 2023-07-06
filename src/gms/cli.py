import os

import click
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from gms.gms import Engine

console = Console()


@click.group()
def cli():
    pass


@click.command("init")
@click.option("--config_path", type=click.File(mode="w", encoding="utf-8"))
def init_config(config_path):
    """init config file"""
    config_path.write(
        """# example config file, please fill in the correct information
# If specifying a file is inconvenient, you can also just set an environment variable with the same name.
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USERNAME=root
MONGO_PASSWORD=123456
MONGO_DB_NAME=ms
MONGO_COLLECTION=ms
# sometimes there is too much data in a collection and we cannot traverse all the records. In this case you can select a flag column, where the different contents of the column correspond to the different structure of the records. An example is event.
# The tool will select the most recent record in the matching flag column for analysis. This will speed things up.
MONGO_KEY_COLUMN=ms
    """
    )
    pass


@click.command()
@click.argument("config_path", type=click.Path(exists=True))
@click.option("--output_format", type=click.Choice(["json", "table"]), default="table")
def run(config_path, output_format):
    """Get the schema in a mongo collection"""
    load_dotenv(config_path)
    engine = Engine(
        host=os.getenv("MONGO_HOST"),
        port=int(os.getenv("MONGO_PORT")),
        db_name=os.getenv("MONGO_DB_NAME"),
        username=os.getenv("MONGO_USERNAME"),
        password=os.getenv("MONGO_PASSWORD"),
        collection=os.getenv("MONGO_COLLECTION"),
        key_column=os.getenv("MONGO_KEY_COLUMN"),
    )
    result = engine.get_all_columns()

    render_map = {
        "json": render_json,
        "table": render_table,
    }
    render_map[output_format](result)


def render_table(data):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim")
    table.add_column("Type")
    for result_key, result_value in data.items():
        table.add_row(result_key, result_value)

    console.print(table)


def render_json(data):
    import json
    type_map = {
        "str": "string",
        "dict": "object",
        "float": "string"
    }
    content = [{"name": key, "type": type_map.get(value, "string")} for key, value in data.items()]
    console.print(json.dumps(content, ensure_ascii=False))


cli.help = "get the schema in a mongo collection"
cli.add_command(init_config)
cli.add_command(run)


def main():
    cli()
