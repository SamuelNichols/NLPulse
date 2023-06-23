import os
import asyncio

from interactions import (
    slash_command,
    SlashContext,
    Client,
    Intents,
    listen,
    ContextMenuContext,
    Message,
    message_context_menu,
    user_context_menu,
    Member,
    ActionRow,
    Button,
    spread_to_rows,
    ButtonStyle,
    component_callback,
    ComponentContext,
    Modal,
    ShortText,
    ParagraphText,
    ModalContext
)
from interactions.api.events import Component

token = os.getenv("HARUHI_BOT_TOKEN")

bot = Client(intents=Intents.DEFAULT)

bot.load_extension("extensions.__init__")


@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@listen()
async def on_message_create(event):
    # This event is called when a message is sent in a channel the bot can see
    print(f"message received: {event.message.content}")


@slash_command(name="my_command", description="My first command :)")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")


@slash_command(name="my_long_command", description="My second command :)")
async def my_long_command_function(ctx: SlashContext):
    # need to defer it, otherwise, it fails
    await ctx.defer()

    # do stuff for a bit
    await asyncio.sleep(600)

    await ctx.send("Hello World")


@message_context_menu(name="repeat")
async def repeat(ctx: ContextMenuContext):
    message: Message = ctx.target
    await ctx.send(message.content)


@user_context_menu(name="ping")
async def ping(ctx: ContextMenuContext):
    member: Member = ctx.target
    await ctx.send(member.mention)

    components: list[ActionRow] = spread_to_rows(
        Button(
            custom_id="click_me",
            style=ButtonStyle.GREEN,
            label="Click Me",
        ),
        Button(
            style=ButtonStyle.GREEN,
            label="Click Me Too",
        ),
    )

    await ctx.channel.send("Look, Buttons!", components=components)


@component_callback("click_me")
async def my_callback(ctx: ComponentContext):
    await ctx.send("You clicked it!")


@slash_command(name="my_modal_command", description="Playing with Modals")
async def my_command_function(ctx: SlashContext):
    my_modal = Modal(
        ShortText(label="Short Input Text", custom_id="short_text"),
        ParagraphText(label="Long Input Text", custom_id="long_text"),
        title="My Modal",
    )
    await ctx.send_modal(modal=my_modal)
    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
    await modal_ctx.send(f"""You input {modal_ctx.responses["short_text"]} and {modal_ctx.responses["long_text"]}""")

bot.start(token)
