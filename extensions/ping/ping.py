import interactions

class Ping(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.slash_command(
        name="ping",
        description="basic ping command",
    )
    async def ping(self, ctx: interactions.InteractionContext) -> None:
        embed = interactions.Embed(
            title="pong",
            description=f"latency: {self.client.latency * 1000:.0f}ms"
        )

        await ctx.send(embeds=embed)

def setup(client) -> None:
    Ping(client)
    print("loaded ping extension")
    