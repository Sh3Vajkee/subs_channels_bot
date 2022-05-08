from aiogram import Dispatcher, types
from db.models import GroupsUsers
from sqlalchemy import delete


async def new_member(u: types.ChatMemberUpdated):
    # db = u.bot.get("db")

    # if u.new_chat_member.status == "member":
    #     async with db() as ssn:
    #         await ssn.merge(GroupsUsers(
    #             user_id=u.new_chat_member.user.id,
    #             group_id=u.chat.id
    #         ))
    #         await ssn.commit()
    #         await ssn.close()
    # elif u.new_chat_member.status == "left":
    #     async with db() as ssn:
    #         await ssn.execute(delete(GroupsUsers).filter(
    #             GroupsUsers.user_id == u.new_chat_member.user.id).filter(
    #                 GroupsUsers.group_id == u.chat.id))
    #         await ssn.commit()
    #         await ssn.close()

    # stj = u.new_chat_member
    # print(stj)
    # print(u.chat.id)
    # groups = [-1001757816271, -1001755813658, -1001783094322]
    pass


def groups_handlers(dp: Dispatcher):
    dp.register_chat_member_handler(new_member)
