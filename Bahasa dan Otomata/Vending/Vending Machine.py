class VendingMachine:
    def __init__(self, dfa_config):
        self.states = {}
        self.current_state = 'S0'
        self.accept_states = []
        self.load_dfa(dfa_config)

    def load_dfa(self, dfa_config):
        with open(dfa_config, 'r') as file:
            lines = file.readlines()
            # states
            self.states = {}
            states_line = lines[1].strip().split(": ")[1].split(", ")
            for line in lines[5:]:  # Mulai dari baris Transitions
                parts = line.strip().split()
                if len(parts) == 3:
                    self.states[(parts[0], int(parts[1]))] = parts[2]
            # accept states
            self.accept_states = lines[3].strip().split(": ")[1].split(", ")

    def transition(self, input_value):
        if (self.current_state, input_value) in self.states:
            new_state = self.states[(self.current_state, input_value)]
            self.current_state = new_state
            return new_state, True
        else:
            return self.current_state, False

    def is_accepted(self):
        return self.current_state in self.accept_states

    def reset(self):
        self.current_state = 'S0'


def main():
    vending_machine = VendingMachine('vending_dfa.txt')
    total_money = 0
    product_prices = {'A': 3000, 'B': 4000, 'C': 6000}
    selected_product = None
    transition_path = ['S0']  # Menyimpan lintasan DFA

    while True:
        user_input = input("Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): ")
        
        if user_input in ['A', 'B', 'C']:
            selected_product = user_input
            price = product_prices[selected_product]
            if total_money < price:
                print(f"Lintasan DFA: {' → '.join(transition_path)}")
                print("Uang tidak cukup.")
                print("Status: REJECTED.")
            else:
                change = total_money - price
                print(f"Lintasan DFA: {' → '.join(transition_path)}")
                print(f"Minuman {selected_product} dapat dibeli.")
                print("Status: ACCEPTED.")
                if change > 0:
                    print(f"Kembalian: {change}")
            break
        else:
            try:
                money = int(user_input)
                if money in [1000, 2000, 5000, 10000]:
                    if total_money + money > 10000:
                        print("Jumlah uang maksimal yang dapat dimasukkan adalah Rp10.000.")
                    else:
                        total_money += money
                        new_state, success = vending_machine.transition(money)
                        if success:
                            if new_state != transition_path[-1]:  
                                transition_path.append(new_state)
                            print(f"Total uang: {total_money}")

                            # Menampilkan minuman yang dapat dibeli
                            available_drinks = []
                            for product, price in product_prices.items():
                                if total_money >= price:
                                    available_drinks.append(f"Minuman {product}")
                            if available_drinks:
                                print("ON: " + ", ".join(available_drinks))
                        else:
                            print("Transisi tidak valid.")
                else:
                    print("Input tidak valid.")
            except ValueError:
                print("Input tidak valid.")

if __name__ == "__main__":
    main()
    