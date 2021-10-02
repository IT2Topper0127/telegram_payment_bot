# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#
# Imports
#
import pyrogram
from telegram_payment_bot.config import Config
from telegram_payment_bot.chat_members import ChatMembersList, ChatMembersGetter
from telegram_payment_bot.helpers import MemberHelper


#
# Classes
#

# Members username getter class
class MembersUsernameGetter:
    # Constructor
    def __init__(self,
                 client: pyrogram.Client,
                 config: Config) -> None:
        self.client = client
        self.config = config

    # Get all with username
    def GetAllWithUsername(self,
                           chat: pyrogram.types.Chat) -> ChatMembersList:
        # Filter chat members
        chat_members_getter = ChatMembersGetter(self.client, self.config)
        return chat_members_getter.FilterMembers(
            chat,
            lambda member: MemberHelper.IsValidMember(member) and member.user.username is not None
        )

    # Get all with no username
    def GetAllWithNoUsername(self,
                             chat: pyrogram.types.Chat) -> ChatMembersList:
        # Filter chat members
        chat_members_getter = ChatMembersGetter(self.client, self.config)
        return chat_members_getter.FilterMembers(
            chat,
            lambda member: MemberHelper.IsValidMember(member) and member.user.username is None
        )
