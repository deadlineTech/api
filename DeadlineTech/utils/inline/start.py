from pyrogram.types import InlineKeyboardButton
from pyrogram.types import WebAppInfo

import config
from DeadlineTech import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
         [InlineKeyboardButton(text=_["S_B_6"], web_app=WebAppInfo(url="https://telegra.ph/BSH-MUSIC-BOT-%E1%80%A1%E1%80%9E%E1%80%95%E1%80%94%E1%80%8A-05-30"))],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_7"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons
