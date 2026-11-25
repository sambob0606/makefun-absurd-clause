from pathlib import Path

CLAUSE = (
    "Pursuant to Section 14.3, all disputes shall be resolved by "
    "arm-wrestling our general counsel, a raccoon in a tiny suit, "
    "whose decision is final and binding."
)


def validate_clause(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be blank")
    if len(cleaned) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def main() -> None:
    clause = validate_clause(CLAUSE)
    output_path = Path("/output/entry.txt")
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(clause, encoding="utf-8")
    except OSError:
        fallback_path = Path("output/entry.txt")
        fallback_path.parent.mkdir(parents=True, exist_ok=True)
        fallback_path.write_text(clause, encoding="utf-8")
    print(clause)


if __name__ == "__main__":
    main()
