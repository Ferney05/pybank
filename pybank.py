
import json
import os
from colorama import Fore
import pyfiglet

class PyBank:
    def __init__(self):
        self.acounts = 0
             
    def withdraw(self, number):
        font = pyfiglet.figlet_format('Retirar')
        print(Fore.BLUE + font)    
        
        amount = int(input('\n¡Cuánto?: '))
        number = str(input('Cel +57: '))
                
        with open(f'{number}.json', 'r') as file:
            data_users = json.load(file)
        
        if isinstance(data_users, dict):
            if data_users.get('saldo') > 0:
                if amount <= data_users.get('saldo'):
                    data_users['saldo'] -= amount
                    
                    with open(f'{number}.json', 'w') as file:
                        json.dump(data_users, file, indent=2)
                
                    with open(f'{number}movements.txt', 'a') as file:    
                        if isinstance(data_users, dict):
                            show_values = f'\nHas retirado: {amount}\n'
                            file.write(show_values)
                    
                    print(f'\nRetiro exitoso.\nHas retirado ${amount}.')
                else:
                    print('\nNo se puede retirar, la cantidad a retirar es mayor que tu saldo.')
            else:
                print('\nNo tienes saldo.')
        else:
            print('\nError en la estructura de datos del usuario.')
            
    def send(self, number):
        font = pyfiglet.figlet_format('Enviar')
        print(Fore.BLUE + font)    
        
        number_account_send = str(input('Cel +57: '))
        amount_send = int(input('¿Cuánto?: '))        
        
        with open(f'{number}.json', 'r') as file:
            data_users = json.load(file)
            
        if number_account_send == number_account_send.upper():
            with open(f'{number_account_send}.json', 'r') as file:
                data_user_final = json.load(file)
            
            if isinstance(data_users, dict) and isinstance(data_user_final, dict):
                if data_users.get('saldo') > 0:
                    if amount_send <= data_users.get('saldo'):
                        data_users['saldo'] -= amount_send
                        data_user_final['saldo'] += amount_send
                        print('\nTransferencia exitosa.')
                    else:
                        print('\nLa cantidad a enviar es mayor que tu saldo.')
                else:
                    print('\nNo tienes saldo.')
            else:
                print('\nError en la estructura de datos de las cuentas.')

                
            with open(f'{number}.json', 'w') as file:
                json.dump(data_users, file, indent=2)
                
            with open(f'{number_account_send}.json', 'w') as file:
                json.dump(data_user_final, file, indent=2)
                            
            if not data_users['saldo'] < amount_send:
                with open(f'{number_account_send}movements.txt', 'a') as file:
                    if isinstance(data_user_final, dict):
                        show_values = f"\nEnvio recibido\n\nDe: {data_users['titular']}\nCuanto?:' {amount_send}\n"
                        file.write(show_values)
                
                with open(f'{number}movements.txt', 'a') as file:    
                    if isinstance(data_users, dict):
                        show_values = f'\nEnvio realizado\n\nPara: {data_user_final['titular']}\nCuanto?: {amount_send}\nNumero PyBank: {number_account_send}\n'
                        
                        file.write(show_values)  
        else:
            print('\nError: El número de cuenta no existe.') 
            self.menu_login(number)
            
    def recharge(self, number):
        font = pyfiglet.figlet_format('Recargar   PyBank')
        print(Fore.BLUE + font)        
        
        amount_recharge = int(input('\n¿Cuánto?: '))
        number = str(input('Cel +57: '))
        
        with open(f'{number}.json', 'r') as file:
            data_users = json.load(file)
            
        if isinstance(data_users, dict):
            data_users['saldo'] += amount_recharge
            print('\nRecarga exitosa.')
        
        with open(f'{number}.json', 'w') as file:
            json.dump(data_users, file, indent=2)
                    
        with open(f'{number}movements.txt', 'a') as file:
            if isinstance(data_users, dict):
                show_values = f"\nRecarga realizada\n\nRecarga en: Punto fisico\nCuanto?: {amount_recharge}\n"
                file.write(show_values)
    
    def change_password(self, number):
        font = pyfiglet.figlet_format('Cambiar   password')
        print(Fore.BLUE + font)

        with open(f'{number}.json', 'r') as file:
            my_data = json.load(file)

        print(f'Hola, {my_data["titular"]}!\n')
        new_password = str(input('Nueva contraseña: '))
            
        if isinstance(my_data, dict):
            my_data['pass'] = new_password.strip()
            print('\nContraseña cambiada con éxito.')
            
        with open(f'{number}.json', 'w') as file:
            json.dump(my_data, file, indent=2)
                   
    def see_balance(self, number):
        font = pyfiglet.figlet_format('\nTu  saldo')
        print(Fore.BLUE + font)
        
        with open(f'{number}.json', 'r') as file:
            my_data = json.load(file)

        print(f'Hola, {my_data["titular"]}!\n')
        
        if isinstance(my_data, dict):
            my_balance = f'Saldo actual: ＄{my_data['saldo']}'
            print(my_balance)
            
        with open(f'{number}.json', 'w') as file:
            json.dump(my_data, file, indent=2)
    
    def create_account_savings(self, number):
        font = pyfiglet.figlet_format('Cuenta   de   ahorros')
        print(Fore.BLUE + font)

        saldo_initial = 0
        
        with open(f'{number}.json', 'r') as file:
            my_data = json.load(file)
            
        print(f'Llena los siguientes campos para crear tu cuenta de ahorros, {my_data["titular"]}\n')
        
        name_account_savings = str(input('Nombre de la cuenta de ahorros: '))
        amount_initial = int(input('Monto inicial ($): '))
        
        print('\n:: Objetivo de ahorro ::\n')
        
        amount_total_reach = int(input('Cantidad total que deseas alcanzar ($): '))
        date_limit = str(input('Fecha limite DD/MM/AAAA: '))
        
        if isinstance(my_data, dict):
            if my_data.get('saldo') > 0:
                if my_data.get('saldo') > amount_initial:
                    saldo_initial += amount_initial
                    my_data['saldo'] -= amount_initial
                    
                    if 'cuenta_ahorros' not in my_data:
                        my_data['cuenta_ahorros'] = []

                    new_account = {f'{name_account_savings.lower()}': {
                        'monto_inicial': saldo_initial, 'cantidad_alcanzar': amount_total_reach, 'fecha_limite': date_limit
                    }}
                    
                    my_data['cuenta_ahorros'].append(new_account)
                    
                    with open(f'{number}.json', 'w') as file:
                        json.dump(my_data, file, indent=2)
                    
                    print('\nCuenta de ahorros creada con éxito.')
                    
                    
                else:
                    print('\nLa cantidad inicial es mayor a tu saldo.')
                    print('No se puedo crear la cuenta de ahorros.')
            else:
                print('\nNo tienes saldo.')
                print('No se puedo crear la cuenta de ahorros.')

    def recharge_my_account_savings(self, number):
        font = pyfiglet.figlet_format('Recargar   cuenta   de   ahorros')
        print(Fore.BLUE + font)
        
        with open(f'{number}.json', 'r') as file:
            my_data = json.load(file)
        
        if 'cuenta_ahorros' in my_data:
            print(f'Tus cuentas de ahorros, {my_data["titular"]}:\n')
        
            for name_account in my_data['cuenta_ahorros']:
                for clave in name_account.keys():
                    print(f'- {clave.capitalize()}')
                
            amount_recharge = int(input('\nCantidad a recargar: '))
            account_recharge = str(input('Cuenta a recargar: '))
                        
            if isinstance(my_data, dict):
                if my_data.get('saldo') > 0:
                    if my_data.get('saldo') > amount_recharge:
                        my_data['saldo'] -= amount_recharge
                        
                        for account in my_data['cuenta_ahorros']:
                            if account_recharge.lower().strip() in account:
                                account[f"{account_recharge.lower().strip()}"]['monto_inicial'] += amount_recharge
                                
                                with open(f'{number}movements.txt', 'a') as file:
                                    show_recharge = f'\nHas recargado: {amount_recharge}\nTipo: Recarga cuenta de ahorros\nPara la cuenta: {account_recharge.lower().strip()}'
                                    
                                    file.write(show_recharge)
                                
                        with open(f'{number}.json', 'w') as file:
                            json.dump(my_data, file, indent=2)
                            
                        print('\nTu cuenta de ahorros fue recargada con éxito.')
                    else:
                        print('\nTu saldo actual es menor que la cantidad a recargar.')
                        print('No se pudo recargar.')
                else:
                    print('\nNo tines saldo.')
                    print('No se pudo recargar.')
        else:
            print('No tienes cuentas de ahorros.')
                
    # Create account and Log-in
    
    def create_user(self):
        font = pyfiglet.figlet_format('Create  Account')
        print(Fore.BLUE + font)
        print('Tu número de cuenta para iniciar sesión será tu número de celular.')
        
        name = str(input('\nNombre: '))
        surname = str(input('Apellido: '))
        number_id = str(input('Número de identidad: '))
        type_id = str(input('Tipo de identidad: '))
        number_account = str(input('Número de celular: '))
        clave = str(input('Clave (4 cifras): '))
        saldo = 0
        
        titular = f'{name.capitalize()} {surname.capitalize()}' 
        
        data_for_account = {'titular': titular, 'tipo_id': type_id, 'numero_id': number_id, 'pass': clave.strip(), 'numero_cuenta': number_account, 'saldo': saldo}
                
        file_json = open(f'{number_account}.json', 'w')
        with open(f'{number_account}movements.txt', 'w') as file_txt:
            json.dump(data_for_account, file_json, indent=2)
            file_txt.write(':::::::::::::::::::::::::')
            file_txt.write('\n:::: Mis Movimientos ::::')
            file_txt.write('\n:::::::::::::::::::::::::\n')

            print('\nCuenta creada con éxito ✔')
        
        file_json.close()
        
        self.acounts += 1
        accounts = {'cantidad_cuentas': self.acounts}

        with open('accounts.json', 'w') as file_account:
            json.dump(accounts, file_account, indent=2)
    
    def menu_login(self, account):
        while True:
            menu = int(input('\n1. Retirar ⬇\n2. Enviar ⮕\n3. Recargar PyBank ⬆\n4. Ver movimientos ≡\n5. Cambiar clave ꗃ\n6. Ver saldo ＄\n7. Crear cuenta de ahorros ✛\n8. Recargar cuenta de ahorros ↺\n9. Cerrar sesión ✖\n\n> '))
            
            if menu == 1:
                self.withdraw(account)
            elif menu == 2:
                self.send(account)
            elif menu == 3:
                self.recharge(account)
            elif menu == 4:
                with open(f'{account}movements.txt', 'r') as file:
                    read = file.read()
                    
                    for info in read.split('\n'):
                        print(info)
            
            elif menu == 5:
                self.change_password(account)
            elif menu == 6:
                self.see_balance(account)
            elif menu == 7:
                self.create_account_savings(account)
            elif menu == 8:
                self.recharge_my_account_savings(account)
            elif menu == 9:
                print('\nSesión cerrada.')
                break
            else:
                print('\nEse rango no existe.')
    
    def login(self):
        font = pyfiglet.figlet_format('Login')
        print(Fore.BLUE + font)

        num_account = str(input('\n+57: '))
        
        if os.path.exists(f'{num_account}.json'):
            to_pass = str(input('Clave: '))

            try:
                with open(f'{num_account}.json') as file:
                    data_users = json.load(file)

                if isinstance(data_users, dict):
                    if data_users.get('pass') == to_pass.strip() and data_users.get('numero_cuenta') == num_account.strip():
                        
                        font = pyfiglet.figlet_format('\nBienvenido  a  PyBank')
                        print(Fore.BLUE + font)

                        print(f'\n¡Hola, {data_users.get("titular")}!')
                        print('¿Qué deseas realizar hoy?\n')
                        
                        self.menu_login(num_account)
                    else:
                        print('\nError: Datos incorrectos.')

            except FileNotFoundError:
                print(f'\nDatos incorrectos o no existen.')
        else: 
            print('\nNo existe una cuenta con ese número de celular.')
            self.create_user()
                        

user = PyBank()

try:
    while True:
        menu = int(input('\n1. Crear cuenta\n2. Iniciar sesión\n\n> '))
        
        if menu == 1:
            user.create_user()
        elif menu == 2:
            user.login()
        else:
            print('\nEse rango no existe.')
            
except Exception as e:
    print(f'\nHubo un error: > {e}')
