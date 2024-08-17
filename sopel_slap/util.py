"""Slap utilities

Part of `sopel-slap`.

Copyright 2024, dgw, technobabbl.es

https://sopel.chat
"""
from __future__ import annotations

import random
from typing import TYPE_CHECKING

from sopel import formatting, tools

if TYPE_CHECKING:
    from sopel.bot import SopelWrapper
    from sopel.trigger import Trigger


def slap(bot: SopelWrapper, trigger: Trigger, nick: str):
    """Do the slapping."""
    # the target could contain formatting control codes, so strip those
    nick = formatting.plain(nick)

    # check for bot-slapping and admin-slapping
    if nick == bot.nick:
        if trigger.admin:
            nick = 'itself'
        else:
            nick = trigger.nick

    if nick in bot.config.core.admins and not trigger.admin:
        nick = trigger.nick

    # ensure target is an Identifier to increase reliability of "is nick" check
    if isinstance(nick, tools.Identifier):
        target = nick
    else:
        if hasattr(bot, 'make_identifier'):
            target = bot.make_identifier(nick)
        else:
            # TODO: remove once Sopel 7 support is dropped
            target = tools.Identifier(nick)

    if not target.is_nick():
        bot.reply("You can't slap the whole channel!")
        return

    if target not in bot.channels[trigger.sender].users and target != 'itself':
        bot.reply("You can't slap someone who isn't here!")
        return

    verb = random.choice(bot.settings.slap.verbs)

    bot.action(f"{verb} {target}")
