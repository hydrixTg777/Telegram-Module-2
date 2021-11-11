import asyncio

import random

from . import *

from telethon import events, Button

sed = '''

**Uploading Episode.... 

▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 0.90%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

fcu = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 1.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

pack = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 3.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

bst = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 6.30%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

bstz = '''import asyncio

import random

from . import *

from telethon import events, Button

sed = '''

**Uploading Episode.... 

▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 0.90%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

fcu = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 1.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

pack = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 3.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

bst = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 6.30%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

bstz = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 10.90%

▫️Filesize > 60.3 MB

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 10.90%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

trx = '''

**Uploading Episode.... 

█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 15.20%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

btc = '''

**Uploading Episode.... 

███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 20.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

eth = '''

**Uploading Episode.... 

███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 30.60%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

src = '''

**Uploading Episode.... 

████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 35.82%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

ace = '''

**Uploading Episode.... 

Hacking... 100%

████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 50.03%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

duke = '''

**Uploading Episode.... 

█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒

❇️ Percentage > 60.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

tms = '''

**Uploading Episode.... 

█████████████████▒▒▒▒▒▒▒▒▒

❇️ Percentage > 78.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

ap = '''

**Uploading Episode.... 

██████████████████████▒▒▒▒

❇️ Percentage > 90.50%

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

sinx = '''

**Uploading Episode.... 

██████████████████████████

❇️ Percentage > 100 % Complete 💯

▫️Filesize > 60.3 MB

▫️Etc -->10m,30s**

'''

@beast_cmd(pattern=".lalit")

async def _(event):

	await event.edit("**Uploading Started.....**")	await asyncio.sleep(4)

	await event.edit(sed)

	await asyncio.sleep(3)

	await event.edit(fcu)

	await asyncio.sleep(3)

	await event.edit(pack)

	await asyncio.sleep(3)

	await event.edit(bst)

	await asyncio.sleep(3)

	await event.edit(bstz)

  await asyncio.sleep(3)

  await event.edit(trx)

  await asyncio.sleep(3)

	await event.edit(btc)

  await asyncio.sleep(3)

	await event.edit(eth)

	await asyncio.sleep(3)

	await event.edit(src)

	await asyncio.sleep(3)

	await event.edit(ace)

	await asyncio.sleep(3)

	await event.edit(duke)

	await asyncio.sleep(3)

	await event.edit(tms)

	await asyncio.sleep(3)

	await event.edit(ap)

	await asyncio.sleep(3)

	await event.edit(sinx)

	await asyncio.sleep(3)

	await event.edit("**Video Cheacking....**")

	await asyncio.sleep(4)

	await event.edit("**Video Extract.....**"")
.
	

	

'''

Video Checking....

Video Extract.....

'''.
