# Victor Smart-Kill

Status and history of Victor-Smart Kill WI-FI electronic mouse and rat traps from VictorPest.com can be accessed with this async Python wrapper module. The wrapper uses the same API as the Victor Pest APP.

[![License][license-shield]](LICENSE)
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

## Getting started

This example gets a list of trap information and trap history for the first trap:

```python
from victor_smart_kill import VictorApi, VictorAsyncClient

async with VictorAsyncClient("username", "password") as client:
    api = VictorApi(client)
    traps = await api.get_traps()
    history = await api.get_trap_history(traps[0].id)
```

[buymecoffee]: https://www.buymeacoffee.com/toreamun
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg
[license-shield]: https://img.shields.io/github/license/toreamun/victor-smart-kill

## API list methods

- get_activity_logs()
- get_mobile_apps()
- get_operators()
- get_profiles()
- get_traps()
- get_trap_history()
- get_users()

## Single item methods.

Each list method usually has corresponding metods to get a single item by id and/or url. You can find the id or url in the result from list mehods.
