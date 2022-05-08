import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import ChatTypeFilter
from keyboars import links_kb


async def start_cmd(m: types.Message):

    await m.answer("<a href='https://t.me/+qMaHf7mWy14zZTVi'>Подать заявку</a>", disable_web_page_preview=True)


async def join_request(req: types.ChatJoinRequest):
    gid = req.chat.id
    uid = req.from_user.id

    await req.bot.send_message(uid, "Подпишись на эти каналы", reply_markup=links_kb)


async def ready_cmd(c: types.CallbackQuery):
    groups = [-1001757816271, -1001755813658, -1001783094322]

    for group in groups:
        check_sub = await c.bot.get_chat_member(group, c.from_user.id)
        if check_sub.status == "left":
            try:
                await c.bot.decline_chat_join_request(-1001730894902, c.from_user.id)
                await c.message.answer("Вы подписались не на все каналы. Заява на вступление отклонена.")
            except:
                await c.message.answer("Вы не подавали заявку на вступление")
            await c.answer()
            return

    try:
        await c.bot.approve_chat_join_request(-1001730894902, c.from_user.id)
        await c.message.answer("Ваша заявка одобрена.")

    except:
        await c.message.answer("Вы не подавали заявку на вступление")
    await c.answer()


def start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_cmd,
        ChatTypeFilter(
            chat_type=[types.ChatType.PRIVATE]
        )
    )
    dp.register_chat_join_request_handler(
        join_request
    )
    dp.register_callback_query_handler(
        ready_cmd,
        ChatTypeFilter(
            chat_type=[types.ChatType.PRIVATE]
        ),
        text="ok"
    )
