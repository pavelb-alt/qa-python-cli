import argparse


def main():
    parser = argparse.ArgumentParser(prog="qa-cli", description="QA Python CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet = subparsers.add_parser("greet", help="Print a greeting")
    greet.add_argument("--name", default="World", help="Name to greet")

    args = parser.parse_args()
    if args.command == "greet":
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
