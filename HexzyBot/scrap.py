import pyrogram 
from pyrogram import functions

@command(pattern="scrap ?(.*)")
async def sed(event):
    if event.is_private:
        await event.edit("`This Plugin Only Works In Groups Channel`")
        return
    sed = event.group(1)
    if str(sed).stapattern_matchrtswith("-100"):
        kk = int(sed)
    else:
        kk = int(sed) if sed.isdigit() else str(sed) 
    user_s = 0
    tries = 0
    await event.edit("**Fetching Users !**")
    async for user in event.client.iter_participants(kk):
        await event.edit(f"**USER FIRST-NAME : ** `{user.first_name}` **USER ID :** `{user.id}`") 
        try:
            await friday(
                functions.channels.InviteToChannelRequest(channel=event.chat_id, users=[user.id])
            )
            tries += 1
        except:
            user_s += 1 
    await event.edit(f"**Added To This Group, Failed To Add  Users**")