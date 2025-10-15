"""Conversation Router - registry-based integration layer.

This router keeps conversation handlers separate. It exposes a flexible
`route_conversation` API that accepts optional include/exclude lists so the
caller can decide which handlers to consider. This preserves backward
compatibility while allowing the caller to disable "fun" or "casual" when
desired.

Handlers should implement the lightweight interface:
 - match(query: str) -> bool
 - handle(query: str) -> str

The router loads known handlers and iterates in a priority order.
"""

from typing import Iterable, Optional


def _load_handlers() -> list:
    """Import and return handler modules in priority order.

    Order matters: earlier handlers get the first chance to match.
    Keep `casual` before `fun` by default so greetings/small-talk win over
    joke/fun matches when both could apply.
    """
    handlers = []
    try:
        from lib.conversations.casual import (
            match as casual_match,
            handle as casual_handle,
        )

        handlers.append(("casual", casual_match, casual_handle))
    except Exception:
        # best-effort import; module might be missing during tests or refactor
        pass

    try:
        from lib.conversations.fun import match as fun_match, handle as fun_handle

        handlers.append(("fun", fun_match, fun_handle))
    except Exception:
        pass

    return handlers


def route_conversation(
    query: str,
    include: Optional[Iterable[str]] = None,
    exclude: Optional[Iterable[str]] = None,
) -> Optional[str]:
    """Route a conversational query to the first matching handler.

    Args:
        query: the user's query string
        include: optional iterable of handler names to restrict to (e.g. ['casual'])
        exclude: optional iterable of handler names to skip (e.g. ['fun'])

    Returns:
        Response string if handled, otherwise None.
    """
    if not query or len(query.strip()) < 2:
        return None

    q = query.strip()
    handlers = _load_handlers()

    inc = set(name.lower() for name in include) if include else None
    exc = set(name.lower() for name in exclude) if exclude else set()

    for name, match_fn, handle_fn in handlers:
        lname = name.lower()
        if inc is not None and lname not in inc:
            continue
        if lname in exc:
            continue

        try:
            if match_fn(q):
                return handle_fn(q)
        except Exception:
            # Ignore faulty handlers to keep router robust
            continue

    return None


def is_conversational_query(query: str) -> bool:
    """Quick pre-filter: return True when the query looks conversational.

    This uses the same handler imports and some conservative keyword checks.
    """
    if not query:
        return False

    q = query.lower().strip()

    greeting_words = ["hello", "hi", "hey", "morning", "afternoon", "evening", "night"]
    small_talk = ["how are you", "how're you", "thank", "thanks", "bye", "goodbye"]
    fun_keywords = ["joke", "riddle", "fact", "fun", "laugh", "smile", "play", "game"]
    mood_keywords = ["sad", "happy", "bored", "excited"]
    about_keywords = ["who are you", "what are you", "what can you"]

    all_keywords = greeting_words + fun_keywords + mood_keywords

    if any(word in q for word in all_keywords):
        return True

    if any(phrase in q for phrase in small_talk + about_keywords):
        return True

    return False


# Example usage / quick smoke test when run as script
if __name__ == "__main__":
    tests = [
        ("hello", None),
        ("tell me a joke", None),
        ("what's the time", None),
    ]

    print("=== Router smoke test ===\n")
    for q, _ in tests:
        print(f"Query: {q}")
        print("  default route ->", route_conversation(q))
        print("  exclude fun ->", route_conversation(q, exclude=["fun"]))
        print("  include only fun ->", route_conversation(q, include=["fun"]))
        print()
