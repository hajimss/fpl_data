import aiohttp

from understat import Understat

async def top_three():
    res = []
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        data = await understat.get_league_players(
            "epl", 2022)

        new_data = sorted(data, key=lambda d: d['xG'], reverse=True)

        res = (new_data[:3])
        print(res)
    return res
