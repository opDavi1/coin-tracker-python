# this file is part of coin-tracker by opdavi1 and subject to the GNU GPL-3.0-or-later license.
# See LICENSE for details or go to <https://www.gnu.org/licenses/>

import os
import toml


DEFAULT_SETTINGS = {
    "api_key": "",
    "database_name": "database",
    "img_directory": "./img",
}


if not os.path.isfile("settings.toml"):
    f = open("settings.toml", "w")
    toml.dump(DEFAULT_SETTINGS, f)
    f.close()

global settings
settings = toml.load("settings.toml")
