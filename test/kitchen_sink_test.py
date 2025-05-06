import json
from pathlib import Path

from mistune_slack.util import render_slack_blocks_from_markdown

TEST_DIR: Path = Path(__file__).resolve().parent


def test_kitchen_sink():
    markdown = (TEST_DIR / "kitchen_sink.md.txt").read_text()
    expected_blocks = json.loads((TEST_DIR / "kitchen_sink.json").read_text())
    blocks = render_slack_blocks_from_markdown(markdown)
    assert blocks == expected_blocks

    # pprint(blocks)


def example():
    from rich.pretty import pprint

    markdown = (TEST_DIR / "kitchen_sink.md.txt").read_text()
    blocks = render_slack_blocks_from_markdown(markdown)
    pprint(blocks)

    print(
        "\nTo preview paste this json here: https://app.slack.com/block-kit-builder/\n"
        + json.dumps({"blocks": blocks}, separators=(",", ":"))
    )


if __name__ == "__main__":
    example()
