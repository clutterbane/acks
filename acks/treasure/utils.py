# ============================================================
#  COIN VALUE CONSTANTS
# ============================================================

COIN_GP = {
    "copper": 0.01,      # 100 cp = 1 gp
    "silver": 0.1,       # 10 sp = 1 gp
    "electrum": 0.2,     # 5 ep = 1 gp
    "gold": 1,           # 1 gp = 1 gp
    "platinum": 5,       # 1 pp = 5 gp
}

# ============================================================
#  COIN CONVERSIONS
# ============================================================

def coin_gp_value(coin_type, amount):
    """Return total gp value of given number of coins."""
    return amount * COIN_GP.get(coin_type, 0)

def coin_amount_from_gp(coin, value_gp):
    """
    Given a GP value and coin type, compute how many such coins equal that value.
    Example: 100 gp in silver → 100 / 0.1 = 1000 sp.
    """
    gp_per_coin = COIN_GP.get(coin)
    if gp_per_coin == 0:
        return 0
    return int(value_gp / gp_per_coin)

def coin_weight_st(amount):
    """1000 coins = 1 stone."""
    return amount / 1000
