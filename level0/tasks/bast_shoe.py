class TextEditor:
    def __init__(self) -> None:
        self.current_str = ''
        self.states = []
        self.last_command = None
        self.undo_states = []

    def add(self, addition_str: str) -> str:
        self.undo_states = []
        self.last_command = 'add'
        self.current_str += addition_str
        self.states.append(self.current_str)
        return self.current_str

    def remove(self, count_remove: int) -> str:
        self.undo_states = []
        self.last_command = 'remove'
        if count_remove > len(self.current_str):
            self.current_str = ''
            self.states.append(self.current_str)
            return ''
        self.current_str = self.current_str[
                           :len(self.current_str) - count_remove
                           ]
        self.states.append(self.current_str)
        return self.current_str

    def get(self, index: int) -> str:
        self.last_command = 'get'
        if index >= len(self.current_str):
            return ''
        return self.current_str[index]

    def undo(self) -> str:
        self.last_command = 'undo'
        self.undo_states.append(self.states.pop())
        self.current_str = self.states[-1]
        return self.current_str

    def redo(self) -> str:
        if self.last_command == 'undo':
            self.current_str = self.undo_states.pop(0)
        self.last_command = 'redo'
        return self.current_str

    def run_command(self, num_command, param) -> str:
        if num_command not in ['1', '2', '3', '4', 5]:
            return self.current_str
        if num_command == '1':
            return self.add(addition_str=param)
        if num_command == '2':
            return self.remove(count_remove=int(param))
        if num_command == '3':
            return self.get(index=int(param))
        if num_command == '4':
            return self.undo()
        return self.redo()


text_editor = TextEditor()


def BastShoe(command: str) -> str:
    num_command = command[0]
    param = command[1:].strip()
    return text_editor.run_command(num_command, param)