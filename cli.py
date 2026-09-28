import argparse, json, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
from engine.rubric_registry import RubricRegistry

def main():
    parser = argparse.ArgumentParser(description="Universal LLM Rubric CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all available rubrics")
    
    inspect_p = subparsers.add_parser("inspect", help="Inspect a rubric definition")
    inspect_p.add_argument("--rubric", required=True, help="Rubric ID")

    score_p = subparsers.add_parser("score", help="Score a response against a rubric")
    score_p.add_argument("--rubric", required=True, help="Rubric ID")
    score_p.add_argument("--prompt", required=True, help="User Prompt")
    score_p.add_argument("--response", required=True, help="Model Response")

    args = parser.parse_args()
    reg = RubricRegistry()

    if args.command == "list":
        print(f"Loaded {len(reg.list_rubrics())} Rubrics:")
        for r in reg.list_rubrics():
            print(f" - {r}")
    elif args.command == "inspect":
        r = reg.get_rubric(args.rubric)
        if r:
            print(json.dumps(r, indent=2))
        else:
            print(f"Rubric {args.rubric} not found.")
    elif args.command == "score":
        res = reg.evaluate_simple(args.rubric, args.prompt, args.response)
        print(json.dumps(res, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
