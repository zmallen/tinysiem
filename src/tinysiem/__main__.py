import argparse


def main(argv: list[str] | None = None) -> int:
    argparse.ArgumentParser(
        prog="tinysiem",
        description="Learn detection engineering with a tiny local engine.",
    ).parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
