from colorama import init, Fore, Style

init()


def print_enabled_state(enabled):
    if enabled:
        print(f'{Fore.GREEN}✅ ENABLED{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}❌ DISABLED{Style.RESET_ALL}')
