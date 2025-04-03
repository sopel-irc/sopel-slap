"""Configuration definitions

Part of `sopel-slap`.

Copyright 2024, dgw, technobabbl.es

https://sopel.chat
"""
from __future__ import annotations

from sopel.config import types

VERBS = (
    'annihilates',
    'destroys',
    'kicks',
    'owns',
    'punches',
    'pwns',
    'roundhouse kicks',
    'slaps',
    'hits',
    'smacks',
    'bashes',
    'whacks',
    'punches',
    'bonks',
    'tickles',
    'karate chops',
    'throws a pie at',
    'elbows',
    'dropkicks',
    'boops',
    'facepalms',
    'smushes',
    'zaps',
    'throws a shoe at',
    'pokes',
    'squishes',
    'yeets',
    'hurls a tomato at',
    'shakes',
    'headbutts',
    'body slams',
    'throws glitter at',
    'jumps on',
    'throws a water balloon at',
    'dunks',
    'throws a snowball at',
    'throws confetti at',
    'throws a banana peel at',
    'throws lego bricks at',
    'hurls pancakes at',
    'throws a cactus at',
    'blasts airhorn at',
    'splatters paint on',
    'locks in a room with bad music',
    'hurls marshmallows at',
)


class SlapSection(types.StaticSection):
    verbs = types.ListAttribute('verbs', default=VERBS)
    """Verbs to choose from when slapping someone."""

    reflexive = types.ValidatedAttribute('reflexive', default='itself')
    """The reflexive pronoun the bot uses when someone slaps it."""


def do_configure(section: types.StaticSection):
    section.configure_setting(
        'verbs',
        "\nEnter verbs to choose from when slapping someone, one per line.\n\n"
        "Alternatively, press Enter twice without typing anything to write\n"
        "the current list (shown below) to your bot's .cfg file, where it\n"
        "can be edited using your favorite text editor.\n\n"
        "Current verb list:",
    )
    section.configure_setting(
        'reflexive',
        "What pronoun should the bot use for itself when someone slaps it?",
    )
