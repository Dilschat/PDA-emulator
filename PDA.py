from types import MethodType


class State:

    def perform_step(self, input_item):
        return input_item in self.acceptable_input


class PDA(object):
    def __init__(self, input_string):
        self.input = input_string
        self.current_state = state0
        self.stack = list()
        self.stack.append('')

    def launch_pda(self):
        for i in self.input:
            try:
                print(i)
                self.current_state.perform_step(i, self)
            except InputError:
                self.invalid_case_print()
                exit()
        self.stack.append(i)
        self.current_state.perform_step('',pda)

    def is_input_valid(self):
        list_of_open_par = list()
        list_of_close_par = list()
        for i in range(0, len(self.stack)):
            if self.stack[i] == '(':
                list_of_open_par.append(i)
            elif self.stack[i] == ')':
                list_of_close_par.append(i)
        if len(list_of_close_par) != len(list_of_close_par):
            self.invalid_case_print()
        else:
            self.valid_case_print(list_of_close_par, list_of_open_par)

    def perform_step_for_state_0(self, input_item, pda):
        if input_item in '(+-':
            pda.current_state = state2
        else:
            pda.current_state = error_state

    def perform_step_for_state_1(self, input_item,pda):
        if input_item in '01':
            pda.current_state = state2
        elif input_item in '(+-':
            pda.current_state = pda.current_state
        else:
            pda.current_state = pda.error_state

    def perform_step_for_state_2(self, input_item,pda):
        if input_item in '01':
            pda.current_state = pda.current_state
        elif input_item in '+-':
            pda.current_state = state1
        elif input_item in '*/':
            pda.current_state = state3
        elif input_item == ')':
            pda.current_state = state4
        else:
            pda.current_state = error_state

    def perform_step_for_state_3(self, input_item,pda):
        if input_item in '01':
            pda.current_state = state2
        elif input_item in '(':
            pda.current_state = state1
        else:
            pda.current_state = error_state

    def perform_step_for_state_4(self, input_item,pda):
        if input_item == '':
            pda.is_input_valid()
        elif input_item in '*/':
            pda.current_state = state3
        elif input_item in ')':
            pda.current_state = pda.current_state
        elif input_item == '+-':
            pda.current_state = state1

        else:
            pda.current_state = error_state

    def perform_error_state(self, input_item, pda):
        raise InputError()

    def invalid_case_print(self):
        print("invalid")

    def valid_case_print(self, closes, opens):
        print("valid")


class InputError(Exception):
    pass


if __name__ == "__main__":
    state0 = State()
    state1 = State()
    state2 = State()
    state3 = State()
    state4 = State()
    error_state = State()
    state0.perform_step = MethodType(PDA.perform_step_for_state_0, state1)
    state1.perform_step = MethodType(PDA.perform_step_for_state_1, state1)
    state2.perform_step = MethodType(PDA.perform_step_for_state_2, state2)
    state3.perform_step = MethodType(PDA.perform_step_for_state_3, state3)
    state4.perform_step = MethodType(PDA.perform_step_for_state_4, state4)
    error_state.perform_step = MethodType(PDA.perform_error_state, error_state)
    pda = PDA('(++-+1101+11001)*(11000+(11110))')
    pda.launch_pda()
