from dragonfly import Dictation, Repeat, Pause, MappingRule, ShortIntegerRef
from castervoice.lib.actions import Text, Key, Mouse
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R



class AnkiRule(MappingRule):
    mapping = {
        "deck <n>":
            R(Key("tab")*Repeat(extra='n')),
    }

    extras = [
        ShortIntegerRef("n", 1, 1000),
    ]
    defaults = {"n": 1, "dict": "nothing"}


def get_rule():
    return AnkiRule, RuleDetails(name="anki", executable="anki")