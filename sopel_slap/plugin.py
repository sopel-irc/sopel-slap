"""Sopel Slap plugin

Plugin for Sopel that lets users slap each other in fun ways.

Original slap.py copyright 2009, Michael Yanovich, yanovich.net.

This reworked version for Sopel 7.1+ copyright 2024, dgw, technobabbl.es

https://sopel.chat
"""
from __future__ import annotations

from sopel import formatting, plugin

from .util import slap


@plugin.commands('slap', 'slaps')
def slap_command(bot, trigger):
    """Slap a <target> (e.g. nickname)"""
    target = trigger.group(3)

    if target is None:
        target = trigger.nick
    else:
        target = formatting.plain(target)

    return slap(bot, trigger, target)
