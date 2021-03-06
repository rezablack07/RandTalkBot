# RandTalkBot Bot matching you with a random person on Telegram.
# Copyright (C) 2016 quasiyoke
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging

class Wizard:
    async def activate(self):
        raise NotImplementedError()

    async def deactivate(self):
        raise NotImplementedError()

    async def handle(self, text):
        '''
        @returns `True` if message was interpreted in this method. `False` if message still needs
            interpretation.
        '''
        raise NotImplementedError()
