from dotamatch import api

class Economy(api.Api):
    url = "http://api.steampowered.com/IEconItems_570/GetSchema/v0001/?"

    def items(self, **kwargs):
        """
        Cosmetic items.

        Available options are:
        language=<lang code>
        """
        return self._get(**kwargs)
