class TextEditor:
    def __init__(self) -> None:
        self.current_str = ''
        self.states = ['']
        self.last_command = None
        self.position_state = 0
        self.allow_undo, self.allow_redo = False, False

    def add(self, addition_str: str) -> str:
        self.current_str += addition_str
        self.states.append(self.current_str)

        if self.allow_undo:
            self.allow_undo = False
            self.current_str = self.states[self.position_state]
            return self.current_str
        self.allow_undo = True
        self.allow_redo = False
        self.position_state += 1
        return self.current_str

    def remove(self, count_remove: int) -> str:
        if count_remove > len(self.current_str):
            self.current_str = ''
            self.states.append(self.current_str)
            return self.current_str
        self.current_str = self.current_str[
                           :len(self.current_str) - count_remove
                           ]
        self.states.append(self.current_str)

        if self.allow_undo:
            self.allow_undo = False
            self.current_str = self.states[self.position_state]
            return self.current_str
        self.allow_undo = True
        self.allow_redo = False
        self.position_state += 1
        return self.current_str

    def get(self, index: int) -> str:
        if index >= len(self.current_str):
            return ''
        return self.current_str[index]

    def undo(self) -> str:
        if not self.allow_undo:
            return self.current_str
        self.allow_undo = True
        self.allow_redo = True

        self.position_state -= 1
        return self.current_str

    def redo(self) -> str:
        if not self.allow_redo:
            return self.current_str
        return self.current_str

    def run_command(self, num_command, param) -> str:
        if num_command not in ['1', '2', '3', '4', '5']:
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


print(BastShoe('1 Привет'))
print(BastShoe('1 , Мир!'))
print(BastShoe('1 ++'))
print(BastShoe('2 2'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('1 *'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('3 6'))
print(BastShoe('2 100'))
