import os
import datetime
import typing


def smart_log(*args, **kwargs) -> None:
    level = kwargs.get('level', 'info').lower()
    timestamp = kwargs.get('timestamp', True)
    date = kwargs.get('date', False)
    save_to = kwargs.get('save_to')
    colored_output = kwargs.get('colored_output', True)  # Fixed variable name

    colors = {
        'info': '\033[94m',
        'debug': '\033[90m',
        'warning': '\033[93m',
        'error': '\033[91m',
        'reset': '\033[0m'  # Added reset color
    }

    level_display = {
        'info': '[INFO]',  # Removed brackets for consistency
        'debug': '[DEBUG]',
        'warning': '[WARNING]',
        'error': '[ERROR]'
    }

    if level not in colors:
        level = 'info'

    message_parts = []
    for argc in args:
        message_parts.append(str(argc))
    message = ' '.join(message_parts)

    time_components = []
    if date:
        time_components.append(datetime.datetime.now().strftime('%Y-%m-%d'))
    if timestamp:
        time_components.append(datetime.datetime.now().strftime('%H:%M:%S'))

    time_prefix = ' '.join(time_components)
    if time_prefix:
        time_prefix += ' '

    # Fixed: Added brackets around level_display
    log_entry = f"{time_prefix}[{level_display[level]}] {message}"

    if colored_output:
        console_output = f"{colors[level]}{log_entry}{colors['reset']}"
    else:
        console_output = log_entry

    # Fixed: file_output should be defined in both cases
    file_output = log_entry

    print(console_output)

    if save_to:
        try:
            with open(save_to, 'a', encoding='utf-8') as f:
                f.write(file_output + '\n')
        except (IOError, OSError) as e:
            # If file saving fails, log the error without causing the main function to crash
            error_msg = f"{datetime.datetime.now().strftime('%H:%M:%S')} [ERROR] Failed to write to log file: {e}"
            if colored_output:
                print(f"{colors['error']}{error_msg}{colors['reset']}")
            else:
                print(error_msg)