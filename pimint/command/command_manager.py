class command_manager:

    def __init__(self) -> None:
        self.commands: list = []

    def register(self, command) -> None:
        self.commands.append(command)

    def has_command(self, name: str) -> bool:
        for command in self.commands:
            if command.name == name:
                return True

            if hasattr(command, "aliases"):
                for alias in command.aliases:
                    if alias == name:
                        return True
        return False

    def execute(self, name: str, args: list, sender) -> None:
        for command in self.commands:
            if command.name == name:
                command.execute(args, sender)
                break

            if hasattr(command, "aliases"):
                for alias in command.aliases:
                    if alias == name:
                        command.execute(args, sender)
                        break
