import random
import re

# ============================================================
# AUDIT ADAPTER
# ============================================================

def _audit_push(audit, message):
    """
    Universal audit adapter:
    - If audit is a function → call it with message
    - If audit is a list → append message
    - If audit is None → no-op
    """
    if audit is None:
        return

    if callable(audit):
        # frontend-style audit function
        audit(message)
        return

    if hasattr(audit, "append"):
        audit.append(message)
        return

    # fallback (should never happen)
    try:
        audit(message)
    except:
        pass


# ============================================================
# DICE ROLLING
# ============================================================

def roll(dice_str, audit=None, note=None):
    """
    Roll dice like '1d4', '2d20', '3d6', or return 0 if None.
    Supports flexible audit logging.
    """
    if dice_str is None or dice_str == "None":
        return 0

    m = re.match(r"(\d+)d(\d+)", dice_str)
    if not m:
        raise ValueError(f"Invalid dice string: {dice_str}")

    count, sides = map(int, m.groups())
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)

    # --- AUDIT TRAIL ---
    msg = (
        f"{note}: rolled {dice_str} → {rolls} = {total}"
        if note else
        f"Rolled {dice_str} → {rolls} = {total}"
    )
    _audit_push(audit, msg)

    return total


# ============================================================
# PERCENT CHANCE ROLL
# ============================================================

def chance(percent, audit=None, note=None):
    """
    Percent chance roll.
    Supports flexible audit logging.
    """
    r = random.random()
    result = r < (percent / 100)

    msg = (
        f"{note}: chance {percent}% → rolled {r:.3f} → {result}"
        if note else
        f"Chance {percent}% → rolled {r:.3f} → {result}"
    )
    _audit_push(audit, msg)

    return result
