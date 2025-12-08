class Dragon:
    """
    Unified dragon model consumed by builder and streamlit.
    Behaves like a data container but supports formatted statblocks.
    """

    def __init__(self, data: dict):
        # copy all fields into attributes:
        for k, v in data.items():
            setattr(self, k, v)

    # --------------------------------------------------------
    # Useful derived fields
    # --------------------------------------------------------

    @property
    def hd_string(self):
        """Return HD formatted for display (e.g. 20 HD)."""
        return f"{self.hd} HD"

    @property
    def legendary(self):
        """True if dragon has legendary increments."""
        return getattr(self, "legendary_increments", 0) > 0

    @property
    def age_range(self):
        """Return age range tuple from AGE_DATA."""
        return getattr(self, "years", None)

    # --------------------------------------------------------
    # Formatted attack routine
    # --------------------------------------------------------

    def attack_block(self):
        """
        Returns a string like:
        'Claw 1d6, Claw 1d6, Bite 2d10'
        Legendary bonuses not added here yet unless you want.
        """
        routine = getattr(self, "attack_routine", [])
        dmg = getattr(self, "damage_profile", [])

        parts = []
        for attack, damage in zip(routine, dmg if isinstance(dmg, (list, tuple)) else [dmg]):
            parts.append(f"{attack.capitalize()} {damage}")

        return ", ".join(parts)

    # --------------------------------------------------------
    # Breath weapon summary
    # --------------------------------------------------------

    def breath_block(self):
        if not getattr(self, "has_breath_weapon", False):
            return "No breath weapon"

        bw = self.breath_weapon
        mode = self.breath_use["label"]

        return f"{bw['shape']} ({bw['area']}), {bw['damage_type']}, {mode}"

    # --------------------------------------------------------
    # Special abilities section
    # --------------------------------------------------------

    def specials_block(self):
        specials = getattr(self, "special_abilities_list", [])
        if not specials:
            return "None"
        return ", ".join(specials)

    # --------------------------------------------------------
    # Full statblock (ACKS style)
    # --------------------------------------------------------

    def statblock(self):
        """
        Return a nicely formatted multi-line statblock for printing.
        This does not affect Streamlit JSON output.
        """
        lines = []

        lines.append(f"{self.color.capitalize()} {self.habitat} Dragon")
        lines.append(f"Age: {self.age_category}")
        lines.append(f"Alignment: {self.alignment}")
        lines.append("")
        lines.append(f"AC {self.ac}, {self.hd_string}, Save {self.save_as}, ML {self.morale}")
        lines.append(f"Size: {self.size}")
        lines.append("")
        lines.append(f"Attacks: {self.attack_block()}")
        lines.append(f"Breath: {self.breath_block()}")
        lines.append("")
        lines.append(f"Special Abilities: {self.specials_block()}")
        lines.append("")
        lines.append(f"Treasure Type: {', '.join(self.encounter['treasure_type'])}")

        if self.legendary:
            lines.append(f"Legendary increments: {self.legendary_increments}")

        return "\n".join(lines)

    # --------------------------------------------------------
    # JSON-friendly representation
    # --------------------------------------------------------

    def to_dict(self):
        """Convert all attributes back to a JSON-serializable dict."""
        return self.__dict__

    def __repr__(self):
        return f"<Dragon {self.color} {self.habitat} ({self.age_category})>"
