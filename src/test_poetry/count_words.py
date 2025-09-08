import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def count_words(filename):
    """Counts the number of words in a file."""
    with open(filename, "r") as f:
        text = f.read()
    words = text.split()
    click.echo(f"Word count: {len(words)}")


if __name__ == "__main__":
    count_words()
