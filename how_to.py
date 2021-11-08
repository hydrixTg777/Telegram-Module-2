



import requests

from . import *


@beast_cmd(pattern=".htg ?(.*)")
async def _(e):
    text = e.pattern_match.group(1)
    if not text:
        return await eod(e, "`Give some text`")
    url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        text.replace(" ", "+")
    )
    response = requests.get(url).text
    if response:
        await eor(e, "[{}]({})\n`Thank me Later 🙃` ".format(text, response.rstrip()))
    else:
        await eod(e, "`something is wrong. please try again later.`")


@beast_cmd(pattern=".htd ?(.*)")
async def _(e):
    text = e.pattern_match.group(1)
    if not text:
        return await eod(e, "`Give some text`")
    url = "https://da.gd/s?url=https://lmddgtfy.net/?q={}".format(
        text.replace(" ", "+")
    )
    response = requests.get(url).text
    if response:
        await eor(e, "[{}]({})\n`Thank me Later 🙃` ".format(text, response.rstrip()))
    else:
        await eod(e, "`something is wrong. please try again later.`")
CMD_HELP.update(
    {
        "": """**Plugin : **`How_to`
        
       ✘ Commands Available -

• `.htg <text>`
   How To Google.
   Some peoples don't know how to google so help them 🙃🙂.

• `.htd <text>`
   How to duck duck go...

"""
    }
)
