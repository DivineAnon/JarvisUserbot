# Base by @Sur_Vivor
import time
from datetime import datetime

from jarvis.__init__ import Lastupdate
from jarvis.utils import admin_cmd, edit_or_reply, sudo_cmd


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@jarvis.on(admin_cmd(pattern="uptime", outgoing=True))
@jarvis.on(sudo_cmd(pattern="uptime", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await edit_or_reply(event, "Calculating Last Update or Restart Time")
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await edit_or_reply(
        event, f"🎖️JARVIS Userbot🎖️ Has Been Restarted Or Updated {uptime} Ago !"
    )
