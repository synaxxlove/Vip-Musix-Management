from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="• ʜᴇʟᴩ •", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="• sᴇᴛᴛɪɴɢs •", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✰ 𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ✰",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="✰ 𝐒ᴜᴘᴘᴏʀᴛ ✰", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="✰ 𝐔ᴘᴅᴀᴛᴇ ✰", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="✰ 𝐇ᴇʟᴘ & 𝐂ᴏᴍᴍᴀɴᴅs ✰", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
