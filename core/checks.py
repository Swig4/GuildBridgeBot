from core.config import DiscordConfig

from discord.ext import commands


async def has_override_role_predicate(ctx):
    if DiscordConfig.overrideRole in ctx.author._roles or await ctx.bot.is_owner(ctx.author):
        return True
    raise commands.MissingRole(DiscordConfig.overrideRole)

has_override_role = commands.check(has_override_role_predicate)


async def has_command_role_predicate(ctx):
    if DiscordConfig.commandRole in ctx.author._roles or await ctx.bot.is_owner(ctx.author):
        return True
    raise commands.MissingRole(DiscordConfig.commandRole)
    
has_command_role = commands.check(has_command_role_predicate)


async def is_not_blacklisted(ctx):
    if DiscordConfig.blacklistRole in ctx.author._roles:
        raise commands.CheckFailure("You are blacklisted.")
    return True
    
has_blacklist_role = commands.check(is_not_blacklisted)