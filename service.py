import typing


class Storage:
    """Storage class"""

    def __init__(self):
        self.storage = {}

    def save(self, message: dict):
        """Save message to storage"""
        save_params = {
            "msisdn": message.get('msisdn'),
            "registered": message.get('registered')
        }

        if len(self.storage) != 0:
            self.storage[max(self.storage.keys()) + 1] = save_params
        else:
            self.storage[1] = save_params

    def delete(self, message: dict):
        """Delete message from storage"""
        del self.storage[message.get('id')]

    def get(self) -> dict:
        """Get storage values"""
        return self.storage


class Commands:
    """Commands class"""

    def __init__(self, dict_types: typing.Dict):
        self.dict_types = dict_types

    def process_command(self, message: dict) -> typing.Tuple[int, str]:
        """Process command type"""
        try:
            self.dict_types[message.get('type')](message)
            return 200, "Command complete successfully"
        except KeyError:
            return 404, "Command not found"
        except Exception as e:
            return 500, str(e)

    def add_or_update(self, new_dict_types: typing.Dict):
        """Add or update command"""
        self.dict_types.update(new_dict_types)

    def delete(self, type_name: str):
        """Delete command"""
        try:
            del self.dict_types[type_name]
        except KeyError:
            print("No such command type")


if __name__ == '__main__':
    create_command = {
        'type': 'create',
        'msisdn': '78005553535',
        'registered': '2020-04-01 08:00:31.337+0000'
    }

    delete_command = {
        'type': 'delete',
        'id': 666
    }

    # create storage
    storage = Storage()

    # create commands
    commands = Commands({'create': storage.save, 'delete': storage.delete})

    # save message to storage
    print(commands.process_command(create_command))
    print(storage.get())

    # delete message from storage
    print(commands.process_command(delete_command))
    print(storage.get())
