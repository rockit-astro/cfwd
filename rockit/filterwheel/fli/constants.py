#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by filterwheeld"""

from rockit.common import TFmt


class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2
    InvalidControlIP = 3
    DeviceNotFound = 4
    InvalidFilter = 5
    NotConnected = 7
    NotDisconnected = 8

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        3: 'error: command not accepted from this IP',
        4: 'error: device not found',
        5: 'error: invalid filter',
        7: 'error: filter wheel is not connected',
        8: 'error: filter wheel is already connected',

        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with filter wheel daemon',
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return 'error: Unknown error code {}'.format(error_code)


class CFWStatus:
    """Status of the filter wheel hardware"""
    Disabled, Initializing, Idle, Moving = range(4)

    _labels = {
        0: 'OFFLINE',
        1: 'INITIALIZING',
        2: 'IDLE',
        3: 'MOVING'
    }

    _formats = {
        0: TFmt.Bold + TFmt.Red,
        1: TFmt.Bold + TFmt.Yellow,
        2: TFmt.Bold,
        3: TFmt.Bold + TFmt.Yellow
    }

    @classmethod
    def label(cls, status, formatting=False):
        """Returns a human readable string describing a status
           Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
